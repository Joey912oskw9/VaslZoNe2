from fastapi.responses import HTMLResponse
from urllib.parse import quote

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VaslZone - ورود</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{--bg:#030303;--bg-2:#080808;--red:#dc2626;--red-2:#ef4444;--red-3:#f87171;--red-glow:rgba(220,38,38,0.4);--yellow:#f59e0b;--yellow-2:#fbbf24;--text:#f5f5f5;--text-2:#a3a3a3;--text-3:#525252}
@keyframes bg-pan{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
html,body{height:100%}
body{
  font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--text);
  display:flex;align-items:center;justify-content:center;padding:20px;
  overflow:hidden;
  background:radial-gradient(ellipse 60% 30% at 50% 0%,rgba(220,38,38,0.08),transparent),
             radial-gradient(ellipse 40% 30% at 80% 100%,rgba(245,158,11,0.04),transparent),
             var(--bg);
}
.bg-grid{position:fixed;inset:0;
  background-image:linear-gradient(rgba(220,38,38,0.03) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(220,38,38,0.03) 1px,transparent 1px);
  background-size:40px 40px;z-index:0;pointer-events:none}
</style></head>
<body>
<div class="bg-grid"></div>
<canvas id="fireCanvas" style="position:fixed;inset:0;z-index:0;pointer-events:none"></canvas>
<script>
const c=document.getElementById('fireCanvas'),ctx=c.getContext('2d');
c.width=window.innerWidth;c.height=window.innerHeight;
const particles=[];
class P{
  constructor(){this.reset()}
  reset(){
    this.x=Math.random()*c.width;
    this.y=c.height+10;
    this.size=Math.random()*3+1;
    this.speedY=Math.random()*2+1;
    this.speedX=(Math.random()-0.5)*0.5;
    this.opacity=Math.random()*0.8+0.2;
    this.color=Math.random()>0.5?'#dc2626':'#fbbf24';
  }
  update(){
    this.y-=this.speedY;
    this.x+=this.speedX;
    this.opacity-=0.003;
    if(this.opacity<=0||this.y<-10)this.reset();
  }
  draw(){
    ctx.beginPath();ctx.arc(this.x,this.y,this.size,0,Math.PI*2);
    ctx.fillStyle=this.color;
    ctx.shadowColor=this.color;ctx.shadowBlur=10;
    ctx.globalAlpha=this.opacity;ctx.fill();
    ctx.shadowBlur=0;ctx.globalAlpha=1;
  }
}
for(let i=0;i<100;i++)particles.push(new P());
function animate(){
  ctx.fillStyle='rgba(3,3,3,0.05)';ctx.fillRect(0,0,c.width,c.height);
  particles.forEach(p=>{p.update();p.draw()});
  requestAnimationFrame(animate);
}
animate();
window.addEventListener('resize',()=>{c.width=window.innerWidth;c.height=window.innerHeight});
</script>
<div style="position:relative;z-index:10;width:100%;max-width:400px;animation:fadeIn .8s ease">
  <div style="text-align:center;margin-bottom:32px">
    <div style="width:80px;height:80px;border-radius:24px;margin:0 auto 16px;
      background:linear-gradient(135deg,#7f1d1d,#dc2626,#f59e0b);
      display:flex;align-items:center;justify-content:center;
      font-size:36px;color:#000;box-shadow:0 0 0 4px rgba(220,38,38,0.2),0 16px 40px rgba(220,38,38,0.3);
      position:relative;overflow:hidden">
      <i class="ti ti-crown" style="position:relative;z-index:1"></i>
    </div>
    <div style="font-size:24px;font-weight:900;background:linear-gradient(135deg,#f5f5f5,#fbbf24);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:-.02em">VaslZone</div>
    <div style="font-size:10px;color:var(--text-2);margin-top:6px;letter-spacing:.3em;font-weight:600">GATEWAY v9.3</div>
  </div>
  <div style="background:linear-gradient(145deg,rgba(15,15,15,0.95),rgba(8,8,8,0.95));
    border:1px solid rgba(220,38,38,0.2);border-radius:20px;padding:32px 28px;
    backdrop-filter:blur(20px);position:relative;overflow:hidden;
    box-shadow:0 0 0 1px rgba(220,38,38,0.1),0 20px 60px rgba(0,0,0,0.5)">
    <div style="position:absolute;top:0;left:0;right:0;height:3px;
      background:linear-gradient(90deg,transparent,var(--red),var(--yellow),transparent);border-radius:20px 20px 0 0"></div>
    <div style="text-align:center;margin-bottom:24px">
      <div style="font-size:18px;font-weight:800;color:var(--text);margin-bottom:6px">🔐 ورود</div>
      <div style="font-size:11px;color:var(--text-2);line-height:1.6">برای دسترسی به مجموعه، رمز عبور را وارد کنید</div>
    </div>
    <div id="err" style="display:none;background:rgba(220,38,38,0.12);border:1px solid rgba(220,38,38,0.3);border-radius:10px;padding:10px 14px;margin-bottom:16px;font-size:12px;color:var(--red-3);align-items:center;gap:8px"></div>
    <form id="form">
      <div style="margin-bottom:20px">
        <label style="display:block;font-size:10px;font-weight:700;color:var(--text-2);text-transform:uppercase;letter-spacing:.08em;margin-bottom:7px">رمز عبور</label>
        <div style="position:relative">
          <input id="pw" type="password" placeholder="•••••••••••" autofocus required
            style="width:100%;padding:14px 46px;border-radius:12px;border:1.5px solid rgba(220,38,38,0.15);background:rgba(0,0,0,0.6);color:var(--text);outline:none;font-family:inherit;font-size:14px;transition:all .3s"
            onfocus="this.style.borderColor='var(--red)';this.style.boxShadow='0 0 0 3px rgba(220,38,38,0.15),0 0 30px rgba(220,38,38,0.1)'"
            onblur="this.style.borderColor='rgba(220,38,38,0.15)';this.style.boxShadow='none'">
          <i class="ti ti-lock" style="position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--text-3);font-size:18px"></i>
        </div>
      </div>
      <button id="btn" type="submit"
        style="width:100%;padding:14px;border:none;border-radius:12px;cursor:pointer;
          background:linear-gradient(135deg,#dc2626,#ef4444);color:#fff;font-family:inherit;
          font-size:14px;font-weight:800;display:flex;align-items:center;justify-content:center;gap:8px;
          box-shadow:0 4px 24px rgba(220,38,38,0.4);transition:all .25s;position:relative;overflow:hidden"
        onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 30px rgba(220,38,38,0.5)'"
        onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(220,38,38,0.4)'"
        onmousedown="this.style.transform='scale(0.97)'"
        onmouseup="this.style.transform=''">
        <i class="ti ti-login-2"></i> ورود به پنل
      </button>
    </form>
    <div style="margin-top:16px;padding-top:16px;border-top:1px solid rgba(220,38,38,0.1);
      text-align:center;font-size:10.5px;color:var(--text-3);
      display:flex;align-items:center;justify-content:center;gap:8px">
      <i class="ti ti-brand-telegram" style="color:var(--yellow)"></i>
      <a href="https://t.me/VaslZone" target="_blank" style="color:var(--yellow-2);font-weight:700;text-decoration:none">@VaslZone</a>
    </div>
  </div>
  <div style="text-align:center;margin-top:24px;font-size:9px;color:var(--text-3)">
    VaslZone Gateway v9.3 · 🔥
  </div>
</div>
<style>
@keyframes fadeIn{from{opacity:0;transform:translateY(20px) scale(0.95)}to{opacity:1;transform:translateY(0) scale(1)}}
</style>
<script>
document.getElementById('form').addEventListener('submit',async function(e){
  e.preventDefault();
  var btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.style.display='none';btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite;display:inline-block"></i> در حال ورود...';
  try{
    var r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){var d=await r.json().catch(function(){return {}});throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    err.style.display='flex';err.innerHTML='<i class="ti ti-alert-triangle"></i><span>'+e.message+'</span>';
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به پنل';
  }
});
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VaslZone · پنل مدیریت</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --bg:#030303;--bg-2:#080808;--bg-3:#0c0c0c;
  --card:#0e0e0e;--card-2:#121212;--card-3:#181818;
  --red:#dc2626;--red-2:#ef4444;--red-3:#f87171;
  --red-glow:rgba(220,38,38,0.15);--red-dim:rgba(220,38,38,0.10);
  --yellow:#f59e0b;--yellow-2:#fbbf24;--yellow-3:#fde047;
  --green:#22c55e;--green-glow:rgba(34,197,94,0.15);
  --text:#f5f5f5;--text-2:#a3a3a3;--text-3:#525252;
  --border:rgba(220,38,38,0.08);--border-2:rgba(220,38,38,0.20);
  --grad-fire:linear-gradient(135deg,#7f1d1d 0%,#dc2626 50%,#f59e0b 100%);
  --grad-red:linear-gradient(135deg,#dc2626,#ef4444);
  --shadow:0 8px 32px rgba(0,0,0,0.6);
  --radius:14px;--radius-l:20px;
}
::-webkit-scrollbar{width:6px;background:var(--bg-2)}
::-webkit-scrollbar-thumb{background:var(--red);border-radius:3px}
html,body{height:100%}
body{
  font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--text);
  direction:rtl;overflow-x:hidden;font-size:14px;
  background:radial-gradient(ellipse 60% 30% at 80% 0%,rgba(220,38,38,0.06),transparent),
             radial-gradient(ellipse 50% 25% at 20% 100%,rgba(245,158,11,0.04),transparent),
             var(--bg);
}
.grid-bg{position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(220,38,38,0.02) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(220,38,38,0.02) 1px,transparent 1px);
  background-size:50px 50px}
DASHBOARD_HTML = DASHBOARD_HTML + r"""
/* ───── نوار بالا ───── */
.top-bar{
  position:fixed;top:0;left:0;right:0;height:56px;z-index:100;
  background:linear-gradient(180deg,rgba(8,8,8,0.98),rgba(8,8,8,0.9));
  backdrop-filter:blur(16px);border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;padding:0 20px}
.top-bar-logo{display:flex;align-items:center;gap:10px}
.top-bar-logo .tb-icon{width:32px;height:32px;border-radius:10px;
  background:var(--grad-fire);display:flex;align-items:center;
  justify-content:center;color:#000;font-size:16px;box-shadow:0 0 12px rgba(220,38,38,0.3)}
.top-bar-logo .tb-name{font-size:14px;font-weight:800;
  background:linear-gradient(90deg,var(--text),var(--yellow-2));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent}
.top-bar-left{display:flex;align-items:center;gap:12px}
.top-bar-btn{width:34px;height:34px;border-radius:9px;border:1px solid var(--border);
  background:var(--card-2);color:var(--text-2);display:flex;align-items:center;
  justify-content:center;font-size:16px;cursor:pointer;transition:.2s}
.top-bar-btn:hover{background:var(--red-dim);color:var(--red-3);border-color:var(--red)}

/* ───── منوی اصلی ───── */
.main-wrap{display:flex;padding-top:56px;min-height:100vh;position:relative;z-index:1}

/* ───── سایدبار چپ ───── */
.sidebar{
  width:220px;flex-shrink:0;background:linear-gradient(180deg,var(--card-2),var(--card));
  border-left:1px solid var(--border);min-height:calc(100vh - 56px);
  padding:12px 8px;position:sticky;top:56px;height:calc(100vh - 56px);overflow-y:auto}
.sidebar-section{font-size:9px;font-weight:700;color:var(--red-3);padding:14px 12px 4px;
  text-transform:uppercase;letter-spacing:.12em;display:flex;align-items:center;gap:6px}
.sidebar-section::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,var(--border),transparent)}
.nav-item{
  display:flex;align-items:center;gap:10px;padding:9px 12px;margin:2px 0;
  border-radius:10px;color:var(--text-2);font-size:12.5px;cursor:pointer;
  transition:all .2s ease;border-right:2px solid transparent}
.nav-item:hover{background:var(--red-dim);color:var(--text)}
.nav-item.active{background:linear-gradient(90deg,rgba(220,38,38,0.15),transparent);
  color:var(--text);border-right-color:var(--red);font-weight:700}
.nav-item i{font-size:17px;width:20px;text-align:center}
.nav-item.active i{color:var(--red-3)}
.nav-item .badge{font-size:9px;padding:2px 7px;border-radius:20px;background:var(--red-dim);
  border:1px solid var(--border-2);color:var(--red-3);font-weight:700;margin-right:auto}

/* ───── محتوا ───── */
.content{flex:1;padding:24px;min-width:0;position:relative}
.page{display:none;animation:pageIn .35s ease}
.page.active{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}

/* ───── کارت‌ها ───── */
.card{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:var(--radius);
  padding:18px 20px;position:relative;overflow:hidden;transition:all .25s}
.card:hover{border-color:var(--border-2)}
.card-title{font-size:13px;font-weight:800;margin-bottom:14px;display:flex;align-items:center;gap:8px}
.card-title i{color:var(--red-3)}
.row-2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}
.row-3{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:16px}

/* ───── متریک کارت ───── */
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.metric-card{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);position:relative;overflow:hidden;
  padding:18px 18px 14px;border-radius:14px;transition:all .25s;cursor:default}
.metric-card:hover{transform:translateY(-3px);border-color:var(--border-2);box-shadow:0 12px 28px rgba(0,0,0,0.4)}
.metric-card::before{content:'';position:absolute;top:0;right:0;width:60px;height:60px;
  background:radial-gradient(circle,rgba(220,38,38,0.08),transparent 70%);pointer-events:none}
.metric-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--red),transparent);
  transform:scaleX(0);transition:transform .3s}
.metric-card:hover::after{transform:scaleX(1)}
.metric-icon{width:36px;height:36px;border-radius:10px;margin-bottom:12px;
  display:flex;align-items:center;justify-content:center;font-size:18px;
  background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)}
.metric-label{font-size:9.5px;color:var(--text-2);font-weight:600;text-transform:uppercase;letter-spacing:.07em;margin-bottom:5px}
.metric-value{font-size:26px;font-weight:800;color:var(--text);line-height:1}
.metric-value .u{font-size:12px;font-weight:500;color:var(--text-2)}
.metric-sub{font-size:9.5px;color:var(--text-2);margin-top:6px;display:flex;align-items:center;gap:4px}
.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite;box-shadow:0 0 6px var(--green)}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}

@media(max-width:1000px){.metrics{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.metrics{grid-template-columns:1fr}}

/* ───── دکمه‌ها ───── */
.btn{font-family:inherit;font-size:12px;font-weight:700;border-radius:10px;
  padding:9px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;
  transition:all .2s;white-space:nowrap;border:none}
.btn i{font-size:14px}
.btn-primary{background:var(--grad-red);color:#fff;box-shadow:0 4px 20px rgba(220,38,38,0.35)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 26px rgba(220,38,38,0.45)}
.btn-outline{background:transparent;border:1.5px solid var(--border-2);color:var(--text-2)}
.btn-outline:hover{background:var(--red-dim);border-color:var(--red);color:var(--text)}
.btn-danger{background:var(--red-dim);border:1.5px solid var(--border-2);color:var(--red-3)}
.btn-danger:hover{background:rgba(220,38,38,0.2)}
.btn-sm{padding:6px 12px;font-size:10.5px;border-radius:8px}
.btn-icon{width:32px;height:32px;padding:0;justify-content:center;border-radius:8px}

/* ───── تاگل ───── */
.tog{width:40px;height:20px;border-radius:20px;
  background:rgba(100,100,100,0.25);position:relative;cursor:pointer;
  transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:14px;height:14px;border-radius:50%;
  background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 2px 4px rgba(0,0,0,.4)}
.tog.on{background:var(--grad-red)}
.tog.on::after{left:23px}

/* ───── فرم ───── */
.input{width:100%;padding:9px 13px;border-radius:9px;border:1px solid var(--border);
  background:rgba(0,0,0,0.4);color:var(--text);font-family:inherit;font-size:12px;
  outline:none;transition:.15s}
.input:focus{border-color:var(--red);box-shadow:0 0 0 3px var(--red-dim);background:rgba(0,0,0,0.6)}
.input::placeholder{color:var(--text-3)}

/* ───── کارت کانفیگ ───── */
.cfg-list{display:flex;flex-direction:column;gap:10px}
.cfg-card{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:14px;padding:14px 16px;
  transition:all .25s;position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--border-2);transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.35)}
.cfg-card.is-off{opacity:.6}
.cfg-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:10px;flex-wrap:wrap}
.cfg-label{font-size:14px;font-weight:700;color:var(--text);display:flex;align-items:center;gap:6px}
.cfg-status{width:8px;height:8px;border-radius:50%;flex-shrink:0;
  background:var(--green);box-shadow:0 0 0 3px var(--green-glow)}
.cfg-card.is-off .cfg-status{background:var(--text-3);box-shadow:none}
.cfg-usage{margin-bottom:8px}
.cfg-bar{height:5px;border-radius:4px;background:rgba(220,38,38,0.08);overflow:hidden}
.cfg-bar-fill{height:100%;border-radius:4px;transition:width .5s}
.cfg-utxt{font-size:9.5px;color:var(--text-2);display:flex;justify-content:space-between;margin-top:4px}
.cfg-row2{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.proto-badge{font-size:8.5px;padding:3px 8px;border-radius:5px;font-weight:700;white-space:nowrap}
.proto-vless{background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)}
.proto-xhttp{background:rgba(168,85,247,0.1);color:#c084fc;border:1px solid rgba(168,85,247,0.2)}
.proto-trojan{background:rgba(245,158,11,0.1);color:var(--yellow-2);border:1px solid rgba(245,158,11,0.25)}

/* ───── کارت‌های گروه ساب ───── */
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px;margin-bottom:18px}
.sub-card{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:16px;padding:16px 18px;transition:all .25s}
.sub-card:hover{border-color:var(--border-2);transform:translateY(-3px);box-shadow:0 12px 30px rgba(0,0,0,.35)}
.sub-head{display:flex;align-items:flex-start;gap:12px;margin-bottom:12px}
.sub-icon{width:40px;height:40px;border-radius:12px;
  background:linear-gradient(135deg,rgba(168,85,247,0.2),rgba(168,85,247,0.05));
  display:flex;align-items:center;justify-content:center;color:#c084fc;font-size:18px;border:1px solid rgba(168,85,247,0.2)}
.sub-name{font-size:15px;font-weight:800;color:var(--text)}
.sub-desc{font-size:10px;color:var(--text-2);margin-top:2px}
.sub-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:10px;
  background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;padding:10px}
.sub-stat{text-align:center}
.sub-stat-val{font-size:15px;font-weight:800;color:var(--text)}
.sub-stat-label{font-size:8px;color:var(--text-2);margin-top:3px;text-transform:uppercase;letter-spacing:.05em}
.sub-url{font-family:monospace;font-size:9.5px;color:#c084fc;word-break:break-all;background:rgba(0,0,0,0.3);padding:8px 10px;border-radius:8px;border:1px dashed rgba(168,85,247,0.2);margin-bottom:10px;display:flex;align-items:center;gap:8px}
.sub-actions{display:flex;gap:6px;flex-wrap:wrap}

/* ───── لگ ───── */
.log-item{display:flex;gap:11px;padding:9px 0;border-bottom:1px solid rgba(220,38,38,0.04)}
.log-ic{width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:rgba(16,185,129,0.1);color:var(--green);border:1px solid rgba(16,185,129,0.2)}
.log-ic.err{background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)}
.log-ic.warn{background:rgba(245,158,11,0.1);color:var(--yellow);border:1px solid rgba(245,158,11,0.2)}
.log-msg{font-size:12px;color:var(--text);line-height:1.5}
.log-time{font-size:9px;color:var(--text-2);margin-top:2px}

/* ───── سرور ───── */
.srv-card{background:linear-gradient(155deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:18px;padding:0;overflow:hidden}
.srv-head{display:flex;align-items:center;gap:14px;padding:20px 22px;border-bottom:1px solid var(--border);
  background:linear-gradient(90deg,rgba(220,38,38,0.08),transparent)}
.srv-icon{width:48px;height:48px;border-radius:14px;background:var(--grad-fire);
  display:flex;align-items:center;justify-content:center;color:#000;font-size:22px}
.srv-name{font-size:15px;font-weight:800;color:var(--text)}
.srv-domain{font-size:11px;color:var(--text-2);margin-top:2px;word-break:break-all}
.srv-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:18px 22px 20px}
.srv-item{display:flex;align-items:center;gap:10px;padding:10px 12px;background:rgba(0,0,0,0.3);
  border:1px solid var(--border);border-radius:10px}
.srv-item-icon{width:30px;height:30px;border-radius:8px;background:var(--red-dim);
  color:var(--red-3);display:flex;align-items:center;justify-content:center;font-size:15px}
.srv-item-label{font-size:9px;color:var(--text-2);text-transform:uppercase;letter-spacing:.05em}
.srv-item-val{font-size:11.5px;font-weight:700;color:var(--text);margin-top:2px}

/* ───── پنل رمز ───── */
.pw-card{background:linear-gradient(155deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:18px;padding:22px}
.pw-input{width:100%;padding:10px 14px;border-radius:10px;border:1px solid var(--border);
  background:rgba(0,0,0,0.3);color:var(--text);font-family:inherit;font-size:12px;outline:none}
.pw-input:focus{border-color:#a855f7;box-shadow:0 0 0 3px rgba(168,85,247,0.1)}

/* ───── مودال ───── */
.modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.7);
  z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}
.modal-overlay.open{display:flex}
.modal-box{background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border-2);border-radius:18px;padding:0;max-width:480px;
  width:calc(100% - 32px);max-height:90vh;overflow-y:auto;box-shadow:0 24px 60px rgba(0,0,0,0.5)}

/* ───── تاست ───── */
.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(60px);
  background:linear-gradient(145deg,var(--card-2),var(--card));border:1px solid var(--border-2);
  color:var(--text);border-radius:12px;padding:10px 18px;font-size:12px;font-weight:700;
  opacity:0;transition:all .3s;z-index:9999;pointer-events:none;white-space:nowrap;
  box-shadow:0 12px 32px rgba(0,0,0,0.5)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,0.3);background:linear-gradient(145deg,rgba(16,185,129,0.15),var(--card))}

/* ───── سایر ───── */
.mb16{margin-bottom:16px}
.empty{text-align:center;padding:50px 20px;color:var(--text-2)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.footer{padding-top:16px;border-top:1px solid var(--border);margin-top:18px;
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px}
.footer-text{font-size:10px;color:var(--text-2)}
.footer-link{color:var(--yellow);font-weight:700;text-decoration:none;font-size:11px}

@media(max-width:900px){
  .sidebar{position:fixed;bottom:0;left:0;right:0;width:100%;height:auto;top:auto;padding:0;
    display:flex;z-index:200;overflow-x:auto;gap:4px;padding:6px 8px;
    background:var(--card-2);border-top:1px solid var(--border);
    border-left:none;min-height:auto}
  .sidebar-section{display:none}
  .nav-item{flex-direction:column;padding:6px 8px;font-size:9px;gap:3px;flex-shrink:0;min-width:0}
  .nav-item i{font-size:18px}
  .nav-item .badge{display:none}
  .content{padding:16px 12px 80px}
  .row-2,.row-3{grid-template-columns:1fr}
}
@media(max-width:560px){
  .metrics{grid-template-columns:1fr 1fr}
  .sub-grid{grid-template-columns:1fr}
  .srv-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div class="grid-bg"></div>
<div class="toast" id="toast"></div>

<div class="top-bar">
  <div class="top-bar-logo">
    <div class="tb-icon"><i class="ti ti-crown"></i></div>
    <span class="tb-name">VaslZone</span>
  </div>
  <div class="top-bar-left">
    <button class="top-bar-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i></button>
    <button class="top-bar-btn" id="logout-btn" title="خروج"><i class="ti ti-logout"></i></button>
  </div>
</div>

<div class="main-wrap">
<div class="sidebar" id="sidebar">
  <div class="sidebar-section">منو</div>
  <div class="nav-item active" data-page="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
  <div class="nav-item" data-page="links"><i class="ti ti-link"></i> کانفیگ‌ها <span class="badge" id="links-nb">0</span></div>
  <div class="nav-item" data-page="subs"><i class="ti ti-folders"></i> گروه‌ها <span class="badge" id="subs-nb">0</span></div>
  <div class="nav-item" data-page="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
  <div class="nav-item" data-page="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
  <div class="nav-item" data-page="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="badge" id="conns-nb">0</span></div>
  <div class="sidebar-section">سیستم</div>
  <div class="nav-item" data-page="resellers"><i class="ti ti-users"></i> نمایندگان<span class="badge" id="res-nb">0</span></div>
  <div class="nav-item" data-page="security"><i class="ti ti-shield-lock"></i> امنیت</div>
  <div class="nav-item" data-page="logs"><i class="ti ti-history"></i> لاگ‌ها</div>
  <div class="nav-item" data-page="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
  <div class="nav-item" data-page="settings"><i class="ti ti-settings"></i> تنظیمات</div>
</div>

<div class="content">
"""
DASHBOARD_HTML = DASHBOARD_HTML + r"""
<div class="page active" id="page-overview">
  <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:20px">
    <div>
      <div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px">
        <i class="ti ti-dashboard" style="color:var(--red-3)"></i> داشبورد
      </div>
      <div id="last-upd" style="font-size:11px;color:var(--text-2);margin-top:4px">در حال بارگذاری...</div>
    </div>
    <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
      <span class="btn btn-sm" style="background:rgba(22,163,74,0.12);color:var(--green);border:1px solid rgba(22,163,74,0.25)"><span class="dot"></span> فعال</span>
      <span class="btn btn-sm btn-outline" id="uptime-badge">—</span>
      <button class="btn btn-primary btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric-card">
      <div class="metric-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="metric-label">اتصالات فعال</div>
      <div class="metric-value" id="m-conns">—</div>
      <div class="metric-sub"><span class="dot"></span> WebSocket</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon" style="background:rgba(16,185,129,0.1);color:var(--green);border-color:rgba(16,185,129,0.2)"><i class="ti ti-transfer"></i></div>
      <div class="metric-label">کل ترافیک</div>
      <div class="metric-value" id="m-traffic">— <span class="u">MB</span></div>
      <div class="metric-sub">از راه‌اندازی</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon" style="background:rgba(239,68,68,0.1);color:var(--red-3);border-color:var(--border-2)"><i class="ti ti-link"></i></div>
      <div class="metric-label">کانفیگ فعال</div>
      <div class="metric-value" id="m-alinks">—</div>
      <div class="metric-sub" id="m-lsub">از کل</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon" style="background:rgba(168,85,247,0.1);color:#c084fc;border-color:rgba(168,85,247,0.2)"><i class="ti ti-folders"></i></div>
      <div class="metric-label">گروه‌های ساب</div>
      <div class="metric-value" id="m-subs">—</div>
      <div class="metric-sub">فعال</div>
    </div>
  </div>
  <div class="card" style="margin-bottom:18px">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:12px">
      <div style="font-size:11px;color:var(--red-3);font-weight:700;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em"><i class="ti ti-link" style="color:var(--red);font-size:15px"></i> لینک پیش‌فرض</div>
      <span class="badge" style="font-size:9px;padding:3px 10px;border-radius:20px;background:rgba(245,158,11,0.1);color:var(--yellow);border:1px solid rgba(245,158,11,0.25)">TLS 443 · WS</span>
    </div>
    <div id="vless-main" style="background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:10px;padding:12px 14px;font-family:monospace;font-size:10.5px;color:var(--yellow-2);word-break:break-all;line-height:1.7;direction:ltr;text-align:left">در حال دریافت...</div>
    <div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
      <button class="btn btn-primary btn-sm" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-outline btn-sm" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-outline btn-sm" onclick="navTo('links')"><i class="ti ti-link"></i> کانفیگ محدود</button>
    </div>
  </div>
  <div class="row-3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div style="height:220px"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div><div style="height:180px"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="row-2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
      <div style="display:flex;justify-content:space-between;font-size:12px;padding:7px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);display:flex;align-items:center;gap:5px"><i class="ti ti-shield-check" style="font-size:13px;color:var(--text-2)"></i> UUID Auth</span><span style="color:var(--green);font-weight:700">● فعال</span></div>
      <div style="display:flex;justify-content:space-between;font-size:12px;padding:7px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check" style="font-size:13px;color:var(--text-2)"></i> VLESS / WS</span><span style="color:var(--green);font-weight:700">● فعال</span></div>
      <div style="display:flex;justify-content:space-between;font-size:12px;padding:7px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);display:flex;align-items:center;gap:5px"><i class="ti ti-bolt" style="font-size:13px;color:var(--text-2)"></i> XHTTP Ultra</span><span style="color:var(--green);font-weight:700">● فعال</span></div>
      <div style="display:flex;justify-content:space-between;font-size:12px;padding:7px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);display:flex;align-items:center;gap:5px"><i class="ti ti-clock" style="font-size:13px;color:var(--text-2)"></i> آپتایم</span><span style="font-weight:700" id="uptime-inline">—</span></div>
      <div style="padding:7px 0">
        <div style="display:flex;justify-content:space-between;margin-bottom:5px"><span style="color:var(--text-2);display:flex;align-items:center;gap:5px;font-size:12px"><i class="ti ti-gauge" style="font-size:13px;color:var(--text-2)"></i> بار نسبی</span><span style="font-size:12px;font-weight:700" id="bw-pct">—%</span></div>
        <div style="height:5px;border-radius:4px;background:rgba(220,38,38,0.08);overflow:hidden"><div style="height:100%;width:0%;background:var(--grad-red);border-radius:4px;transition:width .6s" id="bw-bar"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="badge" style="margin-right:auto;font-size:9px;padding:2px 8px;border-radius:20px;background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)" id="lsummary-badge">0</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="footer">
    <span class="footer-text">VaslZone Gateway v9.3 · Railway Cloud</span>
    <a class="footer-link" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
  </div>
</div>

<div class="page" id="page-links">
  <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:18px">
    <div>
      <div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px"><i class="ti ti-link" style="color:var(--red-3)"></i> کانفیگ‌ها</div>
      <div style="font-size:11px;color:var(--text-2);margin-top:4px">ساخت و مدیریت</div>
    </div>
    <span class="badge" style="font-size:10px;padding:4px 12px;border-radius:20px;background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)" id="links-pg-cnt">۰ کانفیگ</span>
  </div>
  <div class="card" style="margin-bottom:16px">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
      <div style="width:40px;height:40px;border-radius:11px;background:var(--grad-fire);display:flex;align-items:center;justify-content:center;color:#000;font-size:20px"><i class="ti ti-fire"></i></div>
      <div><div style="font-size:14px;font-weight:800;color:var(--text)">کانفیگ جدید</div><div style="font-size:10px;color:var(--text-2)">UUID تصادفی · سهمیه، انقضا و پروتکل</div></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
      <div style="background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;padding:12px 14px">
        <div style="font-size:9px;font-weight:700;color:var(--red-3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px"><i class="ti ti-id" style="font-size:12px"></i> شناسه</div>
        <input class="input" id="nl-label" placeholder="مثلاً: کاربر علی">
        <input class="input" id="nl-note" placeholder="یادداشت" style="margin-top:7px">
      </div>
      <div style="background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;padding:12px 14px">
        <div style="font-size:9px;font-weight:700;color:var(--red-3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px"><i class="ti ti-calendar" style="font-size:12px"></i> انقضا</div>
        <input class="input" id="nl-exp" type="number" min="0" placeholder="روز · 0 = نامحدود">
      </div>
    </div>
    <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap">
      <div style="flex:1;min-width:150px;background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;padding:12px 14px">
        <div style="font-size:9px;font-weight:700;color:var(--red-3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px"><i class="ti ti-gauge" style="font-size:12px"></i> سهمیه</div>
        <div style="display:flex;gap:7px">
          <input class="input" id="nl-val" type="number" min="0" step="0.1" placeholder="0 ∞">
          <select class="input" id="nl-unit" style="max-width:80px"><option value="MB">MB</option><option value="GB">GB</option></select>
        </div>
      </div>
      <div style="flex:1;min-width:150px;background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;padding:12px 14px">
        <div style="font-size:9px;font-weight:700;color:var(--red-3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px"><i class="ti ti-server" style="font-size:12px"></i> IP / پورت</div>
        <input class="input" id="nl-ips" placeholder="1.1.1.1,2.2.2.2">
        <input class="input" id="nl-port" type="number" placeholder="443" style="margin-top:6px">
      </div>
    </div>
    <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap;align-items:flex-end">
      <div style="background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;padding:10px 12px">
        <div style="font-size:9px;font-weight:700;color:var(--red-3);margin-bottom:6px">پروتکل</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WS</option>
          <option value="trojan-ws">Trojan / WS</option>
        </select>
        <div style="display:flex;gap:6px">
          <div class="proto-btn active" data-val="vless-ws" onclick="selProto('vless-ws',this)">VLESS</div>
          <div class="proto-btn" data-val="trojan-ws" onclick="selProto('trojan-ws',this)">Trojan</div>
        </div>
      </div>
      <div style="background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;padding:10px 12px">
        <div style="font-size:9px;font-weight:700;color:var(--red-3);margin-bottom:6px">گروه ساب</div>
        <select class="input" id="nl-sub" style="padding:8px"><option value="">بدون گروه</option></select>
      </div>
      <div style="flex:0.5">
        <input class="input" id="nl-count" type="number" value="1" min="1" style="padding:8px;text-align:center">
      </div>
    </div>
    <style>.proto-btn{padding:7px 14px;border:1.5px solid var(--border-2);border-radius:8px;font-size:11px;font-weight:700;color:var(--text-2);cursor:pointer;transition:.15s;font-family:inherit}.proto-btn:hover{background:var(--red-dim);border-color:var(--red)}.proto-btn.active{background:var(--grad-red);color:#fff;border-color:var(--red);box-shadow:0 4px 14px rgba(220,38,38,0.35)}</style>
    <button class="btn btn-primary" onclick="createLink()" style="margin-top:4px"><i class="ti ti-fire"></i> ساخت کانفیگ</button>
  </div>
  <div class="cfg-list" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>
</div>

<div class="page" id="page-subs">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:10px">
    <div><div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px"><i class="ti ti-folders" style="color:#c084fc"></i> گروه‌های ساب</div></div>
    <div style="display:flex;gap:8px">
      <span class="badge" style="font-size:10px;padding:4px 12px;border-radius:20px;background:rgba(168,85,247,0.1);color:#c084fc;border:1px solid rgba(168,85,247,0.2)" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-sm" style="background:rgba(168,85,247,0.15);color:#c084fc;border:1px solid rgba(168,85,247,0.25)" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> جدید</button>
    </div>
  </div>
  <div class="sub-grid" id="subs-grid"><div class="empty" style="grid-column:1/-1"><i class="ti ti-folders"></i><p>گروهی وجود ندارد</p></div></div>
</div>

<div class="page" id="page-traffic">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;flex-wrap:wrap;gap:10px">
    <div><div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px"><i class="ti ti-chart-area" style="color:var(--red-3)"></i> ترافیک</div></div>
    <button class="btn btn-primary btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
  </div>
  <div class="metrics" style="margin-bottom:16px">
    <div class="metric-card"><div class="metric-icon"><i class="ti ti-database"></i></div><div class="metric-label">کل مصرف</div><div class="metric-value" id="t-traffic">—</div></div>
    <div class="metric-card"><div class="metric-icon" style="background:rgba(245,158,11,0.1);color:var(--yellow);border-color:rgba(245,158,11,0.25)"><i class="ti ti-chart-bar"></i></div><div class="metric-label">میانگین ساعتی</div><div class="metric-value" id="t-avg">—</div></div>
    <div class="metric-card"><div class="metric-icon" style="background:rgba(168,85,247,0.1);color:#c084fc;border-color:rgba(168,85,247,0.2)"><i class="ti ti-clock"></i></div><div class="metric-label">پیک مصرف</div><div class="metric-value" id="t-peak">—</div></div>
    <div class="metric-card"><div class="metric-icon" style="background:rgba(16,185,129,0.1);color:var(--green);border-color:rgba(16,185,129,0.2)"><i class="ti ti-trending-down"></i></div><div class="metric-label">کمترین مصرف</div><div class="metric-value" id="t-low">—</div></div>
  </div>
  <div class="card"><div class="card-title"><i class="ti ti-activity"></i> روند مصرف</div><div style="height:280px"><canvas id="ch3"></canvas></div></div>
</div>

<div class="page" id="page-connections">
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:16px">
    <div><div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px"><i class="ti ti-plug-connected" style="color:var(--green)"></i> اتصالات فعال</div></div>
    <div style="display:flex;gap:8px">
      <span class="badge" style="font-size:10px;padding:4px 12px;border-radius:20px;background:rgba(16,185,129,0.1);color:var(--green);border:1px solid rgba(16,185,129,0.2)" id="conns-live">—</span>
    </div>
  </div>
  <div class="metrics" style="margin-bottom:16px">
    <div class="metric-card"><div class="metric-icon" style="background:rgba(16,185,129,0.1);color:var(--green);border-color:rgba(16,185,129,0.2)"><i class="ti ti-plug-connected"></i></div><div class="metric-label">اتصالات</div><div class="metric-value" id="ch-count">—</div></div>
    <div class="metric-card"><div class="metric-icon" style="background:rgba(245,158,11,0.1);color:var(--yellow);border-color:rgba(245,158,11,0.25)"><i class="ti ti-transfer"></i></div><div class="metric-label">ترافیک لحظه</div><div class="metric-value" id="ch-traffic">—</div></div>
    <div class="metric-card"><div class="metric-icon" style="background:rgba(168,85,247,0.1);color:#c084fc;border-color:rgba(168,85,247,0.2)"><i class="ti ti-clock"></i></div><div class="metric-label">میانگین مدت</div><div class="metric-value" id="ch-avgdur">—</div></div>
    <div class="metric-card"><div class="metric-icon" style="background:rgba(16,185,129,0.1);color:var(--green);border-color:rgba(16,185,129,0.2)"><i class="ti ti-map-pin"></i></div><div class="metric-label">IP یکتا</div><div class="metric-value" id="ch-uniq">—</div></div>
  </div>
  <div class="cfg-list" id="conns-grid"></div>
  <div class="empty" id="conns-empty" style="display:none"><i class="ti ti-plug-off"></i><p>هیچ اتصالی نیست</p></div>
</div>

<div class="page" id="page-resellers">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:10px">
    <div><div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px"><i class="ti ti-users" style="color:#c084fc"></i> نمایندگان</div></div>
    <button class="btn btn-sm" style="background:rgba(168,85,247,0.15);color:#c084fc;border:1px solid rgba(168,85,247,0.25)" onclick="openModal('modal-res')"><i class="ti ti-user-plus"></i> جدید</button>
  </div>
  <div class="card"><div id="res-list">بارگذاری...</div></div>
</div>

<div class="page" id="page-security">
  <div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px;margin-bottom:18px"><i class="ti ti-shield-lock" style="color:var(--red-3)"></i> امنیت</div>
  <div class="row-2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);font-size:12px">TLS/HTTPS</span><span style="color:var(--green);font-size:12px;font-weight:700">● فعال (443)</span></div>
      <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);font-size:12px">Fingerprint</span><span style="font-size:12px;font-weight:700">Chrome Spoof</span></div>
      <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);font-size:12px">هش رمز</span><span style="font-size:12px;font-weight:700">SHA-256+Salt</span></div>
      <div style="display:flex;justify-content:space-between;padding:8px 0"><span style="color:var(--text-2);font-size:12px">سشن</span><span style="font-size:12px;font-weight:700">HttpOnly · ۷ روز</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);font-size:12px">UUID Auth</span><span style="color:var(--green);font-size:12px;font-weight:700">● فعال</span></div>
      <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);font-size:12px">فعال/غیرفعال</span><span style="color:var(--green);font-size:12px;font-weight:700">● فعال</span></div>
      <div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(220,38,38,0.04)"><span style="color:var(--text-2);font-size:12px">سهمیه ترافیک</span><span style="color:var(--green);font-size:12px;font-weight:700">● فعال</span></div>
      <div style="display:flex;justify-content:space-between;padding:8px 0"><span style="color:var(--text-2);font-size:12px">رمز پابلیک</span><span style="color:var(--green);font-size:12px;font-weight:700">● اختیاری</span></div>
    </div>
  </div>
</div>

<div class="page" id="page-logs">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:10px">
    <div><div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px"><i class="ti ti-history" style="color:var(--red-3)"></i> لاگ فعالیت‌ها</div></div>
    <button class="btn btn-primary btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button>
  </div>
  <div class="card"><div id="logs-list">—</div></div>
</div>

<div class="page" id="page-errors">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:10px">
    <div><div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px"><i class="ti ti-alert-triangle" style="color:var(--red-3)"></i> خطاها</div></div>
    <span class="badge" style="font-size:10px;padding:4px 12px;border-radius:20px;background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)" id="errs-badge">0</span>
  </div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div>
</div>

<div class="page" id="page-settings">
  <div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px;margin-bottom:18px"><i class="ti ti-settings" style="color:var(--red-3)"></i> تنظیمات</div>
  <div class="row-2">
    <div class="srv-card">
      <div class="srv-head">
        <div class="srv-icon"><i class="ti ti-server-2"></i></div>
        <div><div class="srv-name">اطلاعات سرور</div><div class="srv-domain" id="set-host">—</div></div>
      </div>
      <div class="srv-grid">
        <div class="srv-item"><div class="srv-item-icon"><i class="ti ti-route"></i></div><div><div class="srv-item-label">پورت</div><div class="srv-item-val">443 (TLS)</div></div></div>
        <div class="srv-item"><div class="srv-item-icon"><i class="ti ti-versions"></i></div><div><div class="srv-item-label">نسخه</div><div class="srv-item-val">v9.3</div></div></div>
        <div class="srv-item"><div class="srv-item-icon"><i class="ti ti-brand-fastapi"></i></div><div><div class="srv-item-label">پلتفرم</div><div class="srv-item-val">FastAPI</div></div></div>
        <div class="srv-item"><div class="srv-item-icon"><i class="ti ti-cloud"></i></div><div><div class="srv-item-label">هاست</div><div class="srv-item-val">Railway</div></div></div>
      </div>
    </div>
    <div class="pw-card">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
        <div style="width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,#a855f7,#7e22ce);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px"><i class="ti ti-key"></i></div>
        <div><div style="font-size:14px;font-weight:800;color:var(--text)">تغییر رمز</div><div style="font-size:10px;color:var(--text-2)">رمز قوی انتخاب کنید</div></div>
      </div>
      <input class="pw-input" id="cp-cur" type="password" placeholder="رمز فعلی" style="margin-bottom:8px">
      <input class="pw-input" id="cp-new" type="password" placeholder="رمز جدید" style="margin-bottom:8px">
      <input class="pw-input" id="cp-cf" type="password" placeholder="تکرار رمز جدید" style="margin-bottom:12px">
      <button class="btn btn-primary" onclick="changePw()" style="width:100%;justify-content:center"><i class="ti ti-shield-check"></i> ذخیره رمز</button>
    </div>
  </div>
</div>

<div class="page" id="page-subscriptions">
  <div style="font-size:20px;font-weight:800;display:flex;align-items:center;gap:8px;margin-bottom:18px"><i class="ti ti-rss" style="color:var(--red-3)"></i> سابسکریپشن</div>
  <div class="row-2">
    <div class="card"><div class="card-title"><i class="ti ti-rss"></i> ساب تکی</div><p style="font-size:11px;color:var(--text-2);line-height:1.7">هر کانفیگ URL جدا دارد. از کارت کانفیگ کپی کنید.</p></div>
    <div class="card"><div class="card-title"><i class="ti ti-database"></i> ساب کامل</div>
      <div style="background:rgba(0,0,0,0.3);padding:10px;border-radius:8px;border:1px solid var(--border);display:flex;align-items:center;gap:8px;margin-bottom:10px">
        <span id="sub-all-url" style="font-family:monospace;font-size:10px;color:var(--yellow-2);flex:1;word-break:break-all">—</span>
        <button class="btn btn-outline btn-sm" onclick="cpSubAll()"><i class="ti ti-copy"></i></button>
      </div>
      <div style="font-size:10px;color:var(--text-2);background:rgba(245,158,11,0.1);padding:8px 10px;border-radius:8px;border:1px solid rgba(245,158,11,0.2)"><i class="ti ti-alert-triangle" style="color:var(--yellow);font-size:12px"></i> فقط با کوکی سشن کار می‌کند.</div>
    </div>
  </div>
  <div class="card"><div class="card-title"><i class="ti ti-folders"></i> لینک ساب گروه‌ها</div><div id="sub-groups-list">در حال بارگذاری...</div></div>
</div>
</div>
</div>

<!-- modals -->
<div class="modal-overlay" id="modal-create-sub">
  <div class="modal-box" style="padding:22px">
    <div style="text-align:center;margin-bottom:16px">
      <div style="width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg,#a855f7,#7e22ce);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;margin:0 auto 10px"><i class="ti ti-folder-plus"></i></div>
      <div style="font-size:15px;font-weight:800">ساخت گروه جدید</div>
    </div>
    <input class="input" id="ns-name" placeholder="نام گروه" style="margin-bottom:8px">
    <input class="input" id="ns-desc" placeholder="توضیحات (اختیاری)" style="margin-bottom:8px">
    <input class="input" id="ns-pw" type="password" placeholder="رمز صفحه پابلیک (اختیاری)" style="margin-bottom:14px">
    <div style="display:flex;gap:8px">
      <button class="btn btn-outline" onclick="closeModal('modal-create-sub')" style="flex:1;justify-content:center">انصراف</button>
      <button class="btn btn-primary" onclick="createSub()" style="flex:1;justify-content:center"><i class="ti ti-folder-plus"></i> ساخت</button>
    </div>
  </div>
</div>

<div class="modal-overlay" id="modal-res">
  <div class="modal-box" style="padding:22px">
    <div style="text-align:center;margin-bottom:16px">
      <div style="width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg,#a855f7,#7e22ce);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;margin:0 auto 10px"><i class="ti ti-user-plus"></i></div>
      <div style="font-size:15px;font-weight:800">نماینده جدید</div>
    </div>
    <input class="input" id="r-name" placeholder="نام" style="margin-bottom:8px">
    <input class="input" id="r-pw" type="password" placeholder="رمز" style="margin-bottom:8px">
    <input class="input" id="r-gb" type="number" placeholder="حجم (GB)" style="margin-bottom:14px">
    <div style="display:flex;gap:8px">
      <button class="btn btn-outline" onclick="closeModal('modal-res')" style="flex:1;justify-content:center">انصراف</button>
      <button class="btn btn-primary" onclick="createReseller()" style="flex:1;justify-content:center"><i class="ti ti-user-plus"></i> ذخیره</button>
    </div>
  </div>
</div>
"""
DASHBOARD_HTML = DASHBOARD_HTML + r"""
<script>
var isDark = localStorage.getItem('VaslZone-theme') !== 'light';
function applyTheme(dark) {
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  var icon = document.getElementById('theme-icon');
  if (icon) icon.className = 'ti ' + (dark ? 'ti-sun' : 'ti-moon');
}
try { applyTheme(isDark); } catch(e) {}

function toggleTheme() {
  isDark = !isDark;
  localStorage.setItem('VaslZone-theme', isDark ? 'dark' : 'light');
  applyTheme(isDark);
}

function toast(msg, type) {
  var el = document.getElementById('toast');
  if (!el) return;
  el.innerHTML = msg;
  el.className = 'toast show';
  if (type === 'ok') el.className += ' ok';
  setTimeout(function() { el.classList.remove('show'); }, 2200);
}

function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1048576) return (b / 1024).toFixed(1) + ' KB';
  if (b < 1073741824) return (b / 1048576).toFixed(2) + ' MB';
  return (b / 1073741824).toFixed(2) + ' GB';
}

function toFa(n) {
  return String(n).replace(/\d/g, function(d) { return '۰۱۲۳۴۵۶۷۸۹'[d]; });
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, function(c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
  });
}

function daysLeft(exp) {
  if (!exp) return null;
  return Math.ceil((new Date(exp) - Date.now()) / 86400000);
}

function expChip(exp, expired) {
  if (expired) return '<span class="badge" style="background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if (!exp) return '<span class="badge" style="background:var(--red-dim);color:var(--yellow);border:1px solid rgba(245,158,11,0.25)"><i class="ti ti-infinity"></i> نامحدود</span>';
  var d = daysLeft(exp);
  if (d <= 0) return '<span class="badge" style="background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if (d <= 3) return '<span class="badge" style="background:rgba(245,158,11,0.1);color:var(--yellow);border:1px solid rgba(245,158,11,0.25)"><i class="ti ti-alert-triangle"></i> ' + toFa(d) + ' روز</span>';
  return '<span class="badge" style="background:rgba(16,185,129,0.1);color:var(--green);border:1px solid rgba(16,185,129,0.25)"><i class="ti ti-calendar-check"></i> ' + toFa(d) + ' روز</span>';
}

function protoBadge(p) {
  var m = {
    'vless-ws': ['VLESS·WS', 'proto-vless'],
    'xhttp-packet-up': ['XHTTP·PUP', 'proto-xhttp'],
    'xhttp-stream-up': ['XHTTP·SUP', 'proto-xhttp'],
    'xhttp-stream-one': ['XHTTPaULTRA', 'proto-xhttp'],
    'trojan-ws': ['Trojan·WS', 'proto-trojan']
  };
  var v = m[p] || m['vless-ws'];
  return '<span class="proto-badge ' + v[1] + '">' + v[0] + '</span>';
}

async function checkAuth() {
  try {
    var r = await fetch('/api/me');
    var d = await r.json();
    if (!d.authenticated) { window.location.href = '/login'; }
  } catch(e) { window.location.href = '/login'; }
}

async function logout() {
  try { await fetch('/api/logout', { method: 'POST' }); } catch(e) {}
  window.location.href = '/login';
}

var logoutBtn = document.getElementById('logout-btn');
if (logoutBtn) logoutBtn.addEventListener('click', logout);

async function authF(url, opts) {
  var r = await fetch(url, opts || {});
  if (r.status === 401) { window.location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

function selProto(val, el) {
  document.getElementById('nl-proto').value = val;
  var all = document.querySelectorAll('.proto-btn');
  for (var i = 0; i < all.length; i++) all[i].classList.remove('active');
  el.classList.add('active');
}

var navItems = document.querySelectorAll('.nav-item');
for (var i = 0; i < navItems.length; i++) {
  navItems[i].addEventListener('click', function() {
    var page = this.getAttribute('data-page');
    if (!page) return;
    navTo(page);
  });
}

function navTo(page) {
  var allNav = document.querySelectorAll('.nav-item');
  for (var i = 0; i < allNav.length; i++) allNav[i].classList.remove('active');
  var targetNav = document.querySelector('.nav-item[data-page="' + page + '"]');
  if (targetNav) targetNav.classList.add('active');
  var allPages = document.querySelectorAll('.page');
  for (var j = 0; j < allPages.length; j++) allPages[j].classList.remove('active');
  var targetPage = document.getElementById('page-' + page);
  if (targetPage) targetPage.classList.add('active');
  var loaders = {
    'links': loadLinks,
    'subs': loadSubs,
    'traffic': null,
    'connections': loadConns,
    'logs': loadActivity,
    'errors': loadErrs,
    'settings': null,
    'subscriptions': loadSubsPage
  };
  if (loaders[page]) loaders[page]();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function openModal(id) {
  var el = document.getElementById(id);
  if (el) el.classList.add('open');
}

function closeModal(id) {
  var el = document.getElementById(id);
  if (el) el.classList.remove('open');
}

var prevTraf = 0, ch1, ch2, ch3;

async function fetchStats() {
  try {
    var r = await authF('/stats');
    var d = await r.json();
    document.getElementById('m-conns').textContent = d.active_connections || 0;
    document.getElementById('conns-nb').textContent = d.active_connections || 0;
    var mb = (d.total_traffic_mb || 0).toFixed(1);
    document.getElementById('m-traffic').innerHTML = mb + ' <span class="u">MB</span>';
    document.getElementById('m-alinks').textContent = d.active_links || '—';
    document.getElementById('m-lsub').textContent = 'از ' + (d.links_count || 0) + ' کانفیگ';
    document.getElementById('m-subs').textContent = d.subs_count || '—';
    document.getElementById('errs-badge').textContent = (d.total_errors || 0) + ' خطا';
    document.getElementById('uptime-inline').textContent = d.uptime || '—';
    document.getElementById('uptime-badge').textContent = d.uptime || '—';
    document.getElementById('last-upd').textContent = 'آخرین بروزرسانی: ' + new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML = '<span class="dot"></span> ' + (d.active_connections || 0) + ' اتصال';
    document.getElementById('t-traffic').innerHTML = mb + ' <span class="u">MB</span>';
    var delta = d.total_traffic_mb - prevTraf;
    var pct = Math.min(100, Math.round((delta / 50) * 100));
    document.getElementById('bw-pct').textContent = pct + '%';
    document.getElementById('bw-bar').style.width = pct + '%';
    prevTraf = d.total_traffic_mb;
    if (d.hourly) {
      var labels = Object.keys(d.hourly).sort();
      var vals = labels.map(function(k) { return +(d.hourly[k] / 1048576).toFixed(2); });
      if (ch1) { ch1.data.labels = labels; ch1.data.datasets[0].data = vals; ch1.update(); }
      if (ch3) { ch3.data.labels = labels; ch3.data.datasets[0].data = vals; ch3.update(); }
      if (vals.length) {
        var avg = vals.reduce(function(a,b) { return a + b; }, 0) / vals.length;
        var peak = Math.max.apply(null, vals);
        document.getElementById('t-avg').innerHTML = avg.toFixed(2) + ' <span class="u">MB</span>';
        document.getElementById('t-peak').innerHTML = peak.toFixed(2) + ' <span class="u">MB</span>';
      }
    }
    renderErrs(d.recent_errors || []);
  } catch(e) { console.error(e); }
}

function renderErrs(errs) {
  var el = document.getElementById('errs-full');
  if (!el) return;
  if (!errs.length) {
    el.innerHTML = '<div style="color:var(--green);padding:10px;font-size:12px"><i class="ti ti-circle-check"></i> بدون خطا</div>';
    return;
  }
  var h = '';
  for (var i = errs.length - 1; i >= 0; i--) {
    h += '<div class="log-item"><div class="log-ic err"><i class="ti ti-alert-circle"></i></div><div class="log-msg">' + esc(errs[i].error) + (errs[i].url ? ' — ' + esc(errs[i].url) : '') + '</div></div>';
  }
  el.innerHTML = h;
}
DASHBOARD_HTML = DASHBOARD_HTML + r"""
var allLinks = [], allSubs = [];

async function loadLinks() {
  try {
    var lr = await authF('/api/links');
    var sr = await authF('/api/subs');
    var ld = await lr.json();
    var sd = await sr.json();
    var links = ld.links || [];
    var subs = sd.subs || [];
    allLinks = links;
    allSubs = subs;
    document.getElementById('links-nb').textContent = links.length;
    document.getElementById('links-pg-cnt').textContent = toFa(links.length) + ' کانفیگ';
    var sel = document.getElementById('nl-sub');
    if (sel) {
      var cur = sel.value;
      sel.innerHTML = '<option value="">بدون گروه</option>' + subs.map(function(s) {
        return '<option value="' + esc(s.sub_id) + '">' + esc(s.name) + '</option>';
      }).join('');
      if (cur) sel.value = cur;
    }
    var grid = document.getElementById('links-grid');
    var empty = document.getElementById('links-empty');
    if (!links.length) {
      grid.innerHTML = '';
      empty.style.display = 'block';
      document.getElementById('lsummary').innerHTML = '<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';
      return;
    }
    empty.style.display = 'none';
    var subMap = {};
    for (var si = 0; si < subs.length; si++) subMap[subs[si].sub_id] = subs[si].name;
    var html = '';
    for (var i = 0; i < links.length; i++) {
      var l = links[i];
      var lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
      var pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
      var bc = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--yellow)' : '#22c55e';
      var allowed = l.active && !l.expired;
      html += '<div class="cfg-card' + (allowed ? '' : ' is-off') + '">' +
        '<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">' +
        '<span class="cfg-status"' + (allowed ? '' : ' style="background:var(--text-3);box-shadow:none"') + '></span>' +
        '<div style="flex:1"><div class="cfg-label">' + esc(l.label) + '</div></div>' +
        '<span class="nav-item" style="padding:2px 6px;margin:0;display:flex;align-items:center;gap:3px">' + expChip(l.expires_at, l.expired) + '</span>' +
        '</div>' +
        '<div class="cfg-usage">' +
        '<div class="cfg-bar"><div class="cfg-bar-fill" style="width:' + pct + '%;background:' + bc + '"></div></div>' +
        '<div class="cfg-utxt"><span>مصرف: ' + l.used_fmt + '</span><span>از ' + lim + '</span></div>' +
        '</div>' +
        '<div class="cfg-row2">' +
        protoBadge(l.protocol) +
        (l.sub_id && subMap[l.sub_id] ? '<span style="font-size:9px;color:var(--text-2)"><i class="ti ti-folder" style="color:#c084fc"></i> ' + esc(subMap[l.sub_id]) + '</span>' : '') +
        '<span style="font-size:9px;color:var(--text-2);margin-right:auto">UUID: ' + l.uuid.slice(0, 8) + '…</span>' +
        '</div>' +
        '<div style="display:flex;gap:5px;margin-top:10px;flex-wrap:wrap;border-top:1px solid var(--border);padding-top:8px">' +
        '<button class="tog' + (allowed ? ' on' : '') + '" onclick="toggleLink(\'' + l.uuid + '\',' + !l.active + ')"></button>' +
        '<button class="btn btn-outline btn-sm btn-icon" onclick="copyText(\'' + esc(l.vless_link || '') + '\')" title="کپی"><i class="ti ti-copy"></i></button>' +
        '<button class="btn btn-outline btn-sm btn-icon" onclick="copyText(\'' + esc(l.sub_url || '') + '\')" title="ساب"><i class="ti ti-rss"></i></button>' +
        '<button class="btn btn-outline btn-sm btn-icon" onclick="showQR(\'' + esc(l.vless_link || '') + '\')" title="QR"><i class="ti ti-qrcode"></i></button>' +
        '<button class="btn btn-outline btn-sm btn-icon" onclick="deleteLink(\'' + l.uuid + '\')" title="حذف"><i class="ti ti-trash"></i></button>' +
        '</div></div>';
    }
    grid.innerHTML = html;
    var ls = document.getElementById('lsummary');
    if (ls) {
      ls.innerHTML = links.slice(0, 6).map(function(l) {
        return '<div style="display:flex;justify-content:space-between;padding:5px 0;font-size:11px;border-bottom:1px solid rgba(220,38,38,0.04)">' +
          '<span style="color:var(--text-2)"><i class="ti ti-' + (l.expired ? 'calendar-x' : l.active ? 'circle-check' : 'circle-x') + '" style="color:' + (l.expired ? 'var(--yellow)' : l.active ? 'var(--green)' : 'var(--red)') + '"></i> ' + esc(l.label) + '</span>' +
          '<span>' + fmtB(l.used_bytes) + ' / ' + (l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes)) + '</span></div>';
      }).join('');
    }
  } catch(e) { console.error(e); }
}

async function createLink() {
  var label = (document.getElementById('nl-label').value || '').trim() || 'کانفیگ جدید';
  var val = document.getElementById('nl-val').value;
  var unit = document.getElementById('nl-unit').value;
  var exp = document.getElementById('nl-exp').value;
  var note = (document.getElementById('nl-note').value || '').trim();
  var sub_id = document.getElementById('nl-sub').value || null;
  var protocol = document.getElementById('nl-proto').value || 'vless-ws';
  var ips = (document.getElementById('nl-ips').value || '').split(',').map(function(s) { return s.trim(); }).filter(Boolean);
  var port = parseInt(document.getElementById('nl-port').value) || null;
  var count = parseInt(document.getElementById('nl-count').value) || 1;
  var body = { label: label, limit_value: val || 0, limit_unit: unit, expires_days: exp || 0, note: note, sub_id: sub_id, protocol: protocol, ips: ips, port: port };
  try {
    if (count > 1) {
      body.count = count;
      var r = await fetch('/api/links/bulk', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      await r.json();
      toast(toFa(count) + ' کانفیگ ساخته شد ✓', 'ok');
    } else {
      var r = await fetch('/api/links', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      var d = await r.json();
      if (d.sub_url) { try { navigator.clipboard.writeText(d.sub_url); } catch(e) {} }
      toast('🔥 کانفیگ ساخته شد', 'ok');
    }
    document.getElementById('nl-label').value = '';
    document.getElementById('nl-val').value = '';
    document.getElementById('nl-exp').value = '';
    document.getElementById('nl-note').value = '';
    document.getElementById('nl-ips').value = '';
    document.getElementById('nl-port').value = '';
    document.getElementById('nl-count').value = '1';
    loadLinks();
  } catch(e) { toast('❌ خطا', 'err'); }
}

async function toggleLink(uuid, newState) {
  try {
    var r = await authF('/api/links/' + uuid, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ active: newState }) });
    if (!r.ok) throw new Error();
    toast(newState ? 'فعال شد ✓' : 'غیرفعال شد', newState ? 'ok' : '');
    loadLinks();
  } catch(e) { toast('❌ خطا', 'err'); }
}

async function deleteLink(uuid) {
  if (!confirm('حذف کانفیگ؟')) return;
  try {
    await authF('/api/links/' + uuid, { method: 'DELETE' });
    toast('حذف شد ✓', 'ok');
    loadLinks();
  } catch(e) { toast('❌ خطا', 'err'); }
}

function copyText(t) {
  try { navigator.clipboard.writeText(t).then(function() { toast('کپی شد ✓', 'ok'); }); } catch(e) {}
}

function showQR(link) {
  if (!link) return;
  window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=' + encodeURIComponent(link), '_blank');
}

function cpText(id) {
  var el = document.getElementById(id);
  if (el) copyText(el.textContent);
}

function qrFor(id) {
  var el = document.getElementById(id);
  if (el) showQR(el.textContent);
}

async function loadSubs() {
  try {
    var r = await authF('/api/subs');
    var d = await r.json();
    var subs = d.subs || [];
    allSubs = subs;
    document.getElementById('subs-nb').textContent = subs.length;
    document.getElementById('subs-pg-cnt').textContent = toFa(subs.length) + ' گروه';
    var grid = document.getElementById('subs-grid');
    if (!subs.length) {
      grid.innerHTML = '<div class="empty" style="grid-column:1/-1"><i class="ti ti-folders"></i><p>گروهی وجود ندارد</p></div>';
      return;
    }
    var h = '';
    for (var i = 0; i < subs.length; i++) {
      var s = subs[i];
      h += '<div class="sub-card">' +
        '<div class="sub-head">' +
        '<div class="sub-icon"><i class="ti ti-folder"></i></div>' +
        '<div style="flex:1"><div class="sub-name">' + esc(s.name) + '</div>' +
        (s.desc ? '<div class="sub-desc">' + esc(s.desc) + '</div>' : '') + '</div>' +
        '<div style="font-size:18px;color:' + (s.has_password ? 'var(--yellow)' : 'var(--green)') + '"><i class="ti ti-' + (s.has_password ? 'lock' : 'lock-open') + '"></i></div>' +
        '</div>' +
        '<div class="sub-stats">' +
        '<div class="sub-stat"><div class="sub-stat-val">' + toFa(s.links_count || 0) + '</div><div class="sub-stat-label">کانفیگ</div></div>' +
        '<div class="sub-stat"><div class="sub-stat-val" style="color:var(--green)">' + toFa(s.active_count || 0) + '</div><div class="sub-stat-label">فعال</div></div>' +
        '<div class="sub-stat"><div class="sub-stat-val" style="font-size:11px">' + esc(s.total_used_fmt || '0') + '</div><div class="sub-stat-label">مصرف</div></div>' +
        '</div>' +
        '<div class="sub-url"><span style="flex:1;word-break:break-all;min-width:0">' + esc(s.public_url) + '</span>' +
        '<button class="btn btn-outline btn-sm btn-icon" onclick="copyText(\'' + esc(s.public_url) + '\')"><i class="ti ti-copy"></i></button></div>' +
        '<div class="sub-actions">' +
        '<button class="btn btn-outline btn-sm" onclick="copySubLinks(\'' + esc(s.sub_id) + '\')"><i class="ti ti-copy"></i> کپی همه</button>' +
        '<button class="btn btn-outline btn-sm" onclick="showQR(\'' + esc(s.sub_url) + '\')"><i class="ti ti-qrcode"></i></button>' +
        '<button class="btn btn-sm" style="background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)" onclick="deleteSub(\'' + esc(s.sub_id) + '\')"><i class="ti ti-trash"></i></button>' +
        '</div></div>';
    }
    grid.innerHTML = h;
  } catch(e) { console.error(e); }
}

async function createSub() {
  var name = (document.getElementById('ns-name').value || '').trim() || 'گروه جدید';
  var desc = (document.getElementById('ns-desc').value || '').trim();
  var pw = (document.getElementById('ns-pw').value || '').trim();
  try {
    var r = await authF('/api/subs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: name, desc: desc, password: pw })
    });
    if (!r.ok) throw new Error();
    document.getElementById('ns-name').value = '';
    document.getElementById('ns-desc').value = '';
    document.getElementById('ns-pw').value = '';
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓', 'ok');
    loadSubs();
  } catch(e) { toast('❌ خطا', 'err'); }
}

async function deleteSub(sub_id) {
  if (!confirm('حذف گروه؟')) return;
  try {
    await authF('/api/subs/' + sub_id, { method: 'DELETE' });
    toast('حذف شد ✓', 'ok');
    loadSubs();
    loadLinks();
  } catch(e) { toast('❌ خطا', 'err'); }
}

async function copySubLinks(subId) {
  try {
    var lr = await authF('/api/links');
    var ld = await lr.json();
    var links = ld.links || [];
    var sub = null;
    for (var i = 0; i < allSubs.length; i++) {
      if (allSubs[i].sub_id === subId) { sub = allSubs[i]; break; }
    }
    if (!sub) { toast('گروه پیدا نشد', 'err'); return; }
    var ids = sub.link_ids || [];
    var urls = [];
    for (var j = 0; j < links.length; j++) {
      if (ids.indexOf(links[j].uuid) !== -1 && links[j].active && !links[j].expired) {
        urls.push(links[j].sub_url || links[j].vless_link);
      }
    }
    if (!urls.length) { toast('کانفیگ فعالی نیست', 'err'); return; }
    navigator.clipboard.writeText(urls.join('\n')).then(function() { toast(toFa(urls.length) + ' لینک کپی شد', 'ok'); });
  } catch(e) { toast('❌ خطا', 'err'); }
}

async function loadSubsPage() {
  var el = document.getElementById('sub-all-url');
  if (el) el.textContent = window.location.protocol + '//' + window.location.host + '/sub-all';
  try {
    var r = await authF('/api/subs');
    var d = await r.json();
    var subs = d.subs || [];
    var el2 = document.getElementById('sub-groups-list');
    if (!subs.length) { el2.innerHTML = '<div class="empty"><i class="ti ti-rss-off"></i><p>گروهی ندارید</p></div>'; return; }
    el2.innerHTML = subs.map(function(s) {
      return '<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;padding:10px 12px;background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:10px;margin-bottom:7px">' +
        '<div style="font-weight:700;font-size:13px">' + esc(s.name) + '</div>' +
        '<div style="display:flex;gap:5px">' +
        '<button class="btn btn-outline btn-sm" onclick="copyText(\'' + esc(s.sub_url) + '\')"><i class="ti ti-copy"></i> ساب</button>' +
        '<button class="btn btn-outline btn-sm" onclick="showQR(\'' + esc(s.sub_url) + '\')"><i class="ti ti-qrcode"></i></button></div></div>';
    }).join('');
  } catch(e) { console.error(e); }
}

function cpSubAll() {
  copyText(window.location.protocol + '//' + window.location.host + '/sub-all');
}

async function loadConns() {
  try {
    var r = await authF('/api/connections');
    var d = await r.json();
    var conns = d.connections || [];
    document.getElementById('ch-count').textContent = toFa(conns.length);
    document.getElementById('conns-live').innerHTML = '<span class="dot"></span> ' + toFa(conns.length) + ' اتصال';
    var grid = document.getElementById('conns-grid');
    var empty = document.getElementById('conns-empty');
    if (!conns.length) {
      grid.innerHTML = '';
      empty.style.display = 'block';
      return;
    }
    empty.style.display = 'none';
    var total = 0, uniq = new Set();
    for (var i = 0; i < conns.length; i++) {
      if (conns[i].bytes) total += conns[i].bytes;
      if (conns[i].ip) uniq.add(conns[i].ip);
    }
    document.getElementById('ch-traffic').textContent = fmtB(total);
    document.getElementById('ch-uniq').textContent = toFa(uniq.size);
    var gridH = '';
    for (var j = 0; j < conns.length; j++) {
      var c = conns[j];
      var secs = c.connected_at ? Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000) : 0;
      var dur = secs < 60 ? secs + ' ث' : secs < 3600 ? Math.floor(secs / 60) + ' د' : Math.floor(secs / 3600) + ' س';
      gridH += '<div class="cfg-card">' +
        '<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px"><span class="cfg-status"></span>' +
        '<div style="font-family:monospace;font-weight:700;font-size:14px;color:var(--text);flex:1">' + esc(c.ip || '—') + '</div>' +
        '<span style="font-size:9px;background:rgba(16,185,129,0.1);color:var(--green);padding:2px 8px;border-radius:10px;border:1px solid rgba(16,185,129,0.2)">زنده</span></div>' +
        '<div style="display:flex;gap:8px;font-size:10.5px;color:var(--text-2)">' +
        '<span><i class="ti ti-transfer"></i> ' + (c.bytes_fmt || '0') + '</span>' +
        '<span><i class="ti ti-clock"></i> ' + dur + '</span></div></div>';
    }
    grid.innerHTML = gridH;
  } catch(e) { console.error(e); }
}

async function loadErrs() {
  try {
    var r = await authF('/stats');
    var d = await r.json();
    renderErrs(d.recent_errors || []);
  } catch(e) {}
}

async function loadActivity() {
  try {
    var r = await authF('/api/activity');
    var d = await r.json();
    var logs = (d.logs || []).slice().reverse();
    var el = document.getElementById('logs-list');
    if (!logs.length) { el.innerHTML = '<div class="empty"><i class="ti ti-history"></i><p>لاگی وجود ندارد</p></div>'; return; }
    var icMap = { ok: 'ti-circle-check', err: 'ti-alert-circle', warn: 'ti-alert-triangle', info: 'ti-info-circle' };
    el.innerHTML = logs.map(function(l) {
      return '<div class="log-item"><div class="log-ic ' + (l.level || 'info') + '"><i class="ti ' + (icMap[l.level] || 'ti-info-circle') + '"></i></div>' +
        '<div class="log-msg">' + esc(l.message) + '<div class="log-time">' + new Date(l.time).toLocaleString('fa-IR') + '</div></div></div>';
    }).join('');
  } catch(e) { console.error(e); }
}

async function fetchDefaultVless() {
  try {
    var r = await authF('/api/links');
    var d = await r.json();
    var links = d.links || [];
    var def = links.filter(function(l) { return l.limit_bytes === 0 && l.active && !l.expired; })[0] ||
              links.filter(function(l) { return l.active && !l.expired; })[0] || links[0];
    var el = document.getElementById('vless-main');
    if (el) el.textContent = def ? (def.vless_link || '') : 'کانفیگی وجود ندارد';
  } catch(e) {}
}

function refreshAll() {
  fetchStats();
  fetchDefaultVless();
  loadLinks();
  var pages = document.querySelectorAll('.page.active');
  for (var i = 0; i < pages.length; i++) {
    var id = pages[i].id;
    if (id === 'page-subs') loadSubs();
    if (id === 'page-connections') loadConns();
    if (id === 'page-logs') loadActivity();
    if (id === 'page-subscriptions') loadSubsPage();
  }
  toast('رفرش شد ✓', 'ok');
}

function initCharts() {
  try {
    if (typeof Chart === 'undefined') { return; }
    var c1 = document.getElementById('ch1');
    if (c1) {
      var ctx = c1.getContext('2d');
      ch1 = new Chart(ctx, {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'MB', data: [], borderColor: '#ef4444', backgroundColor: 'rgba(220,38,38,0.1)', fill: true, tension: 0.4, pointRadius: 0, borderWidth: 2 }] },
        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
          scales: { x: { grid: { display: false }, ticks: { color: '#525252', font: { size: 9 } } },
                    y: { grid: { color: 'rgba(220,38,38,0.05)' }, ticks: { color: '#525252', font: { size: 9 } } } } }
      });
    }
    var c2 = document.getElementById('ch2');
    if (c2) {
      ch2 = new Chart(c2.getContext('2d'), {
        type: 'doughnut',
        data: { labels: ['VLESS/WS', 'XHTTP', 'HTTP Proxy'], datasets: [{ data: [55, 35, 10], backgroundColor: ['#dc2626', '#a855f7', '#f59e0b'], borderWidth: 3, spacing: 3 }] },
        options: { responsive: true, maintainAspectRatio: false, cutout: '72%', plugins: { legend: { position: 'bottom', labels: { color: '#a3a3a3', font: { size: 10 } } } } }
      });
    }
    var c3 = document.getElementById('ch3');
    if (c3) {
      ch3 = new Chart(c3.getContext('2d'), {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'مصرف', data: [], borderColor: '#ef4444', backgroundColor: 'rgba(220,38,38,0.1)', fill: true, tension: 0.4, pointRadius: 0, borderWidth: 2 },
                                        { label: 'میانگین', data: [], borderColor: '#f59e0b', borderDash: [5, 5], pointRadius: 0, fill: false }] },
        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
          scales: { x: { grid: { display: false }, ticks: { color: '#525252', font: { size: 9 } } },
                    y: { grid: { color: 'rgba(220,38,38,0.05)' }, ticks: { color: '#525252', font: { size: 9 } } } } }
      });
    }
  } catch(e) { }
}

document.addEventListener('DOMContentLoaded', async function() {
  await checkAuth();
  setTimeout(function() { try { initCharts(); } catch(e) {} }, 500);
  var sh = document.getElementById('set-host');
  if (sh) sh.textContent = location.host;
  var sa = document.getElementById('sub-all-url');
  if (sa) sa.textContent = window.location.protocol + '//' + window.location.host + '/sub-all';
  fetchStats();
  fetchDefaultVless();
  loadLinks();
  loadSubs();
  setInterval(fetchStats, 4000);
  setInterval(function() {
    var active = document.querySelector('.page.active');
    if (!active) return;
    var id = active.id;
    if (id === 'page-links') loadLinks();
    if (id === 'page-subs') loadSubs();
    if (id === 'page-connections') loadConns();
    if (id === 'page-logs') loadActivity();
  }, 5000);
});

async function changePw() {
  var cur = (document.getElementById('cp-cur').value || '').trim();
  var nw = (document.getElementById('cp-new').value || '').trim();
  var cf = (document.getElementById('cp-cf').value || '').trim();
  if (!cur || !nw || !cf) { toast('همه فیلدها الزامی', 'err'); return; }
  if (nw !== cf) { toast('تکرار رمز اشتباه', 'err'); return; }
  try {
    var r = await authF('/api/change-password', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ current_password: cur, new_password: nw })
    });
    if (!r.ok) { var d = await r.json().catch(function() { return {}; }); throw new Error(d.detail || 'خطا'); }
    toast('رمز تغییر کرد ✓', 'ok');
    document.getElementById('cp-cur').value = '';
    document.getElementById('cp-new').value = '';
    document.getElementById('cp-cf').value = '';
  } catch(e) { toast('❌ ' + e.message, 'err'); }
}

async function createReseller() {
  var name = (document.getElementById('r-name').value || '').trim();
  var pw = (document.getElementById('r-pw').value || '').trim();
  var gb = parseFloat(document.getElementById('r-gb').value) || 0;
  if (!name || !pw) { toast('نام و رمز الزامی', 'err'); return; }
  try {
    var r = await authF('/api/resellers', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: name, password: pw, limit_gb: gb })
    });
    await r.json();
    closeModal('modal-res');
    document.getElementById('r-name').value = '';
    document.getElementById('r-pw').value = '';
    document.getElementById('r-gb').value = '';
    toast('نماینده ساخته شد ✓', 'ok');
  } catch(e) { toast('❌ خطا', 'err'); }
}
</script>
</body></html>"""
