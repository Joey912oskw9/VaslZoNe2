# public_page.py - VaslZone Subscription Page v2.0 BOOM
from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url: str, title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VaslZone · اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-10px)}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.5}}}}
@keyframes shake{{0%,100%{{transform:rotate(0)}}25%{{transform:rotate(-5deg)}}75%{{transform:rotate(5deg)}}}}
@keyframes explode{{0%{{transform:scale(1);opacity:1}}50%{{transform:scale(3);opacity:.5}}100%{{transform:scale(0);opacity:0}}}}
@keyframes bg-scroll{{0%{{background-position:0% 50%}}50%{{background-position:100% 50%}}100%{{background-position:0% 50%}}}}
:root{{--bg:#0a0a05;--bg2:#0d0d08;--card:#12120e;--card2:#1a1a14;--yellow:#ffd700;--yellow2:#ffc107;--yellow3:#ffe44d;--yellow-d:rgba(255,215,0,0.1);--black:#000;--text:#f5f5dc;--text2:#bdb76b;--text3:#6b6b40;--green:#66bb6a;--green-d:rgba(102,187,106,0.1);--red:#ef5350;--red-d:rgba(239,83,80,0.1);--border:rgba(255,215,0,0.12);--border2:rgba(255,215,0,0.3);--shadow:0 8px 32px rgba(0,0,0,0.6)}}
html,body{{height:100%}}
body{{font-family:Vazirmatn,sans-serif;background:radial-gradient(ellipse 80% 35% at 50% -5%,rgba(255,215,0,0.06),transparent),var(--bg);color:var(--text);direction:rtl;min-height:100vh;overflow-x:hidden;position:relative}}
.grid-bg{{position:fixed;inset:0;background-image:linear-gradient(rgba(255,215,0,0.018) 1px,transparent 1px),linear-gradient(90deg,rgba(255,215,0,0.018) 1px,transparent 1px);background-size:45px 45px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:560px;margin:0 auto;padding:16px 12px 60px}}
/* ───── هدر ───── */
.header{{text-align:center;padding:20px 0 10px;position:relative}}
.header::after{{content:'';position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:60px;height:2px;background:linear-gradient(90deg,transparent,var(--yellow),transparent)}}
.profile-pic{{width:80px;height:80px;border-radius:24px;margin:0 auto 14px;background:linear-gradient(135deg,var(--yellow),var(--yellow2));display:flex;align-items:center;justify-content:center;font-size:38px;color:#000;box-shadow:0 0 0 4px var(--yellow-d),0 12px 36px rgba(255,215,0,0.2);position:relative;animation:float 4s ease-in-out infinite}}
.profile-pic i{{position:relative;z-index:1}}
.ch-name{{font-size:28px;font-weight:900;background:linear-gradient(135deg,var(--yellow),var(--yellow3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:-.02em;text-shadow:0 0 40px rgba(255,215,0,0.2)}}
.ch-sub{{font-size:9px;color:var(--text3);letter-spacing:.25em;text-transform:uppercase;margin-top:4px;font-weight:500}}
.ch-link{{display:inline-flex;align-items:center;gap:6px;margin-top:8px;padding:5px 14px;border-radius:20px;background:var(--yellow-d);border:1px solid var(--border);color:var(--yellow);text-decoration:none;font-size:10.5px;font-weight:600;transition:.2s}}
.ch-link:hover{{background:rgba(255,215,0,0.18);border-color:var(--border2)}}
/* ───── موزیک ───── */
.music-btn{{position:fixed;bottom:20px;right:20px;width:44px;height:44px;border-radius:50%;background:var(--card);border:1px solid var(--border);color:var(--yellow);display:flex;align-items:center;justify-content:center;font-size:20px;cursor:pointer;z-index:100;transition:.2s;box-shadow:var(--shadow)}}
.music-btn:hover{{background:var(--yellow-d);border-color:var(--border2);transform:scale(1.1)}}
/* ───── کارت اطلاعات ───── */
.info-card{{background:var(--card);border:1px solid var(--border);border-radius:18px;padding:18px 20px;margin-bottom:14px;position:relative;overflow:hidden;backdrop-filter:blur(6px)}}
.info-card::before{{content:'';position:absolute;top:-50px;left:-50px;width:150px;height:150px;background:radial-gradient(circle,rgba(255,215,0,0.05),transparent 70%);pointer-events:none}}
.info-name{{font-size:18px;font-weight:800;color:var(--text);margin-bottom:4px}}
.info-url{{font-family:monospace;font-size:10px;color:var(--yellow3);word-break:break-all;line-height:1.6;background:rgba(0,0,0,0.3);padding:8px 10px;border-radius:8px;border:1px dashed var(--border);margin-top:8px;display:flex;align-items:center;gap:8px}}
/* ───── استات باکس ───── */
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}}
.stat{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 12px;text-align:center;transition:.2s}}
.stat:hover{{border-color:var(--border2);transform:translateY(-2px)}}
.stat .sl{{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}}
.stat .sv{{font-size:20px;font-weight:800;color:var(--yellow);line-height:1}}
.stat .ss{{font-size:9px;color:var(--text2);margin-top:5px;display:flex;align-items:center;justify-content:center;gap:4px}}
.dot-g{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite;box-shadow:0 0 6px var(--green)}}
/* ───── کارت کانفیگ ───── */
.cfg-card{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:16px 17px;margin-bottom:12px;position:relative;overflow:hidden;border-right:3px solid var(--yellow);transition:.2s}}
.cfg-card:hover{{border-color:var(--border2);transform:translateY(-2px)}}
.cfg-head{{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:10px;flex-wrap:wrap}}
.cfg-label{{font-size:14px;font-weight:700;color:var(--text);display:flex;align-items:center;gap:6px}}
.cfg-proto{{font-size:8px;padding:2px 8px;border-radius:5px;font-weight:700;background:var(--yellow-d);color:var(--yellow);border:1px solid var(--border)}}
.cfg-status{{font-size:9px;padding:3px 9px;border-radius:15px;font-weight:700}}
.cfg-status.ok{{background:var(--green-d);color:var(--green);border:1px solid rgba(102,187,106,0.25)}}
.cfg-status.off{{background:var(--red-d);color:var(--red);border:1px solid rgba(239,83,80,0.25)}}
.cfg-bar{{height:5px;border-radius:3px;background:rgba(255,215,0,0.08);overflow:hidden;margin:6px 0}}
.cfg-bar-fill{{height:100%;border-radius:3px;background:var(--yellow);transition:width .5s}}
.cfg-info{{font-size:10px;color:var(--text2);display:flex;justify-content:space-between;margin-bottom:8px}}
.cfg-info b{{color:var(--yellow3)}}
.cfg-remain{{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;padding:3px 10px;border-radius:6px;margin-top:4px}}
.cfg-remain.ok{{background:var(--green-d);color:var(--green)}}
.cfg-remain.warn{{background:rgba(255,215,0,0.08);color:var(--yellow)}}
.cfg-remain.danger{{background:var(--red-d);color:var(--red)}}
.cfg-link-area{{display:none;margin-top:8px}}
.cfg-link-area.show{{display:block}}
.cfg-link{{background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font-family:monospace;font-size:9px;color:var(--yellow3);word-break:break-all;line-height:1.5;max-height:70px;overflow-y:auto;direction:ltr;text-align:left}}
.cfg-actions{{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap}}
.btn{{font-family:inherit;font-size:10.5px;font-weight:700;padding:7px 14px;border-radius:9px;cursor:pointer;border:none;display:flex;align-items:center;gap:4px;transition:.15s;flex:1;justify-content:center}}
.btn-y{{background:linear-gradient(135deg,var(--yellow),var(--yellow2));color:#000;box-shadow:0 3px 12px rgba(255,215,0,0.25)}}
.btn-y:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(255,215,0,0.35)}}
.btn-o{{background:transparent;border:1px solid var(--border);color:var(--text2)}}
.btn-o:hover{{background:var(--yellow-d);color:var(--yellow);border-color:var(--border2)}}
.btn-sm{{padding:5px 10px;font-size:9px;flex:0}}
.copy-all{{background:linear-gradient(135deg,var(--yellow),var(--yellow2));border-radius:12px;padding:14px 16px;margin-bottom:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;box-shadow:0 6px 24px rgba(255,215,0,0.2)}}
.copy-all-text{{flex:1}}
.copy-all-title{{font-size:12px;font-weight:800;color:#000;display:flex;align-items:center;gap:5px}}
.copy-all-sub{{font-size:9.5px;color:rgba(0,0,0,0.6);margin-top:2px}}
.copy-all-btn{{background:#000;color:var(--yellow);border:none;padding:9px 18px;border-radius:10px;font-family:inherit;font-size:11pt;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.15s}}
.copy-all-btn:hover{{transform:translateY(-2px)}}
/* ───── سرعت ───── */
.speed-card{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:16px 17px;margin-bottom:14px}}
.speed-head{{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}}
.speed-title{{font-size:11px;font-weight:800;color:var(--text2);display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.06em}}
.speed-title i{{color:var(--yellow);font-size:14px}}
.speed-btn{{padding:6px 14px;border-radius:8px;border:1px solid var(--border);background:var(--yellow-d);color:var(--yellow);font-family:inherit;font-size:10.5px;font-weight:700;cursor:pointer;transition:.15s}}
.speed-btn:hover{{background:rgba(255,215,0,0.2);border-color:var(--border2)}}
.speed-btn:disabled{{opacity:.5}}
.speed-result{{font-family:monospace;font-size:13px;font-weight:800;color:var(--yellow3);padding:10px;background:rgba(0,0,0,0.3);border-radius:9px;text-align:center;direction:ltr}}
/* ───── نمودار ───── */
.chart-card{{background:var(--card);border:1px solid var(--border);border-radius:18px;padding:16px 17px;margin-bottom:14px}}
.chart-title{{font-size:11px;font-weight:800;color:var(--text2);margin-bottom:12px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.06em}}
.chart-title i{{color:var(--yellow);font-size:14px}}
.chart-body{{height:200px;margin-bottom:10px}}
.chart-tabs{{display:flex;gap:5px;flex-wrap:wrap}}
.chart-tab{{padding:5px 12px;border-radius:6px;font-size:9.5px;font-weight:700;background:var(--yellow-d);color:var(--text2);border:1px solid var(--border);cursor:pointer;transition:.15s;font-family:inherit}}
.chart-tab.active{{background:var(--yellow);color:#000;border-color:var(--yellow)}}
.chart-tip{{font-size:10px;color:var(--text3);text-align:center;margin-top:8px;font-weight:600}}
/* ───── فوتر ───── */
.footer{{text-align:center;padding:20px 0;font-size:9px;color:var(--text3)}}
.footer a{{color:var(--yellow);font-weight:700;text-decoration:none}}
.toast{{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);border:1px solid var(--border2);color:var(--text);border-radius:10px;padding:8px 16px;font-size:11px;font-weight:600;opacity:0;transition:.25s;z-index:999;white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
@media(max-width:450px){{.stats{{grid-template-columns:1fr 1fr}}.ch-name{{font-size:22px}}}}
/* ───── راکت ───── */
.rocket-area{{position:fixed;left:10px;top:50%;transform:translateY(-50%);z-index:50;display:flex;flex-direction:column;align-items:center;gap:4px}}
.rocket{{width:48px;height:48px;cursor:pointer;font-size:32px;color:var(--yellow);animation:float 3s ease-in-out infinite;transition:.3s;text-align:center;filter:drop-shadow(0 0 10px rgba(255,215,0,0.4))}}
.rocket.launch{{animation:launchRocket 1.2s cubic-bezier(.2,.8,.4,1) forwards!important}}
@keyframes launchRocket{{0%{{transform:translateY(0) rotate(0)}}30%{{transform:translateY(-40px) rotate(-10deg)}}60%{{transform:translateY(-80px) rotate(10deg) scale(1.2)}}100%{{transform:translateY(calc(100vh - 200px)) rotate(5deg) scale(0.8)}}}}
.rocket-explode{{position:fixed;width:100px;height:100px;pointer-events:none;z-index:60;opacity:0}}
.rocket-explode.go{{animation:explode .6s ease-out forwards}}
@media(max-width:500px){{.rocket-area{{display:none}}}}
</style></head><body>
<audio id="bg-music" loop style="display:none">
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3" type="audio/mpeg">
</audio>
<div class="grid-bg"></div>
<div class="toast" id="toast"></div>
<div class="rocket-area" id="rocketArea">
  <div style="font-size:8px;color:var(--text3);letter-spacing:.1em;writing-mode:vertical-rl;font-weight:700">شلیک</div>
  <div class="rocket" id="rocket" onclick="launchRocket()"><i class="ti ti-rocket"></i></div>
</div>
<div class="rocket-explode" id="rocketExplode"><div style="width:100%;height:100%;border-radius:50%;background:radial-gradient(circle,var(--yellow),transparent 70%)"></div></div>
<button class="music-btn" id="musicBtn" onclick="toggleMusic()"><i class="ti ti-music"></i></button>
<div class="wrap">
  <div class="header">
    <div class="profile-pic"><i class="ti ti-bolt"></i></div>
    <div class="ch-name">VaslZone</div>
    <div class="ch-sub">اشتراک اختصاصی</div>
    <a class="ch-link" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
  </div>
  <div id="root"><div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-loader-2" style="font-size:36px;color:var(--yellow);display:block;margin:0 auto 14px;animation:spin 1.2s linear infinite;display:inline-block"></i><p style="font-size:12px">در حال بارگذاری...</p></div></div>
  <div class="footer"><a href="https://t.me/VaslZone" target="_blank">@VaslZone</a> · VaslZone Gateway v9.3</div>
</div>
<style>@keyframes spin{{to{{transform:rotate(360deg)}}}}</style>
    <script>
const API_URL = "{api_url}";
var allLinks = [];

function fmtB(b) { if (!b || b === 0) return '0 B'; if (b < 1024) return b + ' B'; if (b < 1048576) return (b / 1024).toFixed(1) + ' KB'; if (b < 1073741824) return (b / 1048576).toFixed(2) + ' MB'; return (b / 1073741824).toFixed(2) + ' GB'; }
function esc(s) { return String(s || '').replace(/[&<>"']/g, function(c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
function toFa(n) { return String(n).replace(/\d/g, function(d) { return '۰۱۲۳۴۵۶۷۸۹'[d]; }); }

// ───── موزیک ─────
var musicOn = false;
var bgMusic = document.getElementById('bg-music');
function toggleMusic() {
  musicOn = !musicOn;
  if (musicOn) { bgMusic.volume = 0.12; bgMusic.play(); document.getElementById('musicBtn').innerHTML = '<i class="ti ti-music-off"></i>'; }
  else { bgMusic.pause(); document.getElementById('musicBtn').innerHTML = '<i class="ti ti-music"></i>'; }
}
document.addEventListener('click', function() { if (!musicOn) { musicOn = true; try { bgMusic.volume = 0.12; bgMusic.play(); } catch(e) {} document.getElementById('musicBtn').innerHTML = '<i class="ti ti-music-off"></i>'; } }, { once: true });

// ───── راکت ─────
function launchRocket() {
  var r = document.getElementById('rocket');
  if (r.classList.contains('launch')) return;
  r.classList.add('launch');
  setTimeout(function() {
    var exp = document.getElementById('rocketExplode');
    var rect = r.getBoundingClientRect();
    exp.style.left = (rect.left - 25) + 'px';
    exp.style.top = (rect.top + 50) + 'px';
    exp.classList.add('go');
    setTimeout(function() {
      exp.classList.remove('go');
      r.classList.remove('launch');
      window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    }, 800);
  }, 1000);
}

// ───── تاست ─────
function toast(m) { var t = document.getElementById('toast'); t.textContent = m; t.className = 'toast show'; setTimeout(function() { t.classList.remove('show'); }, 1800); }

// ───── لود ─────
async function loadData() {
  try {
    var r = await fetch(API_URL);
    if (!r.ok) throw new Error();
    return await r.json();
  } catch(e) { return null; }
}

// ───── سرعت تست ─────
async function runSpeedTest() {
  var btn = document.getElementById('speedBtn');
  var res = document.getElementById('speedResult');
  btn.disabled = true;
  res.textContent = 'در حال تست...';
  var start = Date.now();
  try {
    var r = await fetch(API_URL + '?_=' + Date.now());
    var data = await r.json();
    var ms = Date.now() - start;
    var ping = ms < 50 ? '🟢' : ms < 150 ? '🟡' : '🔴';
    res.textContent = ping + ' پینگ: ' + ms + 'ms · ' + (data.links ? data.links.length + ' کانفیگ' : '—');
  } catch(e) { res.textContent = '🔴 قطع / خطا'; }
  btn.disabled = false;
}

// ───── رندر ─────
var usageChart = null;

function render(d) {
  if (!d || !d.links || !d.links.length) {
    document.getElementById('root').innerHTML = '<div class="empty" style="text-align:center;padding:70px 20px;color:var(--text3)"><i class="ti ti-link-off" style="font-size:40px;display:block;margin-bottom:14px;opacity:.3"></i><p style="font-size:12px">کانفیگی یافت نشد</p></div>';
    return;
  }
  allLinks = d.links;
  var active = d.links.filter(function(l) { return l.active; }).length;
  var totalUsed = d.links.reduce(function(s, l) { return s + (l.used_bytes || 0); }, 0);
  var h = '';

  // ───── کارت اطلاعات ─────
  h += '<div class="info-card"><div class="info-name">' + esc(d.name || 'VaslZone') + '</div>' +
    (d.desc ? '<div style="font-size:11px;color:var(--text2);margin-top:4px;line-height:1.6">' + esc(d.desc) + '</div>' : '') +
    '<div class="info-url"><span style="flex:1;word-break:break-all;min-width:0">' + esc(d.sub_url || '') + '</span>' +
    '<button class="btn btn-y btn-sm" onclick="navigator.clipboard.writeText(\'' + esc(d.sub_url || '') + '\').then(function(){toast(\'کپی شد \')})"><i class="ti ti-copy"></i></button>' +
    '<button class="btn btn-o btn-sm" onclick="showQR(\'' + esc(d.sub_url || '') + '\')"><i class="ti ti-qrcode"></i></button></div></div>';

  // ───── استات ─────
  h += '<div class="stats"><div class="stat"><div class="sl">وضعیت</div><div class="sv" style="font-size:' + (d.links.length === 1 ? '16' : '20') + 'px">' +
    (d.links.length === 1 ? (d.links[0].active ? 'فعال' : 'غیرفعال') : active + ' / ' + d.links.length) + '</div><div class="ss"></div></div>' +
    '<div class="stat"><div class="sl">مصرف کل</div><div class="sv" style="font-size:17px">' + fmtB(totalUsed) + '</div><div class="ss">از مجموع</div></div>' +
    '<div class="stat"><div class="sl">اتصالات زنده</div><div class="sv">' + (d.active_connections || 0) + '</div><div class="ss"><span class="dot-g"></span> آنلاین</div></div></div>';

  // ───── کپی همه ─────
  if (d.links.length > 1) {
    h += '<div class="copy-all"><div class="copy-all-text"><div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه کانفیگ‌ها</div><div class="copy-all-sub">یک‌بار کلیک، همه لینک‌ها کپی می‌شه</div></div><button class="copy-all-btn" onclick="copyAll()"><i class="ti ti-clipboard-copy"></i> کپی (' + active + ')</button></div>';
  }

  // ───── لیست کانفیگ‌ها ─────
  for (var i = 0; i < d.links.length; i++) {
    var l = d.links[i];
    var pct = l.limit_bytes > 0 ? Math.min(100, (l.used_bytes / l.limit_bytes) * 100) : 0;
    var bc = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--yellow)' : 'var(--green)';
    var remain = l.limit_bytes > 0 ? Math.max(0, l.limit_bytes - l.used_bytes) : -1;
    var rf = remain < 0 ? '∞' : fmtB(remain);
    var rc = remain < 0 ? 'ok' : (remain < 1048576 ? 'danger' : (remain < 1073741824 ? 'warn' : 'ok'));
    var remainLabel = remain < 0 ? 'نامحدود' : rf;

    h += '<div class="cfg-card" id="cfg-' + i + '">' +
      '<div class="cfg-head"><div class="cfg-label">' + esc(l.label) + ' <span class="cfg-proto">' + (l.protocol && l.protocol.indexOf('xhttp') !== -1 ? 'XHTTP' : 'VLESS') + '</span></div>' +
      '<span class="cfg-status ' + (l.active ? 'ok' : 'off') + '">' + (l.active ? 'فعال' : 'غیرفعال') + '</span></div>' +
      '<div class="cfg-info"><span>مصرف: <b>' + l.used_fmt + '</b></span><span>سهمیه: <b>' + l.limit_fmt + '</b></span></div>' +
      '<div class="cfg-bar"><div class="cfg-bar-fill" style="width:' + pct + '%;background:' + bc + '"></div></div>' +
      '<span class="cfg-remain ' + rc + '"><i class="ti ti-' + (remain < 0 ? 'infinity' : 'database') + '"></i> ' + (remain < 0 ? 'نامحدود' : 'باقی‌مانده: ' + rf) + '</span>' +
      '<div class="cfg-link-area" id="vla-' + i + '"><div class="cfg-link">' + esc(l.vless_link || '') + '</div></div>' +
      '<div class="cfg-actions">' +
      '<button class="btn btn-y" onclick="toggleVless(' + i + ');event.stopPropagation()"><i class="ti ti-eye"></i> نمایش لینک</button>' +
      '<button class="btn btn-y" onclick="navigator.clipboard.writeText(window._links[' + i + '].vless).then(function(){toast(\'کپی شد \')})"><i class="ti ti-copy"></i> کپی</button>' +
      '<button class="btn btn-o btn-sm" onclick="showQR(window._links[' + i + '].vless)"><i class="ti ti-qrcode"></i></button></div></div>';
  }

  // ───── سرعت سنج ─────
  h += '<div class="speed-card"><div class="speed-head"><div class="speed-title"><i class="ti ti-speedtest"></i> تست سرعت</div><button class="speed-btn" id="speedBtn" onclick="runSpeedTest()"><i class="ti ti-player-play"></i> شروع تست</button></div><div class="speed-result" id="speedResult">برای تست کلیک کنید</div></div>';

  // ───── نمودار ─────
  h += '<div class="chart-card"><div class="chart-title"><i class="ti ti-chart-bar"></i> نمودار مصرف</div><div class="chart-body"><canvas id="usageChart"></canvas></div>' +
    '<div class="chart-tabs" id="chartTabs">' +
    '<button class="chart-tab" data-range="10s" onclick="setChartRange(\'10s\',this)">۱۰ ثانیه</button>' +
    '<button class="chart-tab" data-range="10m" onclick="setChartRange(\'10m\',this)">۱۰ دقیقه</button>' +
    '<button class="chart-tab active" data-range="1h" onclick="setChartRange(\'1h\',this)">۱ ساعت</button>' +
    '<button class="chart-tab" data-range="1d" onclick="setChartRange(\'1d\',this)">۱ روز</button>' +
    '</div><div class="chart-tip" id="chartTip">↕ نشانگر رو ۲ ثانیه نگه دار برای مقدار دقیق</div></div>';

  document.getElementById('root').innerHTML = h;
  window._links = d.links.map(function(l) { return { vless: l.vless_link || '', label: l.label, used: l.used_bytes, limit: l.limit_bytes }; });

  setTimeout(function() {
    try { initChart(); } catch(e) {}
  }, 200);
}

function toggleVless(i) {
  var el = document.getElementById('vla-' + i);
  if (el) el.classList.toggle('show');
}

function copyAll() {
  var txt = window._links.map(function(l) { return l.vless; }).filter(Boolean).join('\n');
  if (!txt) return;
  navigator.clipboard.writeText(txt).then(function() { toast('✅ همه کپی شد'); });
}

function showQR(url) {
  if (!url) return;
  window.open('https://api.qrserver.com/v1/create-qr-code/?size=280x280&data=' + encodeURIComponent(url), '_blank');
}

// ───── نمودار ─────
var chartRange = '1h';

function setChartRange(range, btn) {
  chartRange = range;
  var btns = document.querySelectorAll('.chart-tab');
  for (var i = 0; i < btns.length; i++) btns[i].classList.remove('active');
  btn.classList.add('active');
  updateChart();
}

function initChart() {
  var c = document.getElementById('usageChart');
  if (!c) return;
  if (typeof Chart === 'undefined') return;
  if (usageChart) { usageChart.destroy(); }
  var labels = [], values = [];
  var points = 20;
  for (var i = 0; i < points; i++) {
    labels.push('');
    values.push(0);
  }
  usageChart = new Chart(c.getContext('2d'), {
    type: 'line',
    data: { labels: labels, datasets: [{ label: 'MB', data: values, borderColor: '#ffd700', backgroundColor: 'rgba(255,215,0,0.1)', fill: true, tension: 0.4, pointRadius: 3, pointBackgroundColor: '#ffd700', pointHoverRadius: 6, borderWidth: 2 }] },
    options: {
      responsive: true, maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: { legend: { display: false }, tooltip: { backgroundColor: 'rgba(12,12,10,0.95)', titleColor: '#ffd700', bodyColor: '#bdb76b', padding: 12, cornerRadius: 8, displayColors: false, titleFont: { size: 11 }, bodyFont: { size: 11 }, callbacks: { label: function(ctx) { return ctx.parsed.y.toFixed(2) + ' MB'; } } } },
      scales: { x: { grid: { display: false }, ticks: { color: '#6b6b40', maxTicksLimit: 6, font: { size: 9 } } }, y: { grid: { color: 'rgba(255,215,0,0.05)' }, ticks: { color: '#6b6b40', font: { size: 9 }, callback: function(v) { return v + ' MB'; } } } }
    }
  });
  updateChart();
}

function updateChart() {
  if (!usageChart) return;
  var points = 20;
  var maxVal = 100;
  if (chartRange === '10s') { points = 10; maxVal = 50; }
  else if (chartRange === '10m') { points = 20; maxVal = 100; }
  else if (chartRange === '1h') { points = 30; maxVal = 200; }
  else if (chartRange === '1d') { points = 48; maxVal = 500; }

  var labels = [], values = [];
  for (var i = 0; i < points; i++) {
    var t = '';
    if (chartRange === '10s') t = (i * 1) + 's';
    else if (chartRange === '10m') t = (i * 30) + 's';
    else if (chartRange === '1h') t = (i * 2) + 'm';
    else t = (i * 30) + 'm';
    labels.push(t);
    var val = Math.random() * maxVal * 0.8;
    if (window._links && window._links.length > 0) {
      var totalUsed = window._links.reduce(function(s, l) { return s + (l.used || 0); }, 0);
      val = Math.min(maxVal, (totalUsed / 1073741824) * (i / points) * 2 + Math.random() * 5);
    }
    values.push(parseFloat(val.toFixed(2)));
  }
  usageChart.data.labels = labels;
  usageChart.data.datasets[0].data = values;
  usageChart.update();
}

// ───── راه‌اندازی ─────
(async function init() {
  var d = await loadData();
  if (d) {
    render(d);
  } else {
    document.getElementById('root').innerHTML = '<div class="empty" style="text-align:center;padding:70px 20px;color:var(--text3)"><i class="ti ti-alert-circle" style="font-size:40px;color:var(--red);display:block;margin-bottom:14px"></i><p>خطا در بارگذاری</p></div>';
  }
})();
</script>
</body></html>"""

def get_public_page_html(uuid_key: str) -> str:
    return get_sub_page_html(
        api_url=f"/api/public/sub/{uuid_key}",
        title="VaslZone Group",
    )

def get_single_sub_page_html(uuid: str) -> str:
    return get_sub_page_html(
        api_url=f"/api/public/sub-single/{uuid}",
        title="VaslZone Config",
    )
