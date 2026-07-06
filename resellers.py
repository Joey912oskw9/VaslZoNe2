# resellers.py
# ── تمام بخش نمایندگان (API + فرانت) ──────────────────────────────────────────
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
import asyncio
import secrets

# Router برای /api/resellers/* و /api/reseller/status
api_router = APIRouter(prefix="/api")

# Router برای /r/{login_token}
token_router = APIRouter()

# ── متغیرهای سراسری (از main پاس می‌شن) ──────────────────────────────────────
RESELLERS = {}; RESELLERS_LOCK = None
SUBS = {}; SUBS_LOCK = None
LINKS = {}; LINKS_LOCK = None
SESSIONS = {}; SESSIONS_LOCK = None
AUTH = {}
hash_password = None; create_session = None; log_activity = None
save_state_callback = None; fmt_bytes = None; parse_size_to_bytes = None
COOKIE_NAME = "rvg_session"
ADMIN_ID = None

def setup(defaults):
    global RESELLERS, RESELLERS_LOCK, SUBS, SUBS_LOCK, LINKS, LINKS_LOCK
    global SESSIONS, SESSIONS_LOCK, AUTH, ADMIN_ID
    global hash_password, create_session, log_activity
    global save_state_callback, fmt_bytes, parse_size_to_bytes, COOKIE_NAME
    RESELLERS = defaults["RESELLERS"]; RESELLERS_LOCK = defaults["RESELLERS_LOCK"]
    SUBS = defaults["SUBS"]; SUBS_LOCK = defaults["SUBS_LOCK"]
    LINKS = defaults["LINKS"]; LINKS_LOCK = defaults["LINKS_LOCK"]
    SESSIONS = defaults["SESSIONS"]; SESSIONS_LOCK = defaults["SESSIONS_LOCK"]
    AUTH = defaults["AUTH"]; ADMIN_ID = defaults.get("ADMIN_ID")
    hash_password = defaults["hash_password"]
    create_session = defaults["create_session"]
    log_activity = defaults["log_activity"]
    save_state_callback = defaults["save_state_callback"]
    fmt_bytes = defaults["fmt_bytes"]
    parse_size_to_bytes = defaults["parse_size_to_bytes"]
    COOKIE_NAME = defaults.get("COOKIE_NAME", "rvg_session")

async def save_state():
    if save_state_callback:
        asyncio.create_task(save_state_callback())

async def require_reseller_auth(request: Request):
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        raise HTTPException(401, "unauthorized")
    async with SESSIONS_LOCK:
        s = SESSIONS.get(token)
        if not s: raise HTTPException(401, "unauthorized")
        if s["exp"] < datetime.now().timestamp():
            SESSIONS.pop(token, None)
            raise HTTPException(401, "unauthorized")
        return s

async def check_reseller_capacity(reseller_id: str, new_limit_bytes: int):
    if new_limit_bytes == 0:
        raise HTTPException(400, "نماینده نمی‌تواند کانفیگ با حجم نامحدود بسازد.")
    async with RESELLERS_LOCK:
        res = RESELLERS.get(reseller_id)
        if not res or not res.get("active", True):
            raise HTTPException(403, "اکانت نماینده غیرفعال است")
        allocated = 0
        async with LINKS_LOCK:
            for d in LINKS.values():
                if d.get("creator_id") == reseller_id:
                    allocated += d.get("limit_bytes", 0)
        if allocated + new_limit_bytes > res.get("total_bytes", 0):
            raise HTTPException(400, "حجم مجاز شما به پایان رسیده است.")

# ── API Endpoints ──────────────────────────────────────────────────────────────
@api_router.post("/resellers/{rid}/reset-token")
async def reset_reseller_token(rid: str, request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "admin":
        raise HTTPException(403, "forbidden")
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404, "not found")
        RESELLERS[rid]["login_token"] = secrets.token_urlsafe(16)
    await save_state()
    return {"ok": True, "login_token": RESELLERS[rid]["login_token"]}

@api_router.get("/resellers")
async def list_resellers(request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "admin": raise HTTPException(403, "forbidden")
    host = request.headers.get("host", "localhost").split(":")[0]
    async with RESELLERS_LOCK: snap_r = dict(RESELLERS)
    async with LINKS_LOCK: snap_l = dict(LINKS)
    result = []
    for rid, r in snap_r.items():
        lc = sum(1 for l in snap_l.values() if l.get("creator_id") == rid)
        al = sum(l.get("limit_bytes",0) for l in snap_l.values() if l.get("creator_id") == rid)
        tr = sum(l.get("used_bytes",0) for l in snap_l.values() if l.get("creator_id") == rid)
        tot = r.get("total_bytes",0)
        result.append({"id":rid,"name":r["name"],"active":r.get("active",True),
            "total_bytes":tot,"total_fmt":fmt_bytes(tot),
            "allocated_bytes":al,"allocated_fmt":fmt_bytes(al),
            "traffic_used":tr,"traffic_fmt":fmt_bytes(tr),
            "remaining_bytes":max(0,tot-al),
            "remaining_fmt":fmt_bytes(max(0,tot-al)),
            "created_at":r.get("created_at"),"links_count":lc,
            "login_link":f"https://{host}/r/{r.get('login_token','')}"})
    return {"resellers": result}

@api_router.post("/resellers")
async def create_reseller(request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "admin": raise HTTPException(403, "forbidden")
    body = await request.json()
    name = str(body.get("name","")).strip()
    pw = str(body.get("password","")).strip()
    limit_gb = float(body.get("limit_gb") or 0)
    if not name or not pw: raise HTTPException(400, "نام و رمز الزامی است")
    if limit_gb <= 0: raise HTTPException(400, "حجم باید > ۰ باشد")
    rid = secrets.token_hex(8)
    sub_id = f"reseller_{rid}"
    async with SUBS_LOCK:
        SUBS[sub_id] = {"name":f"گروه {name}","is_personal":True,
            "link_ids":[],"created_at":datetime.now().isoformat(),"creator_id":rid}
    async with RESELLERS_LOCK:
        RESELLERS[rid] = {"name":name,"password_hash":hash_password(pw),
            "total_bytes":parse_size_to_bytes(limit_gb,"GB"),
            "allocated_bytes":0,"active":True,
            "login_token":secrets.token_urlsafe(16),
            "created_at":datetime.now().isoformat(),"sub_id":sub_id}
    await save_state()
    log_activity("system",f"نماینده «{name}» با {limit_gb}GB ساخته شد","ok")
    return {"ok":True,"id":rid,"name":name,"limit_gb":limit_gb,"sub_id":sub_id}

@api_router.patch("/resellers/{rid}")
async def update_reseller(rid: str, request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "admin": raise HTTPException(403, "forbidden")
    body = await request.json()
    new_total = None
    if "limit_gb" in body:
        new_total = parse_size_to_bytes(float(body["limit_gb"]),"GB")
        async with LINKS_LOCK:
            used = sum(l.get("limit_bytes",0) for l in LINKS.values() if l.get("creator_id") == rid)
        if new_total < used:
            raise HTTPException(400, f"حجم کمتر از مصرف ({fmt_bytes(used)})")
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404, "نماینده یافت نشد")
        r = RESELLERS[rid]
        if "name" in body and str(body["name"]).strip(): r["name"] = str(body["name"]).strip()
        if "active" in body:
            r["active"] = bool(body["active"])
            log_activity("system",f"نماینده «{r['name']}» {'فعال' if r['active'] else 'غیرفعال'} شد","info")
        if new_total is not None:
            r["total_bytes"] = new_total
            log_activity("system",f"حجم «{r['name']}» به {body['limit_gb']}GB","info")
        if "password" in body and str(body["password"]).strip():
            r["password_hash"] = hash_password(str(body["password"]).strip())
            log_activity("system",f"رمز «{r['name']}» تغییر کرد","info")
    await save_state()
    return {"ok": True}

@api_router.delete("/resellers/{rid}")
async def delete_reseller(rid: str, request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "admin": raise HTTPException(403, "forbidden")
    async with RESELLERS_LOCK:
        if rid not in RESELLERS: raise HTTPException(404)
        del RESELLERS[rid]
    await save_state()
    log_activity("system",f"نماینده {rid[:8]}... حذف شد","warn")
    return {"ok": True, "deleted": rid}

@api_router.get("/resellers/{rid}/links")
async def reseller_links(rid: str, request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "admin": raise HTTPException(403, "forbidden")
    async with LINKS_LOCK:
        result = [{"uuid":uid,**d} for uid,d in LINKS.items() if d.get("creator_id") == rid]
    return {"links": result}

@api_router.get("/reseller/status")
async def reseller_status(request: Request):
    s = await require_reseller_auth(request)
    if s["role"] != "reseller": raise HTTPException(403, "forbidden")
    async with RESELLERS_LOCK:
        r = RESELLERS.get(s["user_id"])
        if not r: raise HTTPException(404, "not found")
    async with LINKS_LOCK: snap = dict(LINKS)
    al = sum(l.get("limit_bytes",0) for l in snap.values() if l.get("creator_id")==s["user_id"])
    tr = sum(l.get("used_bytes",0) for l in snap.values() if l.get("creator_id")==s["user_id"])
    lc = sum(1 for l in snap.values() if l.get("creator_id")==s["user_id"])
    tot = r.get("total_bytes",0)
    return {"ok":True,"name":r["name"],"total_bytes":tot,"total_fmt":fmt_bytes(tot),
        "allocated_bytes":al,"allocated_fmt":fmt_bytes(al),
        "remaining_bytes":max(0,tot-al),"remaining_fmt":fmt_bytes(max(0,tot-al)),
        "traffic_used":tr,"traffic_fmt":fmt_bytes(tr),
        "links_count":lc,"sub_id":r.get("sub_id")}

@token_router.get("/r/{login_token}")
async def reseller_token_login(login_token: str):
    async with RESELLERS_LOCK:
        for rid, res in RESELLERS.items():
            if res.get("login_token") == login_token and res.get("active", True):
                token = await create_session("reseller", rid)
                log_activity("auth",f"ورود {res['name']} با لینک اختصاصی","ok")
                resp = RedirectResponse(url="/dashboard")
                resp.set_cookie(COOKIE_NAME, token, max_age=7*24*3600,
                    httponly=True, samesite="lax", path="/")
                return resp
    return HTMLResponse("<h2 style='padding:40px;font-family:sans-serif'>لینک نامعتبر است</h2>", status_code=404)


# ── Front-end JavaScript (تزریق به داشبورد) ──────────────────────────────────
# این تابع main.py فراخونی می‌کنه وقتی dashboard می‌خواد HTML بده
def render_dashboard(role: str, dashboard_html: str) -> str:
    if role != "reseller":
        return dashboard_html
    
    css = """
<style>
body.role-reseller [data-pg-info],body.role-reseller [data-pg-settings],
body.role-reseller [data-pg-resellers],body.role-reseller [data-pg-ipsettings],
body.role-reseller [data-pg-telegram],body.role-reseller .admin-only,
body.role-reseller #link-exp-days,body.role-reseller #link-expires,
body.role-reseller #link-ips,body.role-reseller #link-port,
body.role-reseller #link-sub,body.role-reseller [class*="exp-"],
body.role-reseller [class*="ip-"],body.role-reseller [class*="port-"]{display:none!important}
</style>"""
    
    js = """
<script>
(async function(){
  try{
    document.body.classList.add('role-reseller');
    const r=await fetch('/api/reseller/status');
    if(!r.ok)return;
    const d=await r.json();
    if(!d||!d.ok)return;
    const pct=d.total_bytes?Math.min(100,d.allocated_bytes/d.total_bytes*100):0;
    const O=document.body||document.documentElement;
    const bar=document.createElement('div');
    bar.style.cssText='margin:15px;padding:18px;background:linear-gradient(135deg,rgba(217,119,6,.1),rgba(217,119,6,.03));border:1px solid rgba(217,119,6,.25);border-radius:14px;direction:rtl';
    bar.innerHTML='<div style="display:flex;justify-content:space-between;margin-bottom:10px"><div style=\"font-weight:700;font-size:15px\">📊 وضعیت نمایندگی</div><div style=\"font-size:11px;color:var(--dim)\">'+(d.name||'')+'</div></div><div style=\"height:14px;background:rgba(0,0,0,.3);border-radius:7px;overflow:hidden;margin-bottom:8px\"><div style=\"height:100%;width:'+pct+'%;background:linear-gradient(90deg,#10b981,#06b6d4)\"></div></div><div style=\"display:grid;grid-template-columns:repeat(3,1fr);gap:12px;font-size:12px\"><div><div style=\"color:var(--dim);font-size:10px\">کل</div><div style=\"font-weight:700\">'+(d.total_fmt||'-')+'</div></div><div><div style=\"color:var(--dim);font-size:10px\">تخصیص</div><div style=\"font-weight:700;color:var(--orange)\">'+(d.allocated_fmt||'-')+'</div></div><div><div style=\"color:var(--dim);font-size:10px\">باقی</div><div style=\"font-weight:700;color:'+(d.remaining_bytes>0?'var(--green-t)':'var(--red-t)')+'\">'+(d.remaining_fmt||'-')+'</div></div></div>';
    const targets=[document.getElementById('pg-overview'),document.getElementById('overview'),document.querySelector('main'),document.body];
    for(const t of targets){if(t&&t!==document.body){t.prepend(bar);break}}
  }catch(e){console.error('reseller status:',e)}
})();
</script>"""
    
    return dashboard_html + css + js
