# ── Stats ──────────────────────────────────────────────────────────────────────
async def get_stats(_=Depends(require_auth)):
    async with LINKS_LOCK: snap = dict(LINKS)
    return {
        "active_connections": len(connections), "total_traffic_mb": round(stats["total_bytes"] / (1024 ** 2), 2),
        "total_requests": stats["total_requests"], "total_errors": stats["total_errors"],
        "uptime": uptime(), "timestamp": datetime.now().isoformat(),
        "hourly": dict(hourly_traffic), "recent_errors": list(error_logs)[-10:],
        "links_count": len(snap), "active_links": sum(1 for l in snap.values() if is_link_allowed(l)),
        "expired_links": sum(1 for l in snap.values() if is_link_expired(l)), "subs_count": len(SUBS),
        "resellers_count": len(RESELLERS),
    }

@app.get("/api/activity")
async def get_activity(_=Depends(require_auth)):
    return {"logs": list(activity_logs)[-50:]}

# ── Connection grouping ────────────────────────────────────────────────────────
async def group_connections():
    async with LINKS_LOCK: snap_links = dict(LINKS)
    grouped = defaultdict(lambda: {"sessions": 0, "labels": set(), "transports": set(),
                                 "bytes": 0, "first_connected_at": None, "last_connected_at": None})
    for conn in connections.values():
        ip = conn.get("ip", "نامشخص")
        uid = conn.get("uuid", "نامشخص")
        link = snap_links.get(uid)
        if link:
            grouped[ip]["labels"].add(link["label"])
            grouped[ip]["transports"].add(conn.get("transport", "نامشخص"))
        grouped[ip]["sessions"] += 1
        grouped[ip]["bytes"] += conn.get("bytes", 0)
        ca = conn.get("connected_at")
        if ca:
            if not grouped[ip]["first_connected_at"] or ca < grouped[ip]["first_connected_at"]:
                grouped[ip]["first_connected_at"] = ca
            if not grouped[ip]["last_connected_at"] or ca > grouped[ip]["last_connected_at"]:
                grouped[ip]["last_connected_at"] = ca

@app.get("/api/connections")
async def get_connections(_=Depends(require_auth)):
    await group_connections()

# ── Link Management ───────────────────────────────────────────────────────────
@app.post("/api/links")
async def create_link(request: Request):
    s = await require_reseller_auth(request)
    body = await request.json()
    label = (body.get("label") or "لینک جدید").strip()[:60]
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    note = (body.get("note") or "").strip()[:200]
    ips = [ip.strip() for ip in body.get("ips", []) if ip.strip()]
    port = int(body.get("port")) if body.get("port") else None
    is_personal = bool(body.get("is_personal", False))
    sub_id = body.get("sub_id")
    protocol = body.get("protocol") or DEFAULT_PROTOCOL
    if protocol not in PROTOCOLS: protocol = DEFAULT_PROTOCOL

    if s["role"] == "reseller":
        await check_reseller_capacity(s["user_id"], limit_bytes)
        is_personal = True
        ips = []
        port = None
        exp_days = 0
        expires_at = None
        async with RESELLERS_LOCK:
            my_res = RESELLERS.get(s["user_id"])
            sub_id = my_res.get("sub_id") if my_res else None

    flag = ""
    if ips: flag = await fetch_ip_flag(ips[0])
    if flag: label = f"{label} {flag}"

    uid = generate_uuid()
    async with LINKS_LOCK:
        LINKS[uid] = {
            "label": label, "limit_bytes": limit_bytes, "used_bytes": 0,
            "created_at": datetime.now().isoformat(), "active": True,
            "expires_at": expires_at, "note": note, "is_default": False,
            "sub_id": sub_id, "protocol": protocol, "ips": ips, "port": port,
            "is_personal": is_personal, "creator_id": s["user_id"]
        }
        if sub_id:
            async with SUBS_LOCK:
                if sub_id in SUBS:
                    ids = SUBS[sub_id].setdefault("link_ids", [])
                    if uid not in ids: ids.append(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{label}» توسط {s['user_id']} ساخته شد", "ok")
    host = get_host()
    vless_list = generate_vless_links(LINKS[uid], uid, host)
    return {"uuid": uid, **LINKS[uid], "vless_link": "\n".join(vless_list),
            "sub_url": f"https://{host}/sub/{uid}"}

@app.post("/api/links/bulk")
async def create_links_bulk(request: Request):
    s = await require_reseller_auth(request)
    body = await request.json()
    count = min(int(body.get("count", 1)), 100)
    if count < 1: count = 1
    base_label = (body.get("label") or "Bulk").strip()[:40]
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    ips = [ip.strip() for ip in body.get("ips", []) if ip.strip()]
    port = int(body.get("port")) if body.get("port") else None
    is_personal = bool(body.get("is_personal", False))
    sub_id = body.get("sub_id")
    protocol = body.get("protocol") or DEFAULT_PROTOCOL
    if protocol not in PROTOCOLS: protocol = DEFAULT_PROTOCOL

    if s["role"] == "reseller":
        await check_reseller_capacity(s["user_id"], limit_bytes * count)
        is_personal = True
        ips = []
        port = None
        exp_days = 0
        expires_at = None
        async with RESELLERS_LOCK:
            my_res = RESELLERS.get(s["user_id"])
            sub_id = my_res.get("sub_id") if my_res else None

    created_uids = []
    host = get_host()
    for i in range(count):
        target_ip = ips[i % len(ips)] if ips else ""
        flag = await fetch_ip_flag(target_ip) if target_ip else ""
        label = f"{base_label}-{i+1}" + (f" {flag}" if flag else "")
        uid = generate_uuid()
        async with LINKS_LOCK:
            LINKS[uid] = {
                "label": label, "limit_bytes": limit_bytes, "used_bytes": 0,
                "created_at": datetime.now().isoformat(), "active": True,
                "expires_at": expires_at, "note": "", "is_default": False,
                "sub_id": sub_id, "protocol": protocol,
                "ips": [target_ip] if target_ip else [],
                "port": port, "is_personal": is_personal, "creator_id": s["user_id"]
            }
            if sub_id:
                async with SUBS_LOCK:
                    if sub_id in SUBS:
                        ids = SUBS[sub_id].setdefault("link_ids", [])
                        if uid not in ids: ids.append(uid)
        created_uids.append(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"{count} کانفیگ {base_label} ساخته شد", "ok")
    all_vless = []
    for uid in created_uids:
        all_vless.extend(generate_vless_links(LINKS[uid], uid, host))
    sub_url = ""
    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                uuid_key = SUBS[sub_id].get("uuid_key", "")
                if uuid_key: sub_url = f"https://{host}/sub-group/{uuid_key}"
    return {"ok": True, "count": count, "created_uids": created_uids,
            "sub_url": sub_url, "vless_bulk": "\n".join(all_vless)}

# ── لیست، ویرایش، حذف لینک (همون قبلی، بدون تغییر) ────────────────────────
@app.get("/api/links")
async def list_links(request: Request):
    s = await require_reseller_auth(request)
    host = get_host()
    async with LINKS_LOCK:
        result = []
        for uid, d in LINKS.items():
            if s["role"] == "reseller" and d.get("creator_id") != s["user_id"]: continue
            vless_list = generate_vless_links(d, uid, host)
            result.append({"uuid": uid, **d, "expired": is_link_expired(d),
                "vless_link": "\n".join(vless_list), "sub_url": f"https://{host}/sub/{uid}"})
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.patch("/api/links/{uid}")
async def update_link(uid: str, request: Request):
    s = await require_reseller_auth(request)
    body = await request.json()
    async with LINKS_LOCK:
        if uid not in LINKS: raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        if s["role"] == "reseller" and link.get("creator_id") != s["user_id"]:
            raise HTTPException(status_code=403, detail="forbidden")
        if "active" in body: link["active"] = bool(body["active"])
        if "label" in body: link["label"] = str(body["label"])[:60]
        if "note" in body: link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]: link["used_bytes"] = 0
        if "limit_value" in body:
            lv = float(body.get("limit_value") or 0)
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, body.get("limit_unit") or "GB")
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            link["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
        if "ips" in body: link["ips"] = [ip.strip() for ip in body.get("ips", []) if ip.strip()]
        if "port" in body: link["port"] = int(body["port"]) if body.get("port") else None
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/links/{uid}")
async def delete_link(uid: str, request: Request):
    s = await require_reseller_auth(request)
    async with LINKS_LOCK:
        if uid not in LINKS: raise HTTPException(status_code=404, detail="not found")
        if s["role"] == "reseller" and LINKS[uid].get("creator_id") != s["user_id"]:
            raise HTTPException(status_code=403, detail="forbidden")
        sub_id = LINKS[uid].get("sub_id")
        del LINKS[uid]
        if sub_id:
            async with SUBS_LOCK:
                if sub_id in SUBS:
                    ids = SUBS[sub_id].get("link_ids", [])
                    if uid in ids: ids.remove(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ {uid[:8]}... حذف شد", "err")
    return {"ok": True, "deleted": uid}

# ── Reset Reseller Token ──────────────────────────────────────────────────────
@app.post("/api/resellers/{rid}/reset-token")
async def reset_reseller_token(rid: str, _=Depends(require_auth)):
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404, "not found")
        RESELLERS[rid]["login_token"] = secrets.token_urlsafe(16)
    asyncio.create_task(save_state())
    return {"ok": True, "login_token": RESELLERS[rid]["login_token"]}

# ── Reseller Management (Admin Only) ──────────────────────────────────────────
@app.get("/api/resellers")
async def list_resellers(_=Depends(require_auth)):
    host = get_host()
    async with RESELLERS_LOCK: snap_r = dict(RESELLERS)
    async with LINKS_LOCK: snap_l = dict(LINKS)
    result = []
    for rid, r in snap_r.items():
        links_cnt = sum(1 for l in snap_l.values() if l.get("creator_id") == rid)
        allocated = sum(l.get("limit_bytes", 0) for l in snap_l.values() if l.get("creator_id") == rid)
        traffic = sum(l.get("used_bytes", 0) for l in snap_l.values() if l.get("creator_id") == rid)
        result.append({
            "id": rid, "name": r["name"], "active": r.get("active", True),
            "total_bytes": r.get("total_bytes", 0), "total_fmt": fmt_bytes(r.get("total_bytes", 0)),
            "allocated_bytes": allocated, "allocated_fmt": fmt_bytes(allocated),
            "traffic_used": traffic, "traffic_fmt": fmt_bytes(traffic),
            "remaining_bytes": max(0, r.get("total_bytes", 0) - allocated),
            "remaining_fmt": fmt_bytes(max(0, r.get("total_bytes", 0) - allocated)),
            "created_at": r.get("created_at"), "links_count": links_cnt,
            "login_link": f"https://{host}/r/{r.get('login_token', '')}"
        })
    return {"resellers": result}

@app.post("/api/resellers")
async def create_reseller(request: Request, _=Depends(require_auth)):
    body = await request.json()
    name = str(body.get("name", "")).strip()
    pw = str(body.get("password", "")).strip()
    limit_gb = float(body.get("limit_gb") or 0)
    if not name or not pw: raise HTTPException(400, "نام و رمز عبور الزامی است")
    if limit_gb <= 0: raise HTTPException(400, "حجم باید بیشتر از ۰ باشد")
    rid = secrets.token_hex(8)
    sub_id = f"reseller_{rid}"
    async with SUBS_LOCK:
        SUBS[sub_id] = {
            "name": f"گروه {name}",
            "is_personal": True,
            "link_ids": [],
            "created_at": datetime.now().isoformat(),
            "creator_id": rid,
        }
    async with RESELLERS_LOCK:
        RESELLERS[rid] = {
            "name": name, "password_hash": hash_password(pw),
            "total_bytes": parse_size_to_bytes(limit_gb, "GB"),
            "allocated_bytes": 0,
            "active": True,
            "login_token": secrets.token_urlsafe(16),
            "created_at": datetime.now().isoformat(),
            "sub_id": sub_id,
        }
    asyncio.create_task(save_state())
    log_activity("system", f"نماینده «{name}» با {limit_gb}GB ساخته شد", "ok")
    return {"ok": True, "id": rid, "name": name, "limit_gb": limit_gb, "sub_id": sub_id}

@app.patch("/api/resellers/{rid}")
async def update_reseller(rid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404, "نماینده یافت نشد")
        r = RESELLERS[rid]
        if "name" in body and str(body["name"]).strip():
            r["name"] = str(body["name"]).strip()
        if "active" in body:
            r["active"] = bool(body["active"])
            log_activity("system", f"نماینده «{r['name']}» {'فعال' if r['active'] else 'غیرفعال'} شد", "info")
        if "limit_gb" in body:
            new_total = parse_size_to_bytes(float(body["limit_gb"]), "GB")
            async with LINKS_LOCK:
                used = sum(l.get("limit_bytes", 0) for l in LINKS.values() if l.get("creator_id") == rid)
            if new_total < used:
                raise HTTPException(400, f"نمی‌توان حجم را کمتر از مصرف ({fmt_bytes(used)}) تنظیم کرد")
            r["total_bytes"] = new_total
            log_activity("system", f"حجم نماینده «{r['name']}» به {body['limit_gb']}GB تغییر کرد", "info")
        if "password" in body and str(body["password"]).strip():
            r["password_hash"] = hash_password(str(body["password"]).strip())
            log_activity("system", f"رمز نماینده «{r['name']}» تغییر کرد", "info")
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/resellers/{rid}")
async def delete_reseller(rid: str, _=Depends(require_auth)):
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404)
        del RESELLERS[rid]
    asyncio.create_task(save_state())
    log_activity("system", f"نماینده {rid[:8]}... حذف شد", "warn")
    return {"ok": True, "deleted": rid}

@app.get("/api/resellers/{rid}/links")
async def reseller_links(rid: str, _=Depends(require_auth)):
    async with LINKS_LOCK:
        result = [{"uuid": uid, **d} for uid, d in LINKS.items() if d.get("creator_id") == rid]
    return {"links": result}

# ── Reseller Status Endpoint (جدید) ──────────────────────────────────────────
@app.get("/api/reseller/status")
async def reseller_status(request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "reseller":
        raise HTTPException(403, "forbidden")
    async with RESELLERS_LOCK:
        r = RESELLERS.get(s["user_id"])
        if not r: raise HTTPException(404, "not found")
    async with LINKS_LOCK:
        snap = dict(LINKS)
    allocated = sum(l.get("limit_bytes",0) for l in snap.values() if l.get("creator_id") == s["user_id"])
    traffic = sum(l.get("used_bytes",0) for l in snap.values() if l.get("creator_id") == s["user_id"])
    links_cnt = sum(1 for l in snap.values() if l.get("creator_id") == s["user_id"])
    total = r.get("total_bytes", 0)
    return {
        "ok": True, "name": r["name"],
        "total_bytes": total, "total_fmt": fmt_bytes(total),
        "allocated_bytes": allocated, "allocated_fmt": fmt_bytes(allocated),
        "remaining_bytes": max(0, total-allocated), "remaining_fmt": fmt_bytes(max(0, total-allocated)),
        "traffic_used": traffic, "traffic_fmt": fmt_bytes(traffic),
        "links_count": links_cnt, "sub_id": r.get("sub_id"),
    }

# ── Reseller Token Login ──────────────────────────────────────────────────────
@app.get("/r/{login_token}")
async def reseller_token_login(login_token: str):
    async with RESELLERS_LOCK:
        for rid, res in RESELLERS.items():
            if res.get("login_token") == login_token and res.get("active", True):
                token = await create_session("reseller", rid)
                log_activity("auth", f"ورود {res['name']} با لینک اختصاصی", "ok")
                resp = RedirectResponse(url="/dashboard")
                resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="lax", path="/")
                return resp
    return HTMLResponse("<h2 style='padding:40px;font-family:sans-serif'>لینک نامعتبر است</h2>", status_code=404)

# ── VLESS Relay ───────────────────────────────────────────────────────────────
from relay_vless import RELAY_BUF, parse_vless_header, check_and_use, relay_ws_to_tcp, relay_tcp_to_ws, websocket_tunnel
app.add_api_websocket_route("/ws/{uuid}", websocket_tunnel)

# ── XHTTP ─────────────────────────────────────────────────────────────────────
from xhttp_siz10 import router as xhttp_router
app.include_router(xhttp_router)

# ── HTTP Proxy ────────────────────────────────────────────────────────────────
_HOP = {"connection","keep-alive","proxy-authenticate","proxy-authorization","te","trailers","transfer-encoding","upgrade","content-encoding","content-length"}
@app.api_route("/proxy/{target_url:path}", methods=["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"])
async def http_proxy(target_url: str, request: Request):
    if not target_url.startswith("http"): target_url = "https://" + target_url
    try:
        body = await request.body()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in _HOP and k.lower() != "host"}
        resp = await http_client.request(method=request.method, url=target_url, headers=headers, content=body)
        stats["total_bytes"] += len(resp.content)
        stats["total_requests"] += 1
        hourly_traffic[now_ir().strftime("%H:00")] += len(resp.content)
        return Response(content=resp.content, status_code=resp.status_code,
            headers={k: v for k, v in resp.headers.items() if k.lower() not in _HOP})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "url": target_url, "time": datetime.now().isoformat()})
        raise HTTPException(status_code=502, detail=f"Proxy error: {exc}")

# ── Public Sub Page ───────────────────────────────────────────────────────────
@app.get("/p/{uuid_key}", response_class=HTMLResponse)
async def public_sub_page(uuid_key: str, request: Request):
    from public_page import get_public_page_html
    async with SUBS_LOCK:
        sub = next(({"sub_id": sid, **s} for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
        if not sub: return HTMLResponse("<h2 style='font-family:sans-serif;padding:40px'>گروه پیدا نشد</h2>", status_code=404)
    return HTMLResponse(content=get_public_page_html(uuid_key))

from pages import LOGIN_HTML, DASHBOARD_HTML

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    s = await get_session_data(request.cookies.get(SESSION_COOKIE))
    if s and s["role"] == "admin": return RedirectResponse(url="/dashboard")
    return HTMLResponse(content=LOGIN_HTML)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    s = await get_session_data(request.cookies.get(SESSION_COOKIE))
    if not s: return RedirectResponse(url="/login")
    await ensure_default_link()
    if s["role"] == "reseller":
        return HTMLResponse(content=DASHBOARD_HTML + """<script>
document.body.classList.add('role-reseller');
setTimeout(()=>loadResellerStatus(),1000);
</script>
<style>
body.role-reseller .nav-it[data-pg="resellers"],
body.role-reseller .nav-it[data-pg="ipsettings"],
body.role-reseller .nav-it[data-pg="subscriptions"],
body.role-reseller .nav-it[data-pg="settings"],
body.role-reseller [class*="expire"],
body.role-reseller [class*="ip-input"],
body.role-reseller [class*="port-input"],
body.role-reseller #link-exp-days,
body.role-reseller #link-expires,
body.role-reseller #link-ips,
body.role-reseller #link-port{display:none!important}
</style>""")
    return HTMLResponse(content=DASHBOARD_HTML)

# ── API های فرعی public (همونی که قبلاً بود) ──────────────────────────────────
@app.get("/api/public/sub/{uuid_key}")
async def public_sub_data(uuid_key: str, request: Request):
    async with SUBS_LOCK:
        sub_entry = next(((sid, s) for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
        if not sub_entry: raise HTTPException(status_code=404, detail="not found")
        sub_id, sub = sub_entry
        if sub.get("password_hash"):
            if hash_password(request.query_params.get("pw", "")) != sub["password_hash"]:
                return JSONResponse({"locked": True, "name": sub["name"]})
    host = get_host()
    link_ids = sub.get("link_ids", [])
    async with LINKS_LOCK:
        snap = dict(LINKS)
        links_out = []
        for lid in link_ids:
            link = snap.get(lid)
            if not link: continue
            active_conns = sum(1 for c in connections.values() if c.get("uuid") == lid)
            links_out.append({"uuid": lid, "label": link["label"], "active": is_link_allowed(link),
                "protocol": link.get("protocol", DEFAULT_PROTOCOL), "used_bytes": link.get("used_bytes", 0),
                "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
                "limit_bytes": link.get("limit_bytes", 0),
                "limit_fmt": "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
                "expires_at": link.get("expires_at"),
                "vless_link": "\n".join(generate_vless_links(link, lid, host)),
                "sub_url": f"https://{host}/sub/{lid}", "connections": active_conns})
        total_used = sum(l["used_bytes"] for l in links_out)
        return {"locked": False, "name": sub["name"], "desc": sub.get("desc", ""),
            "sub_url": f"https://{host}/sub-group/{uuid_key}",
            "active_connections": sum(l["connections"] for l in links_out),
            "total_used_fmt": fmt_bytes(total_used), "links": links_out}

@app.get("/api/public/sub-single/{uuid}")
async def public_single_sub_data(uuid: str):
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
        if not link: raise HTTPException(status_code=404, detail="not found")
        host = get_host()
        active_conns = sum(1 for c in connections.values() if c.get("uuid") == uuid)
        vless_list = generate_vless_links(link, uuid, host)
        return {
            "name": link["label"], "desc": link.get("note", ""),
            "total_used_fmt": fmt_bytes(link.get("used_bytes", 0)),
            "active_connections": active_conns,
            "links": [{"uuid": uuid, "label": link["label"],
                "active": is_link_allowed(link),
                "protocol": link.get("protocol", DEFAULT_PROTOCOL),
                "used_bytes": link.get("used_bytes", 0),
                "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
                "limit_bytes": link.get("limit_bytes", 0),
                "limit_fmt": "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
                "vless_link": "\n".join(vless_list),
                "sub_url": None}]
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
@app.get("/health")
async def health():
    return {"status": "ok", "connections": len(connections), "uptime": uptime()}

@app.get("/sub/{uuid}")
async def subscription_single(uuid: str, request: Request):
    import base64
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
        if not link or not is_link_allowed(link):
            raise HTTPException(status_code=404, detail="not found or inactive")
    ua = request.headers.get("user-agent", "").lower()
    if any(b in ua for b in ["mozilla", "chrome", "safari", "firefox", "edge", "opera"]):
        import importlib.util
        spec = importlib.util.spec_from_file_location("pub", "public_page.py")
        pub = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pub)
        return HTMLResponse(content=pub.get_single_sub_page_html(uuid))
    host = get_host()
    lines = generate_vless_links(link, uuid, host)
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain",
        headers={"profile-title": quote(link["label"]), "support-url": "https://t.me/VaslZone"})

@app.get("/sub-all")
async def subscription_all(_=Depends(require_auth)):
    import base64
    host = get_host()
    lines = []
    async with LINKS_LOCK:
        for uid, d in LINKS.items():
            if is_link_allowed(d):
                lines.extend(generate_vless_links(d, uid, host))
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")

@app.get("/sub-group/{uuid_key}")
async def sub_group_subscription(uuid_key: str, request: Request):
    import base64
    async with SUBS_LOCK:
        sub = next((s for s in SUBS.values() if s.get("uuid_key") == uuid_key), None)
        if not sub: raise HTTPException(status_code=404, detail="not found")
        if sub.get("password_hash"):
            if hash_password(request.query_params.get("pw", "")) != sub["password_hash"]:
                raise HTTPException(status_code=403, detail="wrong password")
    ua = request.headers.get("user-agent", "").lower()
    if any(b in ua for b in ["mozilla", "chrome", "safari", "firefox", "edge", "opera"]):
        from public_page import get_public_page_html, get_single_sub_page_html
        return HTMLResponse(content=get_public_page_html(uuid_key))
    host = get_host()
    link_ids = sub.get("link_ids", [])
    lines = []
    async with LINKS_LOCK:
        for lid in link_ids:
            link = LINKS.get(lid)
            if link and is_link_allowed(link):
                lines.extend(generate_vless_links(link, lid, host))
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain",
        headers={"profile-title": quote(sub["name"]), "support-url": "https://t.me/VaslZone", "profile-update-interval": "12"})

@app.post("/api/subs")
async def create_sub(request: Request, _=Depends(require_auth)):
    body = await request.json()
    name = (body.get("name") or "گروه جدید").strip()[:60]
    desc = (body.get("desc") or "").strip()[:200]
    password = (body.get("password") or "").strip()
    sub_id = generate_uuid()
    uuid_key = secrets.token_urlsafe(16)
    async with SUBS_LOCK:
        SUBS[sub_id] = {"name": name, "desc": desc,
            "password_hash": hash_password(password) if password else None,
            "uuid_key": uuid_key, "created_at": datetime.now().isoformat(), "link_ids": []}
    asyncio.create_task(save_state())
    log_activity("sub", f"گروه «{name}» ساخته شد", "ok")
    host = get_host()
    return {"sub_id": sub_id, **SUBS[sub_id],
        "public_url": f"https://{host}/p/{uuid_key}", "sub_url": f"https://{host}/sub-group/{uuid_key}"}

@app.get("/api/subs")
async def list_subs(_=Depends(require_auth)):
    host = get_host()
    async with SUBS_LOCK: snap_subs = dict(SUBS)
    async with LINKS_LOCK: snap_links = dict(LINKS)
    result = []
    for sid, s in snap_subs.items():
        link_ids = s.get("link_ids", [])
        active_count = sum(1 for lid in link_ids if is_link_allowed(snap_links.get(lid)))
        total_used = sum(snap_links[lid].get("used_bytes", 0) for lid in link_ids if lid in snap_links)
        result.append({"sub_id": sid, **s, "password_hash": None,
            "has_password": s.get("password_hash") is not None,
            "links_count": len(link_ids), "active_count": active_count,
            "total_used_bytes": total_used, "total_used_fmt": fmt_bytes(total_used),
            "public_url": f"https://{host}/p/{s['uuid_key']}",
            "sub_url": f"https://{host}/sub-group/{s['uuid_key']}"})
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"subs": result}

@app.patch("/api/subs/{sub_id}")
async def update_sub(sub_id: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with SUBS_LOCK:
        if sub_id not in SUBS: raise HTTPException(status_code=404, detail="sub not found")
        s = SUBS[sub_id]
        if "name" in body: s["name"] = str(body["name"])[:60]
        if "desc" in body: s["desc"] = str(body["desc"])[:200]
        if "password" in body:
            pw = str(body["password"]).strip()
            s["password_hash"] = hash_password(pw) if pw else None
        if "link_ids" in body: s["link_ids"] = list(body["link_ids"])
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/subs/{sub_id}")
async def delete_sub(sub_id: str, _=Depends(require_auth)):
    async with SUBS_LOCK:
        if sub_id not in SUBS: raise HTTPException(status_code=404, detail="sub not found")
        name = SUBS[sub_id].get("name", sub_id)
        del SUBS[sub_id]
    async with LINKS_LOCK:
        for link in LINKS.values():
            if link.get("sub_id") == sub_id: link["sub_id"] = None
    asyncio.create_task(save_state())
    log_activity("sub", f"گروه «{name}» حذف شد", "warn")
    return {"ok": True, "deleted": sub_id}

@app.post("/api/subs/{sub_id}/links")
async def assign_link_to_sub(sub_id: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    link_id = str(body.get("link_id", ""))
    action = str(body.get("action", "add"))
    async with SUBS_LOCK:
        if sub_id not in SUBS: raise HTTPException(status_code=404, detail="sub not found")
        s = SUBS[sub_id]
        ids = s.setdefault("link_ids", [])
        if action == "add":
            if link_id not in ids: ids.append(link_id)
        else:
            if link_id in ids: ids.remove(link_id)
    async with LINKS_LOCK:
        if link_id in LINKS: LINKS[link_id]["sub_id"] = sub_id if action == "add" else None
    asyncio.create_task(save_state())
    return {"ok": True}

@app.post("/api/login")
async def api_login(request: Request):
    body = await request.json()
    ip = client_ip(request)
    pw = str(body.get("password", ""))
    if hash_password(pw) == AUTH["password_hash"]:
        token = await create_session("admin", "admin")
        log_activity("auth", f"ورود ادمین از {ip}", "ok")
        resp = JSONResponse({"ok": True, "role": "admin"})
        resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="lax", path="/")
        return resp
    async with RESELLERS_LOCK:
        for rid, res in RESELLERS.items():
            if res.get("active", True) and res.get("password_hash") == hash_password(pw):
                token = await create_session("reseller", rid)
                log_activity("auth", f"ورود نماینده {res['name']} از {ip}", "ok")
                resp = JSONResponse({"ok": True, "role": "reseller"})
                resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="lax", path="/")
                return resp
    log_activity("auth", f"تلاش ورود ناموفق از {ip}", "err")
    raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")

@app.post("/api/logout")
async def api_logout(request: Request):
    await destroy_session(request.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(SESSION_COOKIE, path="/")
    return resp

@app.get("/api/me")
async def api_me(request: Request):
    s = await get_session_data(request.cookies.get(SESSION_COOKIE))
    return {"authenticated": bool(s), "role": s["role"] if s else None}

@app.post("/api/change-password")
async def api_change_password(request: Request, token=Depends(require_auth)):
    body = await request.json()
    if hash_password(str(body.get("current_password", ""))) != AUTH["password_hash"]:
        raise HTTPException(status_code=400, detail="رمز فعلی اشتباه است")
    new = str(body.get("new_password", ""))
    if len(new) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    AUTH["password_hash"] = hash_password(new)
    await destroy_session(token)
    await save_state()
    log_activity("auth", "رمز عبور پنل تغییر کرد", "ok")
    return {"ok": True}

@app.get("/api/settings/global-ips")
async def get_global_ips(_=Depends(require_auth)):
    return GLOBAL_SETTINGS

@app.post("/api/settings/global-ips")
async def update_global_ips(request: Request, _=Depends(require_auth)):
    body = await request.json()
    GLOBAL_SETTINGS["ips"] = [ip.strip() for ip in body.get("ips", []) if ip.strip()]
    GLOBAL_SETTINGS["port"] = int(body.get("port")) if body.get("port") else None
    asyncio.create_task(save_state())
    log_activity("system", "تنظیمات IP/پورت سراسری بروزرسانی شد", "info")
    return {"ok": True, "settings": dict(GLOBAL_SETTINGS)}

@app.get("/stats")
async def get_stats(_=Depends(require_auth)):
    async with LINKS_LOCK: snap = dict(LINKS)
    return {"active_connections": len(connections),
        "total_traffic_mb": round(stats["total_bytes"] / (1024 ** 2), 2),
        "total_requests": stats["total_requests"], "total_errors": stats["total_errors"],
        "uptime": uptime(), "timestamp": datetime.now().isoformat(),
        "hourly": dict(hourly_traffic), "recent_errors": list(error_logs)[-10:],
        "links_count": len(snap), "active_links": sum(1 for l in snap.values() if is_link_allowed(l)),
        "expired_links": sum(1 for l in snap.values() if is_link_expired(l)),
        "subs_count": len(SUBS), "resellers_count": len(RESELLERS)}

@app.get("/api/activity")
async def get_activity(_=Depends(require_auth)):
    return {"logs": list(activity_logs)[-150:]}

@app.get("/api/connections")
async def get_connections(_=Depends(require_auth)):
    async with LINKS_LOCK: snap = dict(LINKS)
    grouped: dict[str, dict] = {}
    for conn_id, c in connections.items():
        ip = c.get("ip", "نامشخص")
        link = snap.get(c.get("uuid"))
        label = link.get("label") if link else "نامشخص"
        g = grouped.get(ip)
        if g is None:
            g = {"ip": ip, "sessions": 0, "bytes": 0, "labels": set(), "transports": set(),
                 "first_connected_at": c.get("connected_at"), "last_connected_at": c.get("connected_at")}
            grouped[ip] = g
        g["sessions"] += 1
        g["bytes"] += c.get("bytes", 0)
        g["labels"].add(label)
        g["transports"].add(c.get("transport", "vless-ws"))
        ca = c.get("connected_at")
        if ca:
            if not g["first_connected_at"] or ca < g["first_connected_at"]: g["first_connected_at"] = ca
            if not g["last_connected_at"] or ca > g["last_connected_at"]: g["last_connected_at"] = ca
    result = [{"ip": k, "sessions": v["sessions"], "labels": sorted(v["labels"]),
        "label": " · ".join(sorted(v["labels"])) if v["labels"] else "نامشخص",
        "transports": sorted(v["transports"]), "bytes": v["bytes"],
        "bytes_fmt": fmt_bytes(v["bytes"]),
        "connected_at": v["first_connected_at"],
        "last_connected_at": v["last_connected_at"]} for k, v in grouped.items()]
    result.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)
    return {"connections": result, "count": len(result), "raw_count": len(connections)}
@app.post("/api/links")
async def create_link(request: Request):
    s = await require_reseller_auth(request)
    body = await request.json()
    label = (body.get("label") or "لینک جدید").strip()[:60]
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    note = (body.get("note") or "").strip()[:200]
    ips = [ip.strip() for ip in body.get("ips", []) if ip.strip()]
    port = int(body.get("port")) if body.get("port") else None
    is_personal = bool(body.get("is_personal", False))
    sub_id = body.get("sub_id")
    protocol = body.get("protocol") or DEFAULT_PROTOCOL
    if protocol not in PROTOCOLS: protocol = DEFAULT_PROTOCOL

    if s["role"] == "reseller":
        async with RESELLERS_LOCK:
            my_res = RESELLERS.get(s["user_id"])
            if not my_res or not my_res.get("active", True):
                raise HTTPException(status_code=403, detail="اکانت نماینده غیرفعال است")
            sub_id = my_res.get("sub_id")
            if not sub_id: raise HTTPException(500, "ساب نماینده نیست")
        await check_reseller_capacity(s["user_id"], limit_bytes)
        is_personal = True
        ips = []
        port = None
        exp_days = 0
        expires_at = None

    flag = ""
    if ips: flag = await fetch_ip_flag(ips[0])
    if flag: label = f"{label} {flag}"

    uid = generate_uuid()
    async with LINKS_LOCK:
        if s["role"] == "reseller":
            async with RESELLERS_LOCK:
                my_res = RESELLERS.get(s["user_id"])
                total = my_res.get("total_bytes", 0) if my_res else 0
            allocated = 0
            for d in LINKS.values():
                if d.get("creator_id") == s["user_id"]:
                    allocated += d.get("limit_bytes", 0)
            if allocated + limit_bytes > total:
                raise HTTPException(400, "حجم مجاز شما به پایان رسیده است.")
        LINKS[uid] = {"label": label, "limit_bytes": limit_bytes, "used_bytes": 0,
            "created_at": datetime.now().isoformat(), "active": True,
            "expires_at": expires_at, "note": note, "is_default": False,
            "sub_id": sub_id, "protocol": protocol, "ips": ips, "port": port,
            "is_personal": is_personal, "creator_id": s["user_id"]}
        if sub_id:
            async with SUBS_LOCK:
                if sub_id in SUBS:
                    ids = SUBS[sub_id].setdefault("link_ids", [])
                    if uid not in ids: ids.append(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{label}» توسط {s['user_id']} ساخته شد", "ok")
    host = get_host()
    vless_list = generate_vless_links(LINKS[uid], uid, host)
    return {"uuid": uid, **LINKS[uid], "vless_link": "\n".join(vless_list),
            "sub_url": f"https://{host}/sub/{uid}"}

@app.post("/api/links/bulk")
async def create_links_bulk(request: Request):
    s = await require_reseller_auth(request)
    body = await request.json()
    count = min(int(body.get("count", 1)), 100)
    if count < 1: count = 1
    base_label = (body.get("label") or "Bulk").strip()[:40]
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    ips = [ip.strip() for ip in body.get("ips", []) if ip.strip()]
    port = int(body.get("port")) if body.get("port") else None
    is_personal = bool(body.get("is_personal", False))
    sub_id = body.get("sub_id")
    protocol = body.get("protocol") or DEFAULT_PROTOCOL
    if protocol not in PROTOCOLS: protocol = DEFAULT_PROTOCOL

    if s["role"] == "reseller":
        async with RESELLERS_LOCK:
            my_res = RESELLERS.get(s["user_id"])
            if not my_res or not my_res.get("active", True):
                raise HTTPException(status_code=403, detail="اکانت نماینده غیرفعال است")
            sub_id = my_res.get("sub_id")
            if not sub_id: raise HTTPException(500, "ساب نماینده نیست")
        await check_reseller_capacity(s["user_id"], limit_bytes * count)
        is_personal = True
        ips = []
        port = None
        exp_days = 0
        expires_at = None

    created_uids = []
    host = get_host()
    async with LINKS_LOCK:
        if s["role"] == "reseller":
            async with RESELLERS_LOCK:
                my_res = RESELLERS.get(s["user_id"])
                total = my_res.get("total_bytes", 0) if my_res else 0
            allocated = 0
            for d in LINKS.values():
                if d.get("creator_id") == s["user_id"]:
                    allocated += d.get("limit_bytes", 0)
            if allocated + limit_bytes * count > total:
                raise HTTPException(400, "حجم مجاز شما به پایان رسیده است.")
        for i in range(count):
            target_ip = ips[i % len(ips)] if ips else ""
            flag = await fetch_ip_flag(target_ip) if target_ip else ""
            label = f"{base_label}-{i+1}" + (f" {flag}" if flag else "")
            uid = generate_uuid()
            LINKS[uid] = {"label": label, "limit_bytes": limit_bytes, "used_bytes": 0,
                "created_at": datetime.now().isoformat(), "active": True,
                "expires_at": expires_at, "note": "", "is_default": False,
                "sub_id": sub_id, "protocol": protocol,
                "ips": [target_ip] if target_ip else [],
                "port": port, "is_personal": is_personal, "creator_id": s["user_id"]}
            if sub_id:
                async with SUBS_LOCK:
                    if sub_id in SUBS:
                        ids = SUBS[sub_id].setdefault("link_ids", [])
                        if uid not in ids: ids.append(uid)
            created_uids.append(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"{count} کانفیگ {base_label} ساخته شد", "ok")
    all_vless = []
    for uid in created_uids:
        all_vless.extend(generate_vless_links(LINKS[uid], uid, host))
    sub_url = ""
    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                uuid_key = SUBS[sub_id].get("uuid_key", "")
                if uuid_key: sub_url = f"https://{host}/sub-group/{uuid_key}"
    return {"ok": True, "count": count, "created_uids": created_uids,
            "sub_url": sub_url, "vless_bulk": "\n".join(all_vless)}

@app.get("/api/links")
async def list_links(request: Request):
    s = await require_reseller_auth(request)
    host = get_host()
    async with LINKS_LOCK:
        result = []
        for uid, d in LINKS.items():
            if s["role"] == "reseller" and d.get("creator_id") != s["user_id"]: continue
            vless_list = generate_vless_links(d, uid, host)
            result.append({"uuid": uid, **d, "expired": is_link_expired(d),
                "vless_link": "\n".join(vless_list), "sub_url": f"https://{host}/sub/{uid}"})
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.patch("/api/links/{uid}")
async def update_link(uid: str, request: Request):
    s = await require_reseller_auth(request)
    body = await request.json()
    async with LINKS_LOCK:
        if uid not in LINKS: raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        if s["role"] == "reseller" and link.get("creator_id") != s["user_id"]:
            raise HTTPException(status_code=403, detail="forbidden")
        if "active" in body: link["active"] = bool(body["active"])
        if "label" in body: link["label"] = str(body["label"])[:60]
        if "note" in body: link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]: link["used_bytes"] = 0
        if "limit_value" in body:
            lv = float(body.get("limit_value") or 0)
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, body.get("limit_unit") or "GB")
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            link["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
        if "ips" in body: link["ips"] = [ip.strip() for ip in body.get("ips", []) if ip.strip()]
        if "port" in body: link["port"] = int(body["port"]) if body.get("port") else None
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/links/{uid}")
async def delete_link(uid: str, request: Request):
    s = await require_reseller_auth(request)
    async with LINKS_LOCK:
        if uid not in LINKS: raise HTTPException(status_code=404, detail="not found")
        if s["role"] == "reseller" and LINKS[uid].get("creator_id") != s["user_id"]:
            raise HTTPException(status_code=403, detail="forbidden")
        sub_id = LINKS[uid].get("sub_id")
        del LINKS[uid]
        if sub_id:
            async with SUBS_LOCK:
                if sub_id in SUBS:
                    ids = SUBS[sub_id].get("link_ids", [])
                    if uid in ids: ids.remove(uid)
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ {uid[:8]}... حذف شد", "err")
    return {"ok": True, "deleted": uid}

@app.post("/api/resellers/{rid}/reset-token")
async def reset_reseller_token(rid: str, _=Depends(require_auth)):
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404, "not found")
        RESELLERS[rid]["login_token"] = secrets.token_urlsafe(16)
    asyncio.create_task(save_state())
    return {"ok": True, "login_token": RESELLERS[rid]["login_token"]}

@app.get("/api/resellers")
async def list_resellers(_=Depends(require_auth)):
    host = get_host()
    async with RESELLERS_LOCK: snap_r = dict(RESELLERS)
    async with LINKS_LOCK: snap_l = dict(LINKS)
    result = []
    for rid, r in snap_r.items():
        links_cnt = sum(1 for l in snap_l.values() if l.get("creator_id") == rid)
        allocated = sum(l.get("limit_bytes", 0) for l in snap_l.values() if l.get("creator_id") == rid)
        traffic = sum(l.get("used_bytes", 0) for l in snap_l.values() if l.get("creator_id") == rid)
        result.append({"id": rid, "name": r["name"], "active": r.get("active", True),
            "total_bytes": r.get("total_bytes", 0), "total_fmt": fmt_bytes(r.get("total_bytes", 0)),
            "allocated_bytes": allocated, "allocated_fmt": fmt_bytes(allocated),
            "traffic_used": traffic, "traffic_fmt": fmt_bytes(traffic),
            "remaining_bytes": max(0, r.get("total_bytes", 0) - allocated),
            "remaining_fmt": fmt_bytes(max(0, r.get("total_bytes", 0) - allocated)),
            "created_at": r.get("created_at"), "links_count": links_cnt,
            "login_link": f"https://{host}/r/{r.get('login_token', '')}"})
    return {"resellers": result}
@app.post("/api/resellers")
async def create_reseller(request: Request, _=Depends(require_auth)):
    body = await request.json()
    name = str(body.get("name", "")).strip()
    pw = str(body.get("password", "")).strip()
    limit_gb = float(body.get("limit_gb") or 0)
    if not name or not pw: raise HTTPException(400, "نام و رمز عبور الزامی است")
    if limit_gb <= 0: raise HTTPException(400, "حجم باید بیشتر از ۰ باشد")
    rid = secrets.token_hex(8)
    sub_id = f"reseller_{rid}"
    async with SUBS_LOCK:
        SUBS[sub_id] = {"name": f"گروه {name}", "is_personal": True,
            "link_ids": [], "created_at": datetime.now().isoformat(), "creator_id": rid}
    async with RESELLERS_LOCK:
        RESELLERS[rid] = {"name": name, "password_hash": hash_password(pw),
            "total_bytes": parse_size_to_bytes(limit_gb, "GB"),
            "allocated_bytes": 0, "active": True,
            "login_token": secrets.token_urlsafe(16),
            "created_at": datetime.now().isoformat(), "sub_id": sub_id}
    asyncio.create_task(save_state())
    log_activity("system", f"نماینده «{name}» با {limit_gb}GB ساخته شد", "ok")
    return {"ok": True, "id": rid, "name": name, "limit_gb": limit_gb, "sub_id": sub_id}

@app.patch("/api/resellers/{rid}")
async def update_reseller(rid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    new_total = None
    if "limit_gb" in body:
        new_total = parse_size_to_bytes(float(body["limit_gb"]), "GB")
        async with LINKS_LOCK:
            used = sum(l.get("limit_bytes", 0) for l in LINKS.values() if l.get("creator_id") == rid)
        if new_total < used:
            raise HTTPException(400, f"نمی‌توان حجم را کمتر از مصرف ({fmt_bytes(used)}) تنظیم کرد")
    async with RESELLERS_LOCK:
        if rid not in RESELLERS:
            raise HTTPException(404, "نماینده یافت نشد")
        r = RESELLERS[rid]
        if "name" in body and str(body["name"]).strip():
            r["name"] = str(body["name"]).strip()
        if "active" in body:
            r["active"] = bool(body["active"])
            log_activity("system", f"نماینده «{r['name']}» {'فعال' if r['active'] else 'غیرفعال'} شد", "info")
        if new_total is not None:
            r["total_bytes"] = new_total
            log_activity("system", f"حجم نماینده «{r['name']}» به {body['limit_gb']}GB تغییر کرد", "info")
        if "password" in body and str(body["password"]).strip():
            r["password_hash"] = hash_password(str(body["password"]).strip())
            log_activity("system", f"رمز نماینده «{r['name']}» تغییر کرد", "info")
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/resellers/{rid}")
async def delete_reseller(rid: str, _=Depends(require_auth)):
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404)
        del RESELLERS[rid]
    asyncio.create_task(save_state())
    log_activity("system", f"نماینده {rid[:8]}... حذف شد", "warn")
    return {"ok": True, "deleted": rid}

@app.get("/api/resellers/{rid}/links")
async def reseller_links(rid: str, _=Depends(require_auth)):
    async with LINKS_LOCK:
        result = [{"uuid": uid, **d} for uid, d in LINKS.items() if d.get("creator_id") == rid]
    return {"links": result}

@app.get("/api/reseller/status")
async def reseller_status(request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "reseller":
        raise HTTPException(403, "forbidden")
    async with RESELLERS_LOCK:
        r = RESELLERS.get(s["user_id"])
        if not r: raise HTTPException(404, "not found")
    async with LINKS_LOCK:
        snap = dict(LINKS)
    allocated = sum(l.get("limit_bytes",0) for l in snap.values() if l.get("creator_id")==s["user_id"])
    traffic = sum(l.get("used_bytes",0) for l in snap.values() if l.get("creator_id")==s["user_id"])
    links_cnt = sum(1 for l in snap.values() if l.get("creator_id")==s["user_id"])
    total = r.get("total_bytes", 0)
    return {"ok": True, "name": r["name"], "total_bytes": total, "total_fmt": fmt_bytes(total),
        "allocated_bytes": allocated, "allocated_fmt": fmt_bytes(allocated),
        "remaining_bytes": max(0, total-allocated), "remaining_fmt": fmt_bytes(max(0, total-allocated)),
        "traffic_used": traffic, "traffic_fmt": fmt_bytes(traffic),
        "links_count": links_cnt, "sub_id": r.get("sub_id")}

@app.get("/r/{login_token}")
async def reseller_token_login(login_token: str):
    async with RESELLERS_LOCK:
        for rid, res in RESELLERS.items():
            if res.get("login_token") == login_token and res.get("active", True):
                token = await create_session("reseller", rid)
                log_activity("auth", f"ورود {res['name']} با لینک اختصاصی", "ok")
                resp = RedirectResponse(url="/dashboard")
                resp.set_cookie(SESSION_COOKIE, token, max_age=SESSION_TTL, httponly=True, samesite="lax", path="/")
                return resp
    return HTMLResponse("<h2 style='padding:40px;font-family:sans-serif'>لینک نامعتبر است</h2>", status_code=404)

from relay_vless import parse_vless_header, check_and_use, relay_ws_to_tcp, relay_tcp_to_ws, websocket_tunnel
app.add_api_websocket_route("/ws/{uuid}", websocket_tunnel)

from xhttp_siz10 import router as xhttp_router
app.include_router(xhttp_router)

_HOP = {"connection","keep-alive","proxy-authenticate","proxy-authorization","te","trailers","transfer-encoding","upgrade","content-encoding","content-length"}
@app.api_route("/proxy/{target_url:path}", methods=["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"])
async def http_proxy(target_url: str, request: Request):
    if not target_url.startswith("http"): target_url = "https://" + target_url
    try:
        body = await request.body()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in _HOP and k.lower() != "host"}
        resp = await http_client.request(method=request.method, url=target_url, headers=headers, content=body)
        stats["total_bytes"] += len(resp.content)
        stats["total_requests"] += 1
        hourly_traffic[now_ir().strftime("%H:00")] += len(resp.content)
        return Response(content=resp.content, status_code=resp.status_code,
            headers={k: v for k, v in resp.headers.items() if k.lower() not in _HOP})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "url": target_url, "time": datetime.now().isoformat()})
        raise HTTPException(status_code=502, detail=f"Proxy error: {exc}")

@app.get("/p/{uuid_key}", response_class=HTMLResponse)
async def public_sub_page(uuid_key: str, request: Request):
    from public_page import get_public_page_html
    async with SUBS_LOCK:
        sub = next(({"sub_id": sid, **s} for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
        if not sub: return HTMLResponse("<h2 style='font-family:sans-serif;padding:40px'>گروه پیدا نشد</h2>", status_code=404)
    return HTMLResponse(content=get_public_page_html(uuid_key))

from pages import LOGIN_HTML, DASHBOARD_HTML

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    s = await get_session_data(request.cookies.get(SESSION_COOKIE))
    if s and s["role"] == "admin": return RedirectResponse(url="/dashboard")
    return HTMLResponse(content=LOGIN_HTML)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    s = await get_session_data(request.cookies.get(SESSION_COOKIE))
    if not s: return RedirectResponse(url="/login")
    await ensure_default_link()
    if s["role"] == "reseller":
        seller_css = "<style>body.role-reseller .nav-it[data-pg=\"resellers\"],body.role-reseller .nav-it[data-pg=\"ipsettings\"],body.role-reseller .nav-it[data-pg=\"subscriptions\"],body.role-reseller .nav-it[data-pg=\"settings\"],body.role-reseller .ico-admin,body.role-reseller [data-admin=\"1\"],body.role-reseller #link-exp-days,body.role-reseller #link-expires,body.role-reseller #link-ips,body.role-reseller #link-port,body.role-reseller #link-sub{display:none!important}</style>"
        seller_js = "<script>document.body.classList.add('role-reseller');if(typeof loadResellerStatus==='function')setTimeout(()=>loadResellerStatus(),800);</script>"
        return HTMLResponse(content=DASHBOARD_HTML + seller_css + seller_js)
    return HTMLResponse(content=DASHBOARD_HTML)

@app.get("/api/public/sub/{uuid_key}")
async def public_sub_data(uuid_key: str, request: Request):
    async with SUBS_LOCK:
        sub_entry = next(((sid, s) for sid, s in SUBS.items() if s.get("uuid_key") == uuid_key), None)
        if not sub_entry: raise HTTPException(status_code=404, detail="not found")
        sub_id, sub = sub_entry
        if sub.get("password_hash"):
            if hash_password(request.query_params.get("pw", "")) != sub["password_hash"]:
                return JSONResponse({"locked": True, "name": sub["name"]})
    host = get_host()
    link_ids = sub.get("link_ids", [])
    async with LINKS_LOCK:
        snap = dict(LINKS)
        links_out = []
        for lid in link_ids:
            link = snap.get(lid)
            if not link: continue
            active_conns = sum(1 for c in connections.values() if c.get("uuid") == lid)
            links_out.append({"uuid": lid, "label": link["label"], "active": is_link_allowed(link),
                "protocol": link.get("protocol", DEFAULT_PROTOCOL),
                "used_bytes": link.get("used_bytes", 0),
                "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
                "limit_bytes": link.get("limit_bytes", 0),
                "limit_fmt": "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
                "expires_at": link.get("expires_at"),
                "vless_link": "\n".join(generate_vless_links(link, lid, host)),
                "sub_url": f"https://{host}/sub/{lid}", "connections": active_conns})
        total_used = sum(l["used_bytes"] for l in links_out)
        return {"locked": False, "name": sub["name"], "desc": sub.get("desc", ""),
            "sub_url": f"https://{host}/sub-group/{uuid_key}",
            "active_connections": sum(l["connections"] for l in links_out),
            "total_used_fmt": fmt_bytes(total_used), "links": links_out}

@app.get("/api/public/sub-single/{uuid}")
async def public_single_sub_data(uuid: str):
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
        if not link: raise HTTPException(status_code=404, detail="not found")
        host = get_host()
        active_conns = sum(1 for c in connections.values() if c.get("uuid") == uuid)
        vless_list = generate_vless_links(link, uuid, host)
        return {"name": link["label"], "desc": link.get("note", ""),
            "total_used_fmt": fmt_bytes(link.get("used_bytes", 0)),
            "active_connections": active_conns,
            "links": [{"uuid": uuid, "label": link["label"],
                "active": is_link_allowed(link),
                "protocol": link.get("protocol", DEFAULT_PROTOCOL),
                "used_bytes": link.get("used_bytes", 0),
                "used_fmt": fmt_bytes(link.get("used_bytes", 0)),
                "limit_bytes": link.get("limit_bytes", 0),
                "limit_fmt": "∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
                "vless_link": "\n".join(vless_list), "sub_url": None}]}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
