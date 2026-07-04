def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب v11 - طراحی مینیمال و حرفه‌ای با کارت‌های شیشه‌ای"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>VaslZone Sub · {uuid_key[:8]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#0b0e1a;--bg2:#11162b;--bg3:#181f3a;
  --card:rgba(16,20,38,0.8);--card-border:rgba(59,130,246,0.12);--card-border-hover:rgba(59,130,246,0.25);
  --accent:#3b82f6;--accent2:#60a5fa;--accent-glow:rgba(59,130,246,0.12);
  --green:#10b981;--green-bg:rgba(16,185,129,0.06);--green-t:#34d399;
  --red:#ef4444;--red-bg:rgba(239,68,68,0.06);--red-t:#f87171;
  --amber:#f59e0b;--amber-bg:rgba(245,158,11,0.06);--amber-t:#fbbf24;
  --purple:#8b5cf6;--purple-bg:rgba(139,92,246,0.06);--purple-t:#a78bfa;
  --t1:#e8f0fe;--t2:#8aa8d8;--t3:#4a5f82;
  --radius:20px;--shadow:0 12px 48px rgba(0,0,0,0.3);
  --transition:0.3s cubic-bezier(0.4,0,0.2,1);
}}
[data-theme="light"]{{
  --bg:#eef2f7;--bg2:#dce5f2;--bg3:#c8d4e8;
  --card:rgba(255,255,255,0.8);--card-border:rgba(59,130,246,0.12);--card-border-hover:rgba(59,130,246,0.25);
  --accent:#2563eb;--accent2:#1d4ed8;--accent-glow:rgba(37,99,235,0.06);
  --green:#059669;--green-bg:rgba(5,150,105,0.04);--green-t:#047857;
  --red:#dc2626;--red-bg:rgba(220,38,38,0.04);--red-t:#b91c1c;
  --amber:#d97706;--amber-bg:rgba(217,119,6,0.04);--amber-t:#b45309;
  --purple:#7c3aed;--purple-bg:rgba(124,58,237,0.04);--purple-t:#5b21b6;
  --t1:#0f172a;--t2:#334155;--t3:#64748b;
  --shadow:0 12px 40px rgba(0,0,0,0.04);
}}
html,body{{min-height:100%;background:var(--bg);font-family:'Vazirmatn',sans-serif;color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
#particles-canvas{{position:fixed;inset:0;z-index:0;pointer-events:none}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(59,130,246,0.06),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.wrap{{position:relative;z-index:10;max-width:840px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;gap:12px}}
.brand{{display:flex;align-items:center;gap:12px;min-width:0}}
.brand-img{{width:44px;height:44px;border-radius:14px;overflow:hidden;border:1px solid var(--card-border);box-shadow:0 0 30px var(--accent-glow);flex-shrink:0}}
.brand-img img{{width:100%;height:100%;object-fit:cover}}
.brand-name{{font-size:16px;font-weight:900;background:linear-gradient(135deg,#3b82f6,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:-.01em}}
.brand-sub{{font-size:10px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:8px;flex-shrink:0}}
.icon-btn{{width:38px;height:38px;border-radius:12px;background:var(--card);border:1px solid var(--card-border);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:17px;cursor:pointer;transition:.2s;backdrop-filter:blur(4px)}}
.icon-btn:hover{{background:var(--accent-glow);color:var(--accent2);border-color:var(--card-border-hover)}}
.sub-info{{background:var(--card);border:1px solid var(--card-border);border-radius:var(--radius);padding:24px 26px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden;backdrop-filter:blur(16px)}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(59,130,246,0.04),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10.5px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:8px}}
.sub-eyebrow i{{font-size:14px}}
.sub-name{{font-size:24px;font-weight:900;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:13px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:11px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:8px}}
.sub-sub-box{{background:var(--accent-glow);border:1px solid var(--card-border);border-radius:14px;padding:12px 16px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}
.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:20px}}
.stat-card{{background:var(--card);border:1px solid var(--card-border);border-radius:18px;padding:16px 18px;backdrop-filter:blur(8px);transition:.2s}}
.stat-card:hover{{border-color:var(--card-border-hover);transform:translateY(-2px)}}
.stat-label{{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}}
.stat-val{{font-size:24px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:10px;color:var(--t3);margin-top:6px}}
.copy-all-bar{{display:flex;align-items:center;gap:14px;background:linear-gradient(135deg,#3b82f6,#2563eb);border-radius:20px;padding:18px 22px;margin-bottom:20px;box-shadow:0 8px 32px rgba(59,130,246,0.25);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:14px;font-weight:800;color:#fff;display:flex;align-items:center;gap:8px}}
.copy-all-sub{{font-size:10.5px;color:rgba(255,255,255,0.8);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#1d4ed8;border:none;border-radius:14px;padding:10px 20px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.2s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,0.15)}}
.copy-all-btn:active{{transform:translateY(0) scale(.97)}}
.cfg-title{{font-size:12.5px;font-weight:800;color:var(--t2);margin-bottom:14px;display:flex;align-items:center;gap:8px;text-transform:uppercase;letter-spacing:.08em}}
.cfg-title i{{color:var(--accent2);font-size:16px}}
.cfg-grid{{display:grid;gap:14px}}
.cfg-card{{background:var(--card);border:1px solid var(--card-border);border-radius:20px;transition:all var(--transition);position:relative;overflow:hidden;backdrop-filter:blur(12px)}}
.cfg-card:hover{{border-color:var(--card-border-hover);box-shadow:var(--shadow)}}
.cfg-top{{padding:18px 20px 16px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:5px}}
.proto-chip{{font-size:9px;padding:3px 10px;border-radius:7px;font-weight:800}}
.pc-ws{{background:var(--accent-glow);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 12px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:5px;border-radius:4px;background:rgba(59,130,246,0.04);overflow:hidden;margin-bottom:4px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-border);margin:0 20px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:16px;height:16px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-border)}}
.cfg-tear::before{{right:-26px}}
.cfg-tear::after{{left:-26px}}
.cfg-bottom{{padding:14px 20px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-border);border-radius:12px;padding:10px 14px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-glow);border-color:var(--card-border-hover);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,0.2);border:1px solid var(--card-border);border-radius:10px;padding:10px 14px;font-size:9.5px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:8px;max-height:80px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(0,0,0,0.03)}}
.cfg-actions{{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:12px;padding:8px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff;box-shadow:0 4px 16px rgba(59,130,246,0.25)}}
.btn-p:hover{{background:#2563eb}}
.btn-g{{background:var(--accent-glow);color:var(--accent2);border:1px solid rgba(59,130,246,0.08)}}
.btn-g:hover{{background:rgba(59,130,246,0.12)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(139,92,246,0.08)}}
.btn-pur:hover{{background:rgba(139,92,246,0.12)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 10px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.2}}}}
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:70vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-border);border-radius:28px;padding:0;text-align:center;max-width:400px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative;backdrop-filter:blur(16px)}}
.lock-banner{{background:linear-gradient(150deg,rgba(59,130,246,0.06),rgba(59,130,246,0.01) 70%);padding:36px 30px 24px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:20px;background:var(--accent-glow);border:1px solid var(--card-border-hover);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-6px;border-radius:24px;border:1px solid var(--card-border);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.4}}50%{{transform:scale(1.06);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:22px 30px 28px}}
.lock-field{{position:relative;margin-bottom:12px}}
.lock-inp{{width:100%;padding:13px 48px 13px 48px;border-radius:14px;border:1px solid var(--card-border);background:rgba(0,0,0,0.15);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.12em;transition:.18s}}
[data-theme="light"] .lock-inp{{background:rgba(0,0,0,0.02)}}
.lock-inp:focus{{border-color:var(--accent2);box-shadow:0 0 0 3px rgba(59,130,246,0.04)}}
.lock-eye{{position:absolute;left:14px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:17px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:14px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-border);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}
.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:40px;display:block;margin-bottom:14px}}
.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-border);color:var(--t1);border-radius:14px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,0.2);background:var(--green-bg);color:var(--green-t)}}
.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-border);border-radius:24px;padding:24px;text-align:center;max-width:360px;width:100%;box-shadow:var(--shadow);backdrop-filter:blur(16px)}}
.qr-title{{font-size:14px;font-weight:800;margin-bottom:14px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:14px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:12px;border-radius:14px}}
.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700}}
@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:20px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:16px 12px 50px}}
  .lock-banner{{padding:30px 22px 20px}}
  .lock-form{{padding:18px 22px 24px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<canvas id="particles-canvas"></canvas>
<div class="bg-fx"></div>
<audio id="bg-music" loop preload="auto" volume="0.02">
  <source src="https://www.bensound.com/bensound-music/bensound-slowmotion.mp3" type="audio/mpeg">
</audio>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img"><img src="https://uploadkon.ir/uploads/09bd03_26file-00000000ab2071f486cf6128924e8d11.png" alt="cb"></div>
      <div><div class="brand-name">vaslzone</div><div class="brand-sub">Gateway v11 · Bento</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-icon"></i></button>
      <a class="icon-btn" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i></a>
    </div>
  </div>
  <div id="root"><div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div></div>
  <div class="footer">کانال رسمی: <a href="https://t.me/VaslZone" target="_blank">@VaslZone</a> · VaslZone Gateway v11</div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let isDark=localStorage.getItem('VaslZone-pub-theme')!=='light';
function applyTheme(dark){{document.documentElement.setAttribute('data-theme',dark?'dark':'light');document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('VaslZone-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);

// ذرات پس‌زمینه
const c=document.getElementById('particles-canvas'),ctx=c.getContext('2d');
let w,h,pts=[];
function resize(){{w=c.width=window.innerWidth;h=c.height=window.innerHeight}}
resize();window.addEventListener('resize',resize);
const pcolors=['#3b82f6','#60a5fa','#93bbfc','#1d4ed8'];
for(let i=0;i<60;i++){{pts.push({{x:Math.random()*w,y:Math.random()*h,r:Math.random()*1.8+0.5,dx:(Math.random()-0.5)*0.4,dy:(Math.random()-0.5)*0.4,color:pcolors[Math.floor(Math.random()*pcolors.length)],alpha:Math.random()*0.4+0.15}})}}
function draw(){{ctx.clearRect(0,0,w,h);pts.forEach(p=>{{p.x+=p.dx;p.y+=p.dy;if(p.x<0||p.x>w)p.dx*=-1;if(p.y<0||p.y>h)p.dy*=-1;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.color;ctx.globalAlpha=p.alpha;ctx.fill();ctx.shadowColor=p.color;ctx.shadowBlur=8;ctx.fill();ctx.shadowBlur=0;}});requestAnimationFrame(draw)}}
draw();

const music=document.getElementById('bg-music');music.volume=0.02;document.addEventListener('click',()=>{{if(music.paused)music.play();}},{{once:true}});

// توابع اصلی
function toast(msg,type=''){{const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(()=>t.classList.remove('show'),2400);}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{if(p==='xhttp-stream-one')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';return '<span class="proto-chip pc-ws">VLESS · WS</span>';}}
function showQR(label,link){{document.getElementById('qr-label').textContent=label;document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);document.getElementById('qr-modal').classList.add('open');}}
function toggleLink(i){{const wrap=document.getElementById('vw-'+i);const btn=document.getElementById('vt-'+i);const open=wrap.classList.toggle('open');btn.classList.toggle('open',open);btn.querySelector('.ltl span').textContent=open?'پنهان کردن لینک':'نمایش لینک کانفیگ';}}
async function loadData(pw=''){{const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');const r=await fetch(url);return r.json();}}
function renderLock(name,errMsg=''){{document.getElementById('root').innerHTML=`<div class="lock-stage"><div class="lock-card"><div class="lock-banner"><div class="lock-shield"><i class="ti ti-shield-lock"></i></div><div class="lock-title">${{esc(name)}}</div><div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div></div><div class="lock-form"><div class="lock-err" id="lock-err">${{errMsg?'<i class="ti ti-alert-circle"></i> '+esc(errMsg):''}}</div><div class="lock-field"><i class="ti ti-lock lock-lockicon"></i><input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus><button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button></div><button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button></div><div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div></div></div>`;document.getElementById('lock-pw').addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});}}
function togglePwVis(){{const inp=document.getElementById('lock-pw'),icon=document.getElementById('lock-eye-icon');const toText=inp.type==='password';inp.type=toText?'text':'password';icon.className='ti '+(toText?'ti-eye-off':'ti-eye');}}
async function submitLock(){{const pw=document.getElementById('lock-pw').value;const data=await loadData(pw);if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}savedPw=pw;renderContent(data);}}
function renderContent(d){{const activeCount=d.links.filter(l=>l.active).length;const baseSubUrl=d.sub_url||(window.location.protocol+'//'+window.location.host+'/sub-group/'+UUID_KEY);const subUrl=baseSubUrl+(savedPw?'?pw='+encodeURIComponent(savedPw):'');window._VaslZoneSubUrl=subUrl;window._VaslZoneSubName=d.name;window._VaslZoneLinks=d.links.map(l=>({{vless:l.vless_link,sub:l.sub_url+(savedPw?'?pw='+encodeURIComponent(savedPw):''),label:l.label}}));document.getElementById('root').innerHTML=`
<div class="sub-info"><div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div><div class="sub-name">${{esc(d.name)}}</div>${{d.desc?`<div class="sub-desc">${{esc(d.desc)}}</div>`:''}}<div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div><div class="sub-sub-box"><span class="sub-sub-url">${{esc(subUrl)}}</span><button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px" onclick="navigator.clipboard.writeText(window._VaslZoneSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک ساب</button><button class="btn btn-g" style="padding:7px 12px;font-size:10.5px" onclick="showQR(window._VaslZoneSubName+' — کل گروه',window._VaslZoneSubUrl)"><i class="ti ti-qrcode"></i> QR کل</button></div></div>
<div class="copy-all-bar"><div class="copy-all-text"><div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div><div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div></div><button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button></div>
<div class="stats-bar"><div class="stat-card"><div class="stat-label">کانفیگ‌های فعال</div><div class="stat-val">${{toFa(activeCount)}}</div><div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div></div><div class="stat-card"><div class="stat-label">اتصالات زنده</div><div class="stat-val">${{toFa(d.active_connections)}}</div><div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div></div><div class="stat-card"><div class="stat-label">کل مصرف</div><div class="stat-val" style="font-size:18px;margin-top:3px">${{esc(d.total_used_fmt)}}</div><div class="stat-sub">همه کانفیگ‌ها</div></div></div>
<div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div><div class="cfg-grid">${{d.links.map((l,i)=>{{const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--green)';const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);return `<div class="cfg-card${{l.active?'':' inactive'}}"><div class="cfg-top"><div class="cfg-head"><div><div class="cfg-label">${{esc(l.label)}}</div><div class="cfg-badges">${{protoChip(l.protocol)}}${{l.connections>0?`<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>`:''}}</div></div><span class="cfg-status ${{l.active?'ok':'no'}}">${{l.active?'<i class="ti ti-circle-check"></i> فعال':'<i class="ti ti-circle-x"></i> غیرفعال'}}</span></div><div class="cfg-usage"><div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div><div class="utxt"><span>${{esc(l.used_fmt)}} مصرف شده</span><span>سهمیه: ${{lim}}</span></div></div></div><div class="cfg-tear"></div><div class="cfg-bottom"><button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})"><span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span><i class="ti ti-chevron-down"></i></button><div class="cfg-vless-wrap" id="vw-${{i}}"><div class="cfg-vless-inner"><div class="cfg-vless">${{esc(l.vless_link)}}</div></div></div><div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(window._VaslZoneLinks[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک</button><button class="btn btn-g" onclick="showQR(window._VaslZoneLinks[${{i}}].label,window._VaslZoneLinks[${{i}}].vless)"><i class="ti ti-qrcode"></i> QR</button></div></div></div>`}}).join('')}}</div>`;setTimeout(()=>autoRefresh(),30000);}}
function copyAllConfigs(){{const links=window._VaslZoneLinks||[];if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}const text=links.map(l=>l.vless).join('\\n');navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));}}
async function autoRefresh(){{try{{const data=await loadData(savedPw);if(!data.locked)renderContent(data);}}catch(e){{}}}}
async function init(){{try{{const data=await loadData();if(data.locked){{renderLock(data.name);return}}renderContent(data);}}catch(e){{document.getElementById('root').innerHTML='<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';}}}}
init();
</script>
</body></html>"""
