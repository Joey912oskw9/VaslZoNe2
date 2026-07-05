from fastapi.responses import HTMLResponse
from urllib.parse import quote

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>ورود · VaslZone</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --bg:#050505;--bg-2:#0a0a0a;--bg-3:#0e0e0e;
  --card:#0f0f0f;--card-2:#151515;--card-3:#1a1a1a;
  --border:rgba(239,68,68,0.08);--border-2:rgba(239,68,68,0.25);--border-3:rgba(245,158,11,0.30);
  --red:#dc2626;--red-2:#ef4444;--red-3:#f87171;--red-dim:rgba(220,38,38,0.12);
  --yellow:#f59e0b;--yellow-2:#fbbf24;--yellow-3:#fde047;--yellow-d:rgba(245,158,11,0.12);
  --text:#f5f5f5;--text-2:#d4d4d4;--text-3:#a3a3a3;--text-4:#525252;
  --shadow:0 8px 32px rgba(0,0,0,0.6);--shadow-r:0 8px 32px rgba(220,38,38,0.20);
  --radius:14px;--radius-l:20px;
  --grad-red:linear-gradient(135deg,#dc2626 0%,#ef4444 50%,#f87171 100%);
  --grad-fire:linear-gradient(135deg,#7f1d1d 0%,#dc2626 50%,#f59e0b 100%);
}
html,body{height:100%}
body{
  font-family:'Vazirmatn',sans-serif;
  background:var(--bg);
  color:var(--text);
  min-height:100vh;display:flex;align-items:center;justify-content:center;
  padding:20px;overflow:hidden;
}

/* ─── پس‌زمینه متحرک ─── */
.bg-fx{position:fixed;inset:0;background:
  radial-gradient(ellipse 80% 50% at 50% 0%,rgba(220,38,38,0.10),transparent 70%),
  radial-gradient(ellipse 60% 40% at 80% 100%,rgba(245,158,11,0.06),transparent 60%),
  radial-gradient(ellipse 60% 40% at 20% 100%,rgba(239,68,68,0.05),transparent 60%),
  var(--bg);
  z-index:0;pointer-events:none}
.grd-fx{position:fixed;inset:0;background-image:
  linear-gradient(rgba(239,68,68,0.025) 1px,transparent 1px),
  linear-gradient(90deg,rgba(239,68,68,0.025) 1px,transparent 1px);
  background-size:50px 50px;
  z-index:0;pointer-events:none}
.particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.particle{position:absolute;width:2px;height:2px;background:var(--red-3);border-radius:50%;
  box-shadow:0 0 6px var(--red-2);animation:float-up 15s infinite linear}
@keyframes float-up{
  0%{transform:translateY(0) translateX(0);opacity:0}
  10%{opacity:1}
  90%{opacity:1}
  100%{transform:translateY(-100vh) translateX(50px);opacity:0}
}

/* ─── کارت ورود ─── */
.wrap{position:relative;z-index:10;width:100%;max-width:440px}
.brand-top{text-align:center;margin-bottom:30px;animation:fade-down .8s ease}
@keyframes fade-down{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:none}}
.brand-logo{width:80px;height:80px;border-radius:22px;margin:0 auto 18px;
  background:var(--grad-fire);
  display:flex;align-items:center;justify-content:center;font-size:38px;color:#000;
  box-shadow:0 0 0 4px rgba(220,38,38,0.15),0 12px 40px rgba(220,38,38,0.25);
  position:relative;overflow:hidden}
.brand-logo::before{content:'';position:absolute;inset:0;
  background:linear-gradient(45deg,transparent 30%,rgba(255,255,255,0.2) 50%,transparent 70%);
  animation:shine 3s infinite}
@keyframes shine{0%,100%{transform:translateX(-100%)}50%{transform:translateX(100%)}}
.brand-logo i{position:relative;z-index:1}
.brand-name{font-size:22px;font-weight:900;background:var(--grad-red);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;letter-spacing:-.02em;
  text-shadow:0 0 40px rgba(220,38,38,0.3)}
.brand-sub{font-size:10px;color:var(--text-3);margin-top:6px;letter-spacing:.25em;
  font-weight:500}

.card-login{
  background:linear-gradient(145deg,rgba(15,15,15,0.95),rgba(10,10,10,0.95));
  border:1px solid var(--border-2);
  border-radius:var(--radius-l);
  padding:36px 32px 32px;backdrop-filter:blur(20px);
  box-shadow:0 0 0 1px rgba(239,68,68,0.05),var(--shadow-r);
  position:relative;overflow:hidden;
  animation:fade-up .8s ease .2s both}
@keyframes fade-up{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
.card-login::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:var(--grad-fire);border-radius:var(--radius-l) var(--radius-l) 0 0}
.card-login::after{content:'';position:absolute;top:-50px;right:-50px;width:200px;height:200px;
  background:radial-gradient(circle,rgba(220,38,38,0.15),transparent 70%);pointer-events:none}

.h-txt{margin-bottom:24px;text-align:center;position:relative;z-index:1}
.h-txt h1{font-size:20px;font-weight:800;color:var(--text);margin-bottom:6px;letter-spacing:-.01em}
.h-txt p{font-size:11px;color:var(--text-3);line-height:1.7}

.err{
  display:none;background:var(--red-dim);border:1px solid var(--border-2);
  border-radius:10px;padding:10px 14px;
  margin-bottom:18px;font-size:11.5px;color:var(--red-3);
  align-items:center;gap:8px;position:relative;z-index:1;
  animation:shake .4s ease}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}

.field{margin-bottom:18px;position:relative;z-index:1}
.field label{display:block;font-size:10px;font-weight:700;color:var(--text-3);
  margin-bottom:7px;text-transform:uppercase;letter-spacing:.08em}
.inp-wrap{position:relative}
input[type=password]{
  width:100%;padding:14px 46px;
  border-radius:12px;border:1.5px solid var(--border);
  background:rgba(5,5,5,0.6);color:var(--text);
  font-family:inherit;font-size:14px;outline:none;
  transition:all .25s cubic-bezier(.4,0,.2,1)}
input[type=password]:focus{
  border-color:var(--red);
  background:rgba(5,5,5,1);
  box-shadow:0 0 0 3px var(--red-dim),0 0 30px rgba(220,38,38,0.15)}
.ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);
  color:var(--text-4);font-size:18px;pointer-events:none;transition:all .25s}
input:focus~.ic{color:var(--red-2)}

.btn-login{
  width:100%;padding:14px;border:none;border-radius:12px;cursor:pointer;
  background:var(--grad-red);color:#fff;
  font-family:inherit;font-size:14px;font-weight:800;
  display:flex;align-items:center;justify-content:center;gap:8px;
  box-shadow:0 4px 20px rgba(220,38,38,0.4);
  transition:all .25s cubic-bezier(.4,0,.2,1);
  position:relative;overflow:hidden;margin-top:6px;z-index:1}
.btn-login::before{content:'';position:absolute;inset:0;
  background:linear-gradient(120deg,transparent 30%,rgba(255,255,255,0.25) 50%,transparent 70%);
  transform:translateX(-100%);transition:transform .6s}
.btn-login:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(220,38,38,0.5)}
.btn-login:hover::before{transform:translateX(100%)}
.btn-login:active{transform:translateY(0) scale(.98)}
.btn-login:disabled{opacity:.6;cursor:not-allowed;transform:none}

.footer-txt{margin-top:18px;text-align:center;
  padding-top:18px;border-top:1px solid var(--border);
  display:flex;align-items:center;justify-content:center;gap:8px;
  font-size:10.5px;color:var(--text-3);position:relative;z-index:1}
.footer-txt a{color:var(--yellow-2);font-weight:700;text-decoration:none}
</style></head><body>
<div class="bg-fx"></div><div class="grd-fx"></div>
<div class="particles" id="particles"></div>
<div class="wrap">
  <div class="brand-top">
    <div class="brand-logo"><i class="ti ti-flame"></i></div>
    <div class="brand-name">VaslZone</div>
    <div class="brand-sub">GATEWAY · v9.3</div>
  </div>
  <div class="card-login">
    <div class="h-txt">
      <h1>🔐 ورود به پنل</h1>
      <p>برای دسترسی به داشبورد رمز عبور را وارد کنید</p>
    </div>
    <div class="err" id="err"><i class="ti ti-alert-triangle"></i><span id="err-text"></span></div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="••••••••••••" autofocus required>
          <i class="ti ti-key ic"></i>
        </div>
      </div>
      <button class="btn-login" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="footer-txt">کانال رسمی: <a href="https://t.me/VaslZone" target="_blank">@VaslZone</a></div>
  </div>
</div>
<script>
// ایجاد ذرات متحرک
const pc=document.getElementById('particles');
for(let i=0;i<25;i++){
  const p=document.createElement('div');p.className='particle';
  p.style.left=Math.random()*100+'%';
  p.style.bottom='-10px';
  p.style.animationDelay=Math.random()*15+'s';
  p.style.animationDuration=(10+Math.random()*15)+'s';
  pc.appendChild(p);
}
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),
        et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script></body></html>"""


# DASHBOARD_HTML شروع میشه اینجا
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VaslZone Gateway · پنل مدیریت</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script>
  const Chart=null;
</script>
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --bg:#050505;--bg-2:#080808;--bg-3:#0a0a0a;
  --card:#0e0e0e;--card-2:#131313;--card-3:#181818;
  --border:rgba(239,68,68,0.08);--border-2:rgba(239,68,68,0.25);--border-3:rgba(245,158,11,0.30);
  --red:#dc2626;--red-2:#ef4444;--red-3:#f87171;--red-dim:rgba(220,38,38,0.12);
  --yellow:#f59e0b;--yellow-2:#fbbf24;--yellow-3:#fde047;--yellow-d:rgba(245,158,11,0.12);
  --text:#f5f5f5;--text-2:#d4d4d4;--text-3:#a3a3a3;--text-4:#525252;
  --shadow:0 8px 32px rgba(0,0,0,0.5);--shadow-r:0 8px 32px rgba(220,38,38,0.15);
  --radius:14px;--radius-l:20px;
  --grad-red:linear-gradient(135deg,#dc2626 0%,#ef4444 50%,#f87171 100%);
  --grad-fire:linear-gradient(135deg,#7f1d1d 0%,#dc2626 50%,#f59e0b 100%);
  --sidebar:280px;
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--text);
  min-height:100vh;display:flex;font-size:14px;overflow-x:hidden}

/* ───── اسکرول ───── */
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:var(--bg-2)}
::-webkit-scrollbar-thumb{background:linear-gradient(180deg,var(--red),var(--red-2));border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:linear-gradient(180deg,var(--red-2),var(--red))}

/* ───── پس‌زمینه ───── */
.bg-fx{position:fixed;inset:0;
  background:radial-gradient(ellipse 60% 30% at 80% 0%,rgba(220,38,38,0.08),transparent 70%),
             radial-gradient(ellipse 50% 30% at 0% 100%,rgba(245,158,11,0.05),transparent 60%),
             var(--bg);
  z-index:0;pointer-events:none}
.grd-fx{position:fixed;inset:0;
  background-image:linear-gradient(rgba(239,68,68,0.02) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(239,68,68,0.02) 1px,transparent 1px);
  background-size:60px 60px;z-index:0;pointer-events:none}

/* ───── سایدبار ───── */
.sidebar{width:var(--sidebar);min-height:100vh;background:linear-gradient(180deg,
  var(--card-2) 0%,var(--card) 100%);
  border-left:1px solid var(--border);display:flex;flex-direction:column;
  flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;
  transition:transform .3s cubic-bezier(.4,0,.2,1)}
.sb-close{display:none;position:absolute;left:12px;top:18px;
  background:var(--red-dim);border:1px solid var(--border-2);
  color:var(--text-2);width:32px;height:32px;border-radius:9px;
  font-size:18px;align-items:center;justify-content:center;cursor:pointer}

/* ───── لوگو ───── */
.logo{display:flex;align-items:center;gap:12px;padding:22px 20px 18px;
  border-bottom:1px solid var(--border);position:relative}
.logo::after{content:'';position:absolute;bottom:-1px;left:20px;right:20px;
  height:1px;background:linear-gradient(90deg,transparent,var(--red),transparent)}
.logo-img{width:42px;height:42px;border-radius:11px;overflow:hidden;
  background:var(--grad-fire);
  display:flex;align-items:center;justify-content:center;font-size:20px;color:#000;
  box-shadow:0 0 0 2px rgba(220,38,38,0.15),0 6px 20px rgba(220,38,38,0.3);
  position:relative}
.logo-img i{position:relative;z-index:1}
.logo-name{font-size:14.5px;font-weight:800;color:var(--text);letter-spacing:-.01em}
.logo-sub{font-size:9px;color:var(--text-3);margin-top:2px;letter-spacing:.08em}

/* ───── نویگیشن ───── */
.nav-wrap{flex:1;overflow-y:auto;padding:8px 0 16px}
.nav-sec{padding:16px 18px 4px;font-size:9px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--red-3);font-weight:700;
  display:flex;align-items:center;gap:6px}
.nav-sec::after{content:'';flex:1;height:1px;
  background:linear-gradient(90deg,var(--border),transparent)}
.nav-it{display:flex;align-items:center;gap:10px;padding:10px 18px;
  color:var(--text-3);font-size:12.5px;cursor:pointer;
  border-right:2px solid transparent;border-radius:0 10px 10px 0;
  transition:all .2s ease;margin:2px 8px}
.nav-it:hover{background:rgba(239,68,68,0.06);color:var(--text-2);
  border-right-color:rgba(220,38,38,0.3)}
.nav-it.on{background:linear-gradient(90deg,rgba(220,38,38,0.20),rgba(220,38,38,0.05));
  color:var(--text);border-right-color:var(--red);font-weight:700;
  box-shadow:inset 4px 0 10px rgba(220,38,38,0.2)}
.nav-it i{font-size:18px;width:20px;text-align:center;flex-shrink:0}
.nav-it.on i{color:var(--red-3);filter:drop-shadow(0 0 4px var(--red-2))}
.nav-badge{margin-right:auto;background:var(--red-dim);
  border:1px solid var(--border-2);color:var(--red-3);font-size:9px;
  padding:2px 8px;border-radius:20px;font-weight:700}

/* ───── پایین سایدبار ───── */
.sb-foot{padding:14px 16px;border-top:1px solid var(--border);
  display:flex;flex-direction:column;gap:7px}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;
  background:linear-gradient(135deg,#0284c7,#0ea5e9);color:#fff;border-radius:10px;
  padding:10px;font-size:12px;font-weight:700;border:none;cursor:pointer;
  text-decoration:none;transition:.2s}
.tg-btn:hover{filter:brightness(1.15);transform:translateY(-1px)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;
  background:var(--red-dim);border:1px solid var(--border-2);
  color:var(--text-2);border-radius:10px;padding:9px;
  font-size:11.5px;font-weight:600;border:none;cursor:pointer;
  transition:.2s;font-family:inherit}
.theme-btn:hover{background:rgba(220,38,38,0.18);color:var(--text)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;
  background:transparent;border:1.5px solid var(--border-3);
  color:var(--yellow);border-radius:10px;padding:9px;
  font-size:11.5px;font-weight:700;border:none;cursor:pointer;
  transition:.2s;font-family:inherit}
.logout-btn:hover{background:var(--yellow-d);border-color:var(--yellow-2)}

/* ───── موبایل ───── */
.mob-top{display:none;position:fixed;top:0;right:0;left:0;
  height:58px;background:var(--card-2);border-bottom:1px solid var(--border-2);
  z-index:150;align-items:center;justify-content:space-between;padding:0 14px;
  transition:.3s}
.mob-top .ml{display:flex;align-items:center;gap:10px}
.mob-logo{width:30px;height:30px;border-radius:8px;background:var(--grad-fire);
  display:flex;align-items:center;justify-content:center;color:#000;font-size:16px}
.mob-title{color:var(--text);font-size:13.5px;font-weight:800;
  background:var(--grad-red);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--red-dim);
  border:1px solid var(--border-2);color:var(--text-2);
  width:36px;height:36px;border-radius:9px;font-size:17px;
  display:flex;align-items:center;justify-content:center;cursor:pointer}
.overlay{display:none;position:fixed;inset:0;
  background:rgba(0,0,0,0.7);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}

/* ───── محتوا ───── */
.main{margin-right:var(--sidebar);flex:1;padding:28px 28px 60px;
  min-width:0;position:relative;z-index:1;transition:margin .3s cubic-bezier(.4,0,.2,1)}
.pg{display:none;animation:fade-in .4s ease}
.pg.on{display:block}
@keyframes fade-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.pg-b{display:block}
.pg-b.on{display:none}

/* ───── تاپ‌بار ───── */
.topbar{display:flex;align-items:flex-start;justify-content:space-between;
  margin-bottom:26px;flex-wrap:wrap;gap:14px}
.tb-title{font-size:21px;font-weight:800;color:var(--text);
  display:flex;align-items:center;gap:10px;letter-spacing:-.02em}
.tb-title i{color:var(--red);font-size:24px;filter:drop-shadow(0 0 6px var(--red-dim))}
.tb-sub{font-size:11px;color:var(--text-3);margin-top:5px;font-weight:500}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:4px 11px;border-radius:20px;font-weight:700;
  display:inline-flex;align-items:center;gap:5px;white-space:nowrap;
  border:1px solid transparent}
.bg-green{background:rgba(16,185,129,0.12);color:#34d399;border-color:rgba(16,185,129,0.25)}
.bg-blue{background:var(--red-dim);color:var(--red-3);border-color:var(--border-2)}
.bg-amber{background:var(--yellow-d);color:var(--yellow);border-color:rgba(245,158,11,0.30)}
.bg-red{background:var(--red-dim);color:var(--red-3);border-color:var(--border-2)}
.bg-purple{background:rgba(168,85,247,0.12);color:#c084fc;border-color:rgba(168,85,247,0.25)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dot.g{background:#22c55e;box-shadow:0 0 6px #22c55e;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}

/* ───── کارت‌های متریک ───── */
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.metric{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:var(--radius);
  padding:18px 18px 14px;position:relative;overflow:hidden;
  transition:all .25s ease;cursor:default;
}
.metric::before{content:'';position:absolute;top:0;right:0;width:3px;
  height:100%;background:var(--red);transform:scaleY(0);transform-origin:top;
  transition:transform .3s ease}
.metric:hover{border-color:var(--border-2);transform:translateY(-3px);
  box-shadow:0 12px 30px rgba(0,0,0,0.4)}
.metric:hover::before{transform:scaleY(1)}
.metric::after{content:'';position:absolute;top:-30px;right:-30px;
  width:80px;height:80px;background:radial-gradient(circle,
  rgba(220,38,38,0.10),transparent 70%);pointer-events:none}
.m-icon{width:38px;height:38px;border-radius:10px;
  background:linear-gradient(135deg,var(--red-dim),rgba(220,38,38,0.05));
  display:flex;align-items:center;justify-content:center;margin-bottom:12px;
  color:var(--red-3);font-size:20px;border:1px solid var(--border-2);
  box-shadow:0 0 12px rgba(220,38,38,0.10)}
.m-icon.suc{background:rgba(16,185,129,0.10);color:#34d399;border-color:rgba(16,185,129,0.25);
  box-shadow:0 0 12px rgba(16,185,129,0.10)}
.m-icon.dan{background:rgba(239,68,68,0.10);color:var(--red-3);border-color:var(--red)}
.m-icon.pur{background:rgba(168,85,247,0.10);color:#c084fc;
  border-color:rgba(168,85,247,0.25)}
.m-label{font-size:9.5px;color:var(--text-3);margin-bottom:5px;
  font-weight:600;text-transform:uppercase;letter-spacing:.07em}
.m-val{font-size:26px;font-weight:800;color:var(--text);
  line-height:1;letter-spacing:-.02em}
.m-val .u{font-size:13px;font-weight:500;color:var(--text-3);margin-right:3px}
.m-sub{font-size:9.5px;color:var(--text-3);margin-top:7px;display:flex;
  align-items:center;gap:4px}

@media(max-width:1100px){.metrics{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.metrics{grid-template-columns:1fr}
"""
DASHBOARD_HTML = DASHBOARD_HTML + r"""
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:14px;margin-bottom:20px}
.traf-main-stat{
  background:linear-gradient(155deg,var(--card-2) 0%,var(--card) 60%);
  border:1px solid var(--border);border-radius:20px;
  padding:24px 26px;position:relative;overflow:hidden;
  box-shadow:var(--shadow)}
.traf-main-stat::before{content:'';position:absolute;top:-60px;left:-60px;
  width:200px;height:200px;
  background:radial-gradient(circle,var(--red-dim),transparent 70%);pointer-events:none}
.traf-main-stat::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,transparent,var(--red),transparent)}
.traf-main-label{font-size:10.5px;color:var(--red-3);font-weight:700;
  text-transform:uppercase;letter-spacing:.10em;margin-bottom:12px;
  display:flex;align-items:center;gap:6px;position:relative}
.traf-main-label i{font-size:14px;filter:drop-shadow(0 0 4px var(--red-dim))}
.traf-main-val{font-size:38px;font-weight:900;color:var(--text);
  line-height:1;letter-spacing:-.03em;display:flex;align-items:baseline;gap:7px;
  font-feature-settings:"tnum"}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--text-3)}
.traf-trend{display:inline-flex;align-items:center;gap:5px;font-size:11px;
  font-weight:700;padding:5px 12px;border-radius:20px;margin-top:14px}
.traf-trend.up{background:rgba(16,185,129,0.12);color:#34d399;border:1px solid rgba(16,185,129,0.25)}
.traf-trend.down{background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)}

.traf-mini{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:18px;
  padding:18px 19px;display:flex;flex-direction:column;
  justify-content:space-between;transition:all .25s ease;position:relative;overflow:hidden}
.traf-mini:hover{border-color:var(--border-2);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:34px;height:34px;border-radius:10px;
  background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2);
  display:flex;align-items:center;justify-content:center;font-size:17px}
.traf-mini-icon.pk{background:var(--yellow-d);color:var(--yellow);
  border-color:rgba(245,158,11,0.30)}
.traf-mini-icon.lo{background:rgba(168,85,247,0.12);color:#c084fc;
  border-color:rgba(168,85,247,0.25)}
.traf-mini-label{font-size:9.5px;color:var(--text-3);font-weight:700;
  text-transform:uppercase;letter-spacing:.07em}
.traf-mini-val{font-size:23px;font-weight:800;color:var(--text);
  letter-spacing:-.02em;font-feature-settings:"tnum"}
.traf-mini-sub{font-size:9.5px;color:var(--text-3);margin-top:4px}

/* ───── کارت ترافیک نمودار ───── */
.traf-chart-card{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:22px;
  padding:24px 26px 18px;box-shadow:var(--shadow);
  margin-bottom:18px;position:relative;overflow:hidden}
.traf-chart-card::after{content:'';position:absolute;top:-60px;left:-60px;
  width:200px;height:200px;background:radial-gradient(circle,
  rgba(245,158,11,0.05),transparent 70%);pointer-events:none}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;
  margin-bottom:8px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:15px;font-weight:800;color:var(--text);
  display:flex;align-items:center;gap:9px}
.traf-chart-title i{color:var(--red-3);font-size:19px;
  filter:drop-shadow(0 0 6px var(--red-dim))}
.traf-chart-sub{font-size:10.5px;color:var(--text-3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;
  font-size:10.5px;color:var(--text-2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px;
  box-shadow:0 0 6px currentColor}
.traf-range-tabs{display:flex;gap:4px;background:var(--red-dim);
  padding:3px;border-radius:10px;border:1px solid var(--border-2)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;
  font-weight:700;color:var(--text-3);cursor:pointer;transition:.15s;
  border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--grad-red);color:#fff;
  box-shadow:0 4px 14px rgba(220,38,38,0.4)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

@media(max-width:1000px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:240px}}

/* ───── باکس VLESS ───── */
.vless-box{
  background:linear-gradient(135deg,var(--card-2) 0%,var(--card) 100%);
  border:1px solid var(--border);border-radius:18px;
  padding:22px 24px;margin-bottom:20px;
  box-shadow:var(--shadow);position:relative;overflow:hidden}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;
  width:200px;height:200px;background:radial-gradient(circle,
  var(--red-dim),transparent 70%);pointer-events:none}
.vless-box::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:var(--grad-fire)}
.vl-header{display:flex;align-items:center;justify-content:space-between;
  margin-bottom:14px;flex-wrap:wrap;gap:10px}
.vl-title{color:var(--red-3);font-size:11px;display:flex;
  align-items:center;gap:7px;font-weight:700;text-transform:uppercase;
  letter-spacing:.07em}
.vl-title i{color:var(--red);font-size:16px;
  filter:drop-shadow(0 0 4px var(--red-dim))}
.vl-code{background:rgba(0,0,0,0.4);border:1px solid var(--border);
  border-radius:10px;padding:14px 16px;font-size:11px;
  font-family:ui-monospace,monospace;color:var(--yellow-3);
  word-break:break-all;line-height:1.8;letter-spacing:.01em;
  position:relative}
.vl-code::before{content:'$';position:absolute;left:14px;top:12px;
  color:var(--red-3);font-weight:700;font-size:14px}
.vl-code{padding-right:14px;padding-left:38px}
.vl-actions{display:flex;gap:9px;margin-top:14px;flex-wrap:wrap}

/* ───── دکمه‌ها ───── */
.btn{font-family:inherit;font-size:12px;font-weight:700;border-radius:10px;
  padding:9px 15px;cursor:pointer;display:inline-flex;
  align-items:center;gap:6px;transition:all .2s ease;
  white-space:nowrap;border:none}
.btn i{font-size:14px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:var(--grad-red);color:#fff;
  box-shadow:0 4px 18px rgba(220,38,38,0.4)}
.btn-p:hover{transform:translateY(-2px);
  box-shadow:0 8px 24px rgba(220,38,38,0.5)}
.btn-p:active{transform:translateY(0) scale(.97)}
.btn-o{background:transparent;border:1.5px solid var(--border-2);color:var(--text-2)}
.btn-o:hover{background:var(--red-dim);color:var(--text);
  border-color:var(--red)}
.btn-g{background:var(--red-dim);border:1.5px solid var(--border-2);
  color:var(--red-3)}
.btn-g:hover{background:rgba(220,38,38,0.20);color:var(--text);
  border-color:var(--red)}
.btn-d{background:var(--red-dim);border:1.5px solid var(--border-2);
  color:var(--red-3)}
.btn-d:hover{background:rgba(220,38,38,0.20)}
.btn-pur{background:rgba(168,85,247,0.12);color:#c084fc;
  border:1.5px solid rgba(168,85,247,0.25)}
.btn-pur:hover{background:rgba(168,85,247,0.20)}
.btn-amber{background:var(--yellow-d);color:var(--yellow);
  border:1.5px solid rgba(245,158,11,0.30)}
.btn-amber:hover{background:rgba(245,158,11,0.20);color:var(--yellow-2)}
.btn-sm{padding:6px 11px;font-size:10.5px;border-radius:7px}
.btn-icon{width:32px;height:32px;padding:0;justify-content:center;
  border-radius:8px;font-size:13px}

/* ───── کارت‌های اطلاعات ───── */
.card{background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius);padding:20px 22px;
  transition:all .25s ease;position:relative;overflow:hidden}
.card:hover{border-color:var(--border-2)}
.card-title{font-size:13px;font-weight:800;color:var(--text);
  margin-bottom:16px;display:flex;align-items:center;gap:8px}
.card-title i{color:var(--red-3);font-size:17px;
  filter:drop-shadow(0 0 4px var(--red-dim))}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:18px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:18px}
.mb16{margin-bottom:16px}

/* ───── لیست‌های اطلاعات ───── */
.sr{display:flex;align-items:center;justify-content:space-between;
  padding:10px 0;border-bottom:1px solid rgba(239,68,68,0.04);
  font-size:12px;transition:.2s}
.sr:hover{background:rgba(239,68,68,0.03);padding-left:10px;border-radius:8px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--text-2);display:flex;align-items:center;gap:7px}
.sr-k i{font-size:14px;color:var(--text-3)}
.sr-v{color:var(--text);font-weight:700;font-size:11.5px}

/* ───── کارت‌های نمودار ───── */
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}

/* ───── چیپ‌ها ───── */
.exp-chip{font-size:9px;padding:3px 9px;border-radius:6px;
  font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:rgba(16,185,129,0.12);color:#34d399;border:1px solid rgba(16,185,129,0.25)}
.ec-warn{background:var(--yellow-d);color:var(--yellow);
  border:1px solid rgba(245,158,11,0.30)}
.ec-exp{background:var(--red-dim);color:var(--red-3);
  border:1px solid var(--border-2)}
.ec-inf{background:var(--red-dim);color:var(--yellow);
  border:1px solid rgba(245,158,11,0.30)}

/* ───── تاگل ───── */
.tog{width:42px;height:22px;border-radius:22px;
  background:rgba(100,100,100,0.25);position:relative;cursor:pointer;
  transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:16px;height:16px;
  border-radius:50%;background:#fff;left:3px;top:3px;
  transition:.2s;box-shadow:0 2px 4px rgba(0,0,0,.4)}
.tog.on{background:linear-gradient(90deg,var(--red),var(--yellow))}
.tog.on::after{left:23px}

/* ───── فرم‌ها ───── */
.form-row{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:6px}
.fg label{font-size:10px;color:var(--text-3);font-weight:700;
  text-transform:uppercase;letter-spacing:.07em}
.fi,.fs{padding:9px 13px;border-radius:9px;border:1px solid var(--border);
  background:rgba(0,0,0,0.40);color:var(--text);font-family:inherit;
  font-size:12px;outline:none;transition:.15s;min-width:100px}
.fi::placeholder{color:var(--text-4)}
.fi:focus,.fs:focus{border-color:var(--red);
  background:rgba(0,0,0,0.7);box-shadow:0 0 0 3px var(--red-dim)}
.fs option{background:var(--card-2);color:var(--text)}

/* ───── توضیحات ───── */
.cl{background:var(--red-dim);border:1px solid var(--border-2);
  border-radius:10px;padding:11px 14px;font-size:11px;
  color:var(--text-2);display:flex;gap:9px;align-items:flex-start;
  line-height:1.8;margin-top:14px}
.cl i{font-size:16px;color:var(--red-3);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--yellow-d);border-color:rgba(245,158,11,0.30);
  color:var(--yellow)}

/* ───── پنل ساخت کانفیگ ───── */
.create-panel{
  background:linear-gradient(155deg,var(--card-2) 0%,var(--card) 55%);
  border:1px solid var(--border);border-radius:22px;
  padding:0;overflow:hidden;box-shadow:var(--shadow);
  margin-bottom:18px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;
  width:220px;height:220px;background:radial-gradient(circle,
  var(--red-dim),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:14px;padding:24px 26px 18px;
  position:relative;background:linear-gradient(90deg,rgba(239,68,68,0.10),transparent);
  border-bottom:1px solid var(--border)}
.cp-head-icon{width:48px;height:48px;border-radius:14px;
  background:var(--grad-fire);display:flex;align-items:center;
  justify-content:center;color:#000;font-size:24px;flex-shrink:0;
  box-shadow:0 0 0 3px var(--red-dim),0 8px 24px rgba(220,38,38,0.4);
  position:relative;overflow:hidden}
.cp-head-icon::after{content:'';position:absolute;inset:0;
  background:linear-gradient(45deg,transparent,rgba(255,255,255,0.4),transparent);
  animation:shine 3s infinite}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:17px;font-weight:800;background:var(--grad-red);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;letter-spacing:-.02em}
.cp-head-sub{font-size:11px;color:var(--text-3);margin-top:3px}
.cp-body{padding:22px 26px;position:relative}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-bottom:18px}
.cp-block{background:rgba(0,0,0,0.30);border:1px solid var(--border);
  border-radius:14px;padding:16px 18px;position:relative;
  transition:.25s}
.cp-block:hover{border-color:var(--border-2)}
.cp-block::before{content:'';position:absolute;top:0;left:0;
  width:3px;height:30%;background:var(--red);border-radius:14px 0 0 0}
.cp-block-label{font-size:10px;font-weight:800;color:var(--red-3);
  text-transform:uppercase;letter-spacing:.10em;display:flex;
  align-items:center;gap:6px;margin-bottom:12px}
.cp-block-label i{color:var(--red);font-size:15px}
.cp-input-full{width:100%;padding:11px 14px;border-radius:10px;
  border:1px solid var(--border);background:rgba(0,0,0,0.45);
  color:var(--text);font-family:inherit;font-size:12.5px;
  outline:none;transition:.15s}
.cp-input-full:focus{border-color:var(--red);
  box-shadow:0 0 0 3px var(--red-dim);background:rgba(0,0,0,0.7)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px;flex-wrap:wrap}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 80px}

/* ───── چیپ‌های انتخاب سریع ───── */
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:6px 13px;border-radius:9px;
  background:var(--red-dim);color:var(--text-2);
  border:1px solid var(--border-2);cursor:pointer;
  transition:.15s;white-space:nowrap;font-family:inherit}
.chip:hover{background:rgba(220,38,38,0.20);color:var(--text);
  border-color:var(--red)}
.chip.active{background:var(--grad-red);color:#fff;border-color:var(--red);
  box-shadow:0 4px 14px rgba(220,38,38,0.4)}

/* ───── کارت پروتکل ───── */
.proto-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:9px}
.proto-card{border:1.5px solid var(--border);border-radius:14px;
  padding:14px 13px;cursor:pointer;transition:.2s ease;
  text-align:center;position:relative;background:var(--card-2);
  display:flex;flex-direction:column;align-items:center;gap:6px}
.proto-card:hover{border-color:var(--border-2);transform:translateY(-2px);
  box-shadow:0 6px 18px rgba(0,0,0,0.3)}
.proto-card.active{border-color:var(--red);background:linear-gradient(180deg,
  rgba(220,38,38,0.20),rgba(220,38,38,0.05));
  box-shadow:0 0 0 1px var(--red),0 8px 24px rgba(220,38,38,0.20)}
.proto-card-check{position:absolute;top:8px;left:8px;
  width:18px;height:18px;border-radius:50%;background:var(--red);
  color:#fff;font-size:11px;display:flex;align-items:center;
  justify-content:center;opacity:0;transform:scale(.5);
  transition:.2s;box-shadow:0 0 8px var(--red-3)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-icon{width:34px;height:34px;border-radius:10px;
  background:var(--red-dim);color:var(--red-3);font-size:18px;
  display:flex;align-items:center;justify-content:center;
  border:1px solid var(--border-2)}
.proto-card.active .proto-card-icon{background:var(--grad-red);color:#fff;
  border:none;box-shadow:0 4px 12px rgba(220,38,38,0.4)}
.proto-card-title{font-size:11px;font-weight:800;color:var(--text)}
.proto-card-desc{font-size:8.5px;color:var(--text-3);line-height:1.5}
.proto-card.active .proto-card-desc{color:var(--red-3)}

/* ───── پاورقی پنل ساخت ───── */
.cp-footer{display:flex;align-items:center;justify-content:space-between;
  gap:14px;padding-top:18px;border-top:1px solid var(--border);
  flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:9px;font-size:10.5px;
  color:var(--text-3);line-height:1.7;flex:1;min-width:230px}
.cp-footer-note i{color:var(--red-3);font-size:16px;flex-shrink:0}
.cp-submit-btn{
  background:var(--grad-red);color:#fff;border:none;border-radius:13px;
  padding:14px 28px;font-family:inherit;font-size:13.5px;
  font-weight:800;cursor:pointer;display:flex;align-items:center;
  gap:9px;transition:.25s;box-shadow:0 6px 24px rgba(220,38,38,0.4);
  white-space:nowrap;position:relative;overflow:hidden}
.cp-submit-btn::before{content:'';position:absolute;inset:0;
  background:linear-gradient(120deg,transparent,rgba(255,255,255,0.3),transparent);
  transform:translateX(-100%);transition:.7s}
.cp-submit-btn:hover{transform:translateY(-2px);
  box-shadow:0 10px 30px rgba(220,38,38,0.5)}
.cp-submit-btn:hover::before{transform:translateX(100%)}
.cp-submit-btn:active{transform:translateY(0) scale(.97)}

@media(max-width:780px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr 1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}

/* ───── لیست کانفیگ ───── */
.cfg-grid{display:flex;flex-direction:column;gap:11px}
.cfg-card{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:14px;padding:0;
  transition:all .25s ease;position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--border-2);
  box-shadow:0 8px 26px rgba(0,0,0,0.35);transform:translateY(-2px)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:10px;height:10px;border-radius:50%;
  background:var(--green);flex-shrink:0;
  box-shadow:0 0 0 3px rgba(16,185,129,0.20),0 0 10px rgba(16,185,129,0.5)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);
  box-shadow:0 0 0 3px var(--red-dim),0 0 10px var(--red-2)}
.cfg-card.is-exp .cfg-status-dot{background:var(--yellow);
  box-shadow:0 0 0 3px var(--yellow-d),0 0 10px var(--yellow)}
.cfg-identity{display:flex;flex-direction:column;gap:4px;min-width:160px;
  flex-shrink:0}
.cfg-label{font-size:14px;font-weight:700;color:var(--text);
  display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;
  font-size:10px;color:var(--text-3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;
  color:var(--yellow-3);background:var(--red-dim);
  border:1px solid var(--border-2);padding:2px 7px;border-radius:5px;
  cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:rgba(220,38,38,0.20);
  border-color:var(--red);color:var(--text)}
.cfg-divider-v{width:1px;align-self:stretch;
  background:var(--border);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:170px;display:flex;
  flex-direction:column;gap:6px}
.ubar{height:6px;border-radius:4px;
  background:rgba(220,38,38,0.10);overflow:hidden;position:relative}
.ubar-f{height:100%;border-radius:4px;transition:width .5s ease;
  position:relative;overflow:hidden}
.ubar-f::after{content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.3),transparent);
  animation:shimmer 2s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
.utxt{font-size:9.5px;color:var(--text-3);display:flex;
  justify-content:space-between;font-feature-settings:"tnum"}
.utxt b{color:var(--text-2);font-weight:700}
.cfg-exp-col{flex-shrink:0;min-width:115px;text-align:center}
.cfg-badges-col{display:flex;flex-direction:column;gap:6px;
  flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:8.5px;padding:4px 9px;border-radius:6px;
  font-weight:700;white-space:nowrap;letter-spacing:.03em}
.pc-ws{background:var(--red-dim);color:var(--red-3);
  border:1px solid var(--border-2)}
.pc-xhttp{background:rgba(168,85,247,0.12);color:#c084fc;
  border:1px solid rgba(168,85,247,0.25)}
.pc-trojan{background:var(--yellow-d);color:var(--yellow);
  border:1px solid rgba(245,158,11,0.30)}
.pc-ss{background:rgba(16,185,129,0.12);color:#34d399;
  border:1px solid rgba(16,185,129,0.25)}
.cfg-sub-tag{font-size:9px;color:var(--text-3);
  display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:#c084fc;font-size:11px}

/* ───── ریسپانسیو لیست کانفیگ ───── */
@media(max-width:900px){
  .cfg-row{flex-wrap:wrap}
  .cfg-divider-v{display:none}
  .cfg-usage-col{min-width:100%;order:4}
}
@media(max-width:780px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:14px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:13px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:11px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--border);
    padding-top:11px;margin-top:2px;width:100%}
}

/* ───── صفحه گروه‌های ساب ───── */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;
  gap:13px;margin-bottom:18px;flex-wrap:wrap}
.subs-search{flex:1;min-width:220px;position:relative}
.subs-search input{width:100%;padding:12px 42px 12px 17px;border-radius:12px;
  border:1.5px solid var(--border);background:var(--card);
  color:var(--text);font-family:inherit;font-size:13px;outline:none;
  transition:.15s}
.subs-search input:focus{border-color:var(--red);
  box-shadow:0 0 0 3px var(--red-dim)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);
  color:var(--text-3);font-size:15px}

.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));
  gap:16px;margin-bottom:20px}
.sub-card{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:20px;
  padding:0;overflow:hidden;transition:all .25s ease;position:relative}
.sub-card:hover{border-color:var(--border-2);transform:translateY(-4px);
  box-shadow:0 16px 36px rgba(0,0,0,0.30)}
.sub-card-top{background:linear-gradient(155deg,rgba(168,85,247,0.10),transparent 65%);
  padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;
  width:130px;height:130px;background:radial-gradient(circle,
  rgba(168,85,247,0.15),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:14px;position:relative}
.sub-card-icon{width:46px;height:46px;border-radius:14px;
  background:linear-gradient(135deg,#a855f7,#7e22ce);color:#fff;font-size:20px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  box-shadow:0 6px 18px rgba(168,85,247,0.40)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:16px;font-weight:800;color:var(--text);
  letter-spacing:-.01em;white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--text-3);margin-top:3px;
  line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;
  -webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:28px;height:28px;border-radius:9px;
  display:flex;align-items:center;justify-content:center;font-size:13px}
.sub-card-lock-badge.locked{background:var(--yellow-d);color:var(--yellow);
  border:1px solid rgba(245,158,11,0.30)}
.sub-card-lock-badge.open{background:rgba(16,185,129,0.12);color:#34d399;
  border:1px solid rgba(16,185,129,0.25)}

.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;
  position:relative;margin-top:16px;background:rgba(0,0,0,0.40);
  border:1px solid var(--border);border-radius:13px;overflow:hidden}
.sub-card-stat{padding:12px 8px;text-align:center;
  border-left:1px solid var(--border)}
.sub-card-stat:first-child{border-left:none}
.sub-card-stat-val{font-size:16px;font-weight:800;color:var(--text);
  line-height:1.2;font-feature-settings:"tnum"}
.sub-card-stat-label{font-size:8.5px;color:var(--text-3);
  font-weight:700;text-transform:uppercase;letter-spacing:.06em;
  margin-top:5px}

.sub-card-url-row{margin:14px 20px 0;background:rgba(168,85,247,0.10);
  border:1px dashed rgba(168,85,247,0.30);border-radius:11px;
  padding:9px 12px;display:flex;align-items:center;gap:8px;min-width:0}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;
  color:#c084fc;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
  min-width:0}
.sub-card-url-copy{background:none;border:none;color:#c084fc;cursor:pointer;
  font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:#e9d5ff;transform:scale(1.1)}

.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}

/* ───── خالی ───── */
.subs-empty-v2,.conn-empty-v2{
  text-align:center;padding:70px 20px;background:var(--card);
  border:1.5px dashed var(--border-2);border-radius:20px;
  grid-column:1/-1}
.subs-empty-v2-icon,.conn-empty-v2-icon{
  width:64px;height:64px;border-radius:18px;background:var(--red-dim);
  display:flex;align-items:center;justify-content:center;
  font-size:28px;color:#c084fc;margin:0 auto 16px;border:1px solid rgba(168,85,247,0.25)}
.conn-empty-v2-icon{color:var(--text-3);border-color:var(--border-2)}
.subs-empty-v2-title,.conn-empty-v2-title{font-size:13.5px;font-weight:700;
  color:var(--text-2);margin-bottom:6px}
.subs-empty-v2-sub,.conn-empty-v2-sub{font-size:11px;color:var(--text-3)}

@media(max-width:520px){
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
  .sub-card-stats{grid-template-columns:repeat(3,1fr)}
}
"""
DASHBOARD_HTML = DASHBOARD_HTML + r"""
/* ───── کارت‌های مودال V2 ───── */
.modal-bg,.qr-modal{display:none;position:fixed;inset:0;
  background:rgba(0,0,0,0.70);z-index:500;align-items:center;
  justify-content:center;backdrop-filter:blur(6px);padding:20px}
.modal-bg.open,.qr-modal.open{display:flex}
.modal-v2{
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border-2);border-radius:22px;
  padding:0;max-width:480px;width:calc(100% - 32px);
  max-height:92vh;overflow-y:auto;position:relative;
  animation:modal-in .25s cubic-bezier(.4,0,.2,1);
  box-shadow:0 24px 70px rgba(0,0,0,0.5),0 0 0 1px rgba(239,68,68,0.10)}
@keyframes modal-in{from{opacity:0;transform:scale(.95) translateY(20px)}to{opacity:1;transform:none}}
.modal-v2-head{
  background:linear-gradient(155deg,rgba(168,85,247,0.16),transparent 65%);
  padding:20px 24px 16px;position:relative;overflow:hidden;
  border-bottom:1px solid var(--border)}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;
  width:180px;height:180px;background:radial-gradient(circle,
  rgba(168,85,247,0.20),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;
  background:var(--red-dim);border:1px solid var(--border-2);
  color:var(--text-2);width:32px;height:32px;border-radius:8px;
  font-size:15px;display:flex;align-items:center;
  justify-content:center;cursor:pointer;z-index:5;transition:.15s}
.modal-v2-close:hover{background:var(--red-dim);border-color:var(--red);
  color:var(--red-3)}
.modal-v2-icon{width:44px;height:44px;border-radius:13px;
  background:linear-gradient(135deg,#a855f7,#7e22ce);color:#fff;font-size:20px;
  display:flex;align-items:center;justify-content:center;margin-bottom:13px;
  position:relative;z-index:1;box-shadow:0 8px 22px rgba(168,85,247,0.50)}
.modal-v2-title{font-size:17px;font-weight:800;color:var(--text);
  position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:11px;color:var(--text-3);margin-top:4px;
  position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:18px 24px 22px;border-top:1px solid var(--border)}
.modal-v2-field{margin-bottom:13px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;
  font-size:9.5px;font-weight:800;color:var(--text-2);
  text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}
.modal-v2-field label i{color:#c084fc;font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:14px;top:50%;
  transform:translateY(-50%);color:var(--text-3);font-size:14px;
  pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:10px 40px 10px 14px;border-radius:11px;
  border:1px solid var(--border);background:rgba(0,0,0,0.30);
  color:var(--text);font-family:inherit;font-size:12.5px;
  outline:none;transition:.15s}
.modal-v2-input:focus{border-color:#a855f7;
  box-shadow:0 0 0 3px rgba(168,85,247,0.12);background:rgba(0,0,0,0.50)}
.modal-v2-input:focus~i{color:#c084fc}
.modal-v2-input::placeholder{color:var(--text-4)}
.modal-v2-hint{background:var(--red-dim);
  border:1px solid var(--border-2);border-radius:11px;padding:10px 13px;
  font-size:10px;color:var(--text-2);display:flex;gap:8px;align-items:flex-start;
  line-height:1.6;margin-top:3px}
.modal-v2-hint i{font-size:14px;color:var(--red-3);
  margin-top:2px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:9px;margin-top:17px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:11px;border-radius:11px;
  background:transparent;border:1.5px solid var(--border-2);
  color:var(--text-2);font-family:inherit;font-size:12px;font-weight:700;
  cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--red-dim);color:var(--text);
  border-color:var(--red)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:11px;border-radius:11px;
  background:linear-gradient(135deg,#a855f7,#7e22ce);color:#fff;border:none;
  font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;
  display:flex;align-items:center;gap:6px;transition:.15s;
  box-shadow:0 6px 22px rgba(168,85,247,0.40)}
.modal-v2-btn-submit:hover{transform:translateY(-2px);
  box-shadow:0 10px 30px rgba(168,85,247,0.50)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.97)}

/* ───── کارت مودال مولفه V2 (lmodal) ───── */
.lmodal-head{background:linear-gradient(155deg,var(--red-dim) 0%,transparent 70%);
  padding:24px 26px 18px;position:relative;border-bottom:1px solid var(--border)}
.lmodal-head::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:var(--grad-fire)}
.lmodal-icon-row{display:flex;align-items:center;gap:13px;position:relative;z-index:1}
.lmodal-icon{width:46px;height:46px;border-radius:14px;
  background:var(--grad-fire);color:#000;font-size:22px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  box-shadow:0 6px 22px rgba(220,38,38,0.40)}
.lmodal-title-v2{font-size:15px;font-weight:800;color:var(--text)}
.lmodal-sub-v2{font-size:10.5px;color:var(--text-3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;
  border:1px solid var(--border);background:rgba(0,0,0,0.30);
  color:var(--text);font-family:inherit;font-size:12px;outline:none}
.lmodal-search input:focus{border-color:var(--red);
  box-shadow:0 0 0 3px var(--red-dim)}
.lmodal-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);
  color:var(--text-3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:12px;position:relative;z-index:1;
  flex-wrap:wrap;align-items:center}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 12px;border-radius:9px;
  background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2);
  cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(220,38,38,0.20);border-color:var(--red)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--text-3);
  display:flex;align-items:center}

.lmodal-list{padding:12px 14px;max-height:380px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 13px;
  border-radius:13px;cursor:pointer;transition:.15s;
  margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--red-dim);
  border-color:var(--border-2)}
.lrow-v2.checked{background:linear-gradient(90deg,rgba(220,38,38,0.12),
  rgba(220,38,38,0.04));border-color:var(--red)}
.lrow-v2-check{width:22px;height:22px;border-radius:7px;border:2px solid var(--border-2);
  flex-shrink:0;display:flex;align-items:center;justify-content:center;
  transition:.15s;background:rgba(0,0,0,0.30)}
.lrow-v2.checked .lrow-v2-check{background:var(--grad-red);border-color:var(--red);
  box-shadow:0 0 10px var(--red-3)}
.lrow-v2-check i{font-size:14px;color:#fff;opacity:0;transform:scale(.5);
  transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:36px;height:36px;border-radius:10px;
  background:var(--red-dim);color:var(--red-3);font-size:16px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  border:1px solid var(--border-2)}
.lrow-v2.checked .lrow-v2-avatar{background:var(--grad-red);color:#fff;
  border:none;box-shadow:0 4px 14px rgba(220,38,38,0.35)}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:13px;font-weight:700;color:var(--text);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--text-3);margin-top:2px;display:flex;
  align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:4px 10px;border-radius:20px;
  flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:rgba(16,185,129,0.12);color:#34d399;
  border:1px solid rgba(16,185,129,0.25)}
.lrow-v2-status.off{background:var(--red-dim);color:var(--red-3);
  border:1px solid var(--border-2)}

.lmodal-footer{display:flex;align-items:center;justify-content:space-between;
  gap:11px;padding:18px 26px;border-top:1px solid var(--border);
  background:rgba(0,0,0,0.40)}
.lmodal-footer-info{font-size:10.5px;color:var(--text-3);
  display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--red-3);font-size:14px}
.lmodal-footer-btns{display:flex;gap:9px}

@media(max-width:520px){.sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr;
  .sub-card-stats{grid-template-columns:repeat(3,1fr)}}}

.modal{background:var(--card);border:1px solid var(--border);
  border-radius:20px;padding:30px 28px;max-width:520px;width:calc(100% - 32px);
  max-height:90vh;overflow-y:auto;position:relative;
  animation:modal-in .25s ease}
.modal-close{position:absolute;top:14px;left:14px;
  background:var(--red-dim);border:1px solid var(--border-2);
  color:var(--text-2);width:32px;height:32px;border-radius:8px;
  font-size:16px;display:flex;align-items:center;
  justify-content:center;cursor:pointer;border:none}
.modal-title{font-size:17px;font-weight:800;color:var(--text);
  margin-bottom:20px;display:flex;align-items:center;gap:9px}
.modal-title i{color:var(--red-3);font-size:19px;
  filter:drop-shadow(0 0 4px var(--red-dim))}
.lrow{display:flex;align-items:center;gap:9px;padding:7px 0;
  border-bottom:1px solid rgba(239,68,68,0.05)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:18px;height:18px;border-radius:5px;cursor:pointer;
  accent-color:var(--red)}
.lrow-label{flex:1;font-size:12px;color:var(--text)}
.lrow-badge{font-size:9px;padding:2px 8px;border-radius:5px;
  background:rgba(16,185,129,0.12);color:#34d399;font-weight:700;
  border:1px solid rgba(16,185,129,0.25)}

/* ───── تاست ───── */
.toast{
  position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(60px);
  background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border-2);color:var(--text);
  border-radius:14px;padding:11px 20px;font-size:12px;font-weight:700;
  opacity:0;transition:all .3s cubic-bezier(.4,0,.2,1);
  z-index:9999;pointer-events:none;
  display:flex;align-items:center;gap:9px;
  box-shadow:0 12px 36px rgba(0,0,0,0.5),0 0 0 1px rgba(239,68,68,0.15);
  white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,0.35);
  box-shadow:0 12px 36px rgba(0,0,0,0.5),0 0 0 1px rgba(16,185,129,0.20);
  background:linear-gradient(145deg,rgba(16,185,129,0.18),var(--card))}
.toast.err{border-color:var(--red-dim);
  background:linear-gradient(145deg,rgba(239,68,68,0.18),var(--card))}
.toast.ok i,.toast.err i{font-size:16px}

.dash-footer{border-top:1px solid var(--border);margin-top:18px;
  padding-top:16px;display:flex;align-items:center;
  justify-content:space-between;flex-wrap:wrap;gap:10px}
.df-text{font-size:10px;color:var(--text-3)}
.df-link{font-size:11.5px;color:var(--red-3);
  display:flex;align-items:center;gap:6px;font-weight:700;
  text-decoration:none;transition:.15s}
.df-link:hover{color:var(--red-2)}
.df-link i{font-size:14px}

/* ───── هیرو اتصال ───── */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:20px}
.conn-hero-tile{
  background:var(--card);border:1px solid var(--border);
  border-radius:18px;padding:18px 19px;position:relative;
  overflow:hidden;transition:.2s}
.conn-hero-tile:hover{border-color:var(--border-2);transform:translateY(-2px);
  box-shadow:0 10px 28px rgba(0,0,0,0.35)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;
  height:2px;background:linear-gradient(90deg,transparent,var(--red),transparent)}
.conn-hero-icon{width:34px;height:34px;border-radius:10px;
  background:rgba(16,185,129,0.10);color:#34d399;font-size:17px;
  display:flex;align-items:center;justify-content:center;
  margin-bottom:11px;border:1px solid rgba(16,185,129,0.25)}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--red-dim);
  color:var(--red-3);border-color:var(--border-2)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:rgba(168,85,247,0.12);
  color:#c084fc;border-color:rgba(168,85,247,0.25)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--yellow-d);
  color:var(--yellow);border-color:rgba(245,158,11,0.30)}
.conn-hero-label{font-size:9.5px;color:var(--text-3);font-weight:700;
  text-transform:uppercase;letter-spacing:.07em;margin-bottom:5px}
.conn-hero-val{font-size:22px;font-weight:800;color:var(--text);
  line-height:1;letter-spacing:-.02em;font-feature-settings:"tnum"}
.conn-hero-unit{font-size:11px;color:var(--text-3);font-weight:500}

.conn-toolbar{display:flex;align-items:center;justify-content:space-between;
  gap:11px;margin-bottom:16px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12.5px;font-weight:800;color:var(--text-2);
  display:flex;align-items:center;gap:8px;text-transform:uppercase;
  letter-spacing:.07em}
.conn-toolbar-title i{color:#34d399;font-size:16px;
  filter:drop-shadow(0 0 4px rgba(16,185,129,0.5))}
.conn-live-badge{display:flex;align-items:center;gap:6px;
  font-size:10.5px;font-weight:700;color:#34d399;
  background:rgba(16,185,129,0.10);padding:5px 12px;border-radius:20px;
  border:1px solid rgba(16,185,129,0.20)}
.conn-live-dot{width:7px;height:7px;border-radius:50%;
  background:#22c55e;animation:pulse 1.6s infinite;
  box-shadow:0 0 8px #22c55e}

.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
  gap:15px}
.conn-card-v2{background:linear-gradient(145deg,var(--card-2),var(--card));
  border:1px solid var(--border);border-radius:18px;
  padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);
  position:relative}
.conn-card-v2:hover{border-color:var(--red-dim);
  transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,0.35)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;
  width:140px;height:140px;background:radial-gradient(circle,
  rgba(16,185,129,0.10),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:13px;
  padding:16px 18px 14px;position:relative}
.conn-avatar{width:44px;height:44px;border-radius:13px;
  background:linear-gradient(135deg,var(--green),#22c55e);
  color:#fff;font-size:19px;display:flex;align-items:center;
  justify-content:center;flex-shrink:0;position:relative;
  box-shadow:0 4px 14px rgba(16,185,129,0.40)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;
  border-radius:16px;border:1.5px solid var(--green);
  opacity:.4;animation:breathe 2.4s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.15);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14.5px;font-weight:800;
  color:var(--text);display:flex;align-items:center;gap:6px;
  letter-spacing:.02em}
.conn-ip-copy{background:none;border:none;color:var(--text-3);
  cursor:pointer;font-size:13px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--red-3)}
.conn-label-v2{font-size:10.5px;color:var(--text-3);margin-top:2px;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;
  padding:4px 10px;border-radius:20px;background:rgba(16,185,129,0.12);
  color:#34d399;display:flex;align-items:center;gap:4px;
  white-space:nowrap;flex-shrink:0;border:1px solid rgba(16,185,129,0.25)}
.conn-card-v2-divider{height:1px;
  background:linear-gradient(90deg,transparent,var(--border-2) 15%,
  var(--border-2) 85%,transparent);margin:0 18px}
.conn-card-v2-body{padding:14px 18px 16px}
.conn-proto-row{margin-bottom:13px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-bottom:13px}
.conn-stat-box{display:flex;align-items:center;gap:9px}
.conn-stat-icon{width:28px;height:28px;border-radius:8px;
  background:var(--red-dim);color:var(--red-3);
  display:flex;align-items:center;justify-content:center;font-size:13px;
  flex-shrink:0;border:1px solid var(--border-2)}
.conn-stat-icon.time{background:rgba(168,85,247,0.12);color:#c084fc;
  border-color:rgba(168,85,247,0.25)}
.conn-stat-text-label{font-size:8.5px;color:var(--text-3);
  font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.conn-stat-text-val{font-size:12px;font-weight:700;color:var(--text);
  margin-top:2px}
.conn-duration-track{height:6px;border-radius:4px;
  background:var(--red-dim);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;
  background:linear-gradient(90deg,var(--green),#22c55e);position:relative;
  overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.35),transparent);
  width:40%;animation:shimmer 1.8s linear infinite}

/* ───── ریسپانسیو اتصال ───── */
@media(max-width:780px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.conn-hero{grid-template-columns:1fr}}

/* ───── خالی و لود ───── */
.empty{text-align:center;padding:55px 20px;color:var(--text-3)}
.empty i{font-size:42px;opacity:.3;margin-bottom:14px;display:block}
.empty p{font-size:12.5px;margin-top:5px;color:var(--text-3)}
.sub-empty,.conn-empty{display:none}
.empty-state{text-align:center;padding:70px 20px;background:transparent;
  color:var(--text-3)}
.empty-state i{font-size:42px;opacity:.3;margin-bottom:14px;display:block}

/* ───── لگ ───── */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:13px;padding:11px 0;
  border-bottom:1px solid rgba(239,68,68,0.04);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:32px;height:32px;border-radius:9px;
  display:flex;align-items:center;justify-content:center;
  font-size:15px;flex-shrink:0}
.log-ic.ok{background:rgba(16,185,129,0.12);color:#34d399;
  border:1px solid rgba(16,185,129,0.25)}
.log-ic.err{background:var(--red-dim);color:var(--red-3);
  border:1px solid var(--border-2)}
.log-ic.warn{background:var(--yellow-d);color:var(--yellow);
  border:1px solid rgba(245,158,11,0.30)}
.log-ic.info{background:var(--red-dim);color:var(--red-3);
  border:1px solid var(--border-2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--text);line-height:1.6}
.log-time{font-size:9.5px;color:var(--text-3);margin-top:2px;
  display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;
  background:var(--red-dim);color:var(--red-3);font-weight:700;
  text-transform:uppercase;letter-spacing:.04em;
  border:1px solid var(--border-2)}
.erow{padding:10px 0;border-bottom:1px solid rgba(239,68,68,0.05)}
.erow:last-child{border-bottom:none}
.etime{color:var(--text-3);font-size:9.5px;margin-bottom:4px;
  display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-3);font-family:ui-monospace,monospace;
  background:var(--red-dim);padding:6px 9px;border-radius:6px;
  word-break:break-all;font-size:10.5px;
  border:1px solid var(--border-2)}

/* ───── سرور پنل ───── */
.srv-panel{
  background:linear-gradient(155deg,var(--card-2) 0%,var(--card) 60%);
  border:1px solid var(--border);border-radius:22px;
  overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;
  width:200px;height:200px;background:radial-gradient(circle,
  var(--red-dim),transparent 70%);pointer-events:none}
.srv-panel::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:var(--grad-fire)}
.srv-hero{display:flex;align-items:center;gap:15px;padding:24px 26px;
  position:relative;border-bottom:1px solid var(--border)}
.srv-hero-icon{width:54px;height:54px;border-radius:15px;
  background:var(--grad-fire);color:#000;font-size:24px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  box-shadow:0 6px 22px rgba(220,38,38,0.40);
  animation:pulse-shadow 3s ease-in-out infinite}
@keyframes pulse-shadow{0%,100%{box-shadow:0 6px 22px rgba(220,38,38,0.40)}
  50%{box-shadow:0 6px 30px rgba(220,38,38,0.70)}}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:16px;font-weight:800;color:var(--text);
  word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--text-3);margin-top:4px;
  display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:12px;
  padding:22px 22px 22px;position:relative}
.srv-tile{display:flex;align-items:center;gap:12px;
  background:rgba(0,0,0,0.30);border:1px solid var(--border);
  border-radius:13px;padding:13px 14px;transition:.2s}
.srv-tile:hover{border-color:var(--border-2);transform:translateY(-1px)}
.srv-tile-icon{width:36px;height:36px;border-radius:10px;
  background:var(--red-dim);color:var(--red-3);
  display:flex;align-items:center;justify-content:center;font-size:17px;
  flex-shrink:0;border:1px solid var(--border-2)}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--text-3);font-weight:700;
  text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--text);
  word-break:break-word}

/* ───── پنل رمز ───── */
.pw-panel{
  background:linear-gradient(155deg,var(--card-2) 0%,var(--card) 60%);
  border:1px solid var(--border);border-radius:22px;
  overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;
  width:200px;height:200px;background:radial-gradient(circle,
  rgba(168,85,247,0.15),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:15px;padding:24px 26px 18px;
  position:relative}
.pw-hero-icon{width:54px;height:54px;border-radius:15px;
  background:linear-gradient(135deg,#a855f7,#7e22ce);color:#fff;font-size:24px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  box-shadow:0 6px 22px rgba(168,85,247,0.40)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:16px;font-weight:800;color:var(--text)}
.pw-hero-sub{font-size:10.5px;color:var(--text-3);margin-top:3px}
.pw-body{padding:5px 26px 22px;position:relative}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;
  color:var(--text-2);text-transform:uppercase;letter-spacing:.07em;
  margin-bottom:7px}
.pw-input{width:100%;padding:11px 44px 11px 14px;border-radius:11px;
  border:1px solid var(--border);background:rgba(0,0,0,0.30);
  color:var(--text);font-family:inherit;font-size:12.5px;
  outline:none;transition:.15s}
.pw-input:focus{border-color:#a855f7;
  box-shadow:0 0 0 3px rgba(168,85,247,0.12)}
.pw-eye{position:absolute;left:12px;top:36px;background:none;
  border:none;color:var(--text-3);cursor:pointer;font-size:16px;
  padding:4px;display:flex}
.pw-eye:hover{color:#c084fc}
.pw-strength{height:5px;border-radius:4px;background:var(--red-dim);
  margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:4px;
  background:rgba(100,100,100,.20);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--text-3);margin-top:5px;
  display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:5px 11px;border-radius:7px;
  background:var(--red-dim);color:var(--text-3);font-weight:600;
  display:flex;align-items:center;gap:4px;transition:.18s;
  border:1px solid var(--border-2)}
.pw-req.met{background:rgba(16,185,129,0.12);color:#34d399;
  border:1px solid rgba(16,185,129,0.25)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,#a855f7,#7e22ce);
  color:#fff;border:none;border-radius:13px;padding:13px;
  font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;
  display:flex;align-items:center;gap:9px;
  box-shadow:0 6px 22px rgba(168,85,247,0.40);transition:.18s}
.pw-submit:hover{transform:translateY(-2px);
  box-shadow:0 10px 28px rgba(168,85,247,0.50)}
.pw-submit:active{transform:translateY(0) scale(.97)}

/* ───── پنل تنظیمات سایت - قابلیت‌های سفارشی ───── */
@media(max-width:1100px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,0.5)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
}
@media(max-width:520px){
  .main{padding:62px 12px 50px}
  .g2,.g3{grid-template-columns:1fr}
}

@keyframes spin{to{transform:rotate(360deg)}}
@keyframes modal-in{from{opacity:0;transform:scale(.95) translateY(20px)}to{opacity:1;transform:none}}
</style></head><body>
<div class="bg-fx"></div><div class="grd-fx"></div>

<div class="toast" id="toast"></div>

<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:550px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--red-3)">—</span></div>
          <div class="lmodal-sub-v2">کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> لغو همه</button>
        <span class="lmodal-count" id="lmodal-count">۰ انتخاب شده</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">در حال بارگذاری...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> تغییرات بلافاصله اعمال می‌شود</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">بستن</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> ذخیره</button>
      </div>
    </div>
  </div>
</div>

<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ساخت گروه جدید</div>
      <div class="modal-v2-sub">یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثلاً: کانال تلگرام">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه درباره این گروه">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> رمز صفحه پابلیک (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی بگذارید = بدون رمز">
      </div>
      <div class="modal-v2-hint" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.</span></div>
      <div class="modal-v2-footer">
        <button class="modal-v2-btn-cancel" onclick="closeModal('modal-create-sub')">انصراف</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> ساخت گروه</button>
      </div>
    </div>
  </div>
</div>

<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:16px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>

<div class="modal-bg" id="modal-res">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-res')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> نماینده جدید</div>
    <div class="fg" style="margin-bottom:10px"><label>نام</label><input class="fi" id="r-name" style="width:100%"></div>
    <div class="fg" style="margin-bottom:10px"><label>رمز</label><input class="fi" id="r-pw" type="password" style="width:100%"></div>
    <div class="fg" style="margin-bottom:15px"><label>حجم (GB)</label><input class="fi" id="r-gb" type="number" style="width:100%"></div>
    <button class="btn btn-p" onclick="createReseller()"><i class="ti ti-user-plus"></i> ذخیره</button>
    </div>
  </div>
</div>

<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><i class="ti ti-flame"></i></div>
    <span class="mob-title">VaslZone</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img"><i class="ti ti-flame"></i></div>
    <div><div class="logo-name">VaslZone</div><div class="logo-sub">GATEWAY · v9.3</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec"><i class="ti ti-dashboard"></i> پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="resellers"><i class="ti ti-users"></i> نمایندگان <span class="nav-badge" id="res-nb">0</span></div>
    <div class="nav-it" data-pg="ipsettings"><i class="ti ti-world"></i> IP سراسری</div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec"><i class="ti ti-cpu"></i> سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
  </div>
  <div class="sb-foot">
    <a class="tg-btn" href="https://t.me/VaslZone" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout" style="transform:scaleX(-1)"></i> خروج</button>
  </div>
</aside>
"""

DASHBOARD_HTML = DASHBOARD_HTML + r"""
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-flame"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot g"></span> 🔥 فعال</span>
      <span class="badge" style="background:rgba(245,158,11,0.12);color:var(--yellow)"><span class="dot g"></span> <span id="uptime-badge">—</span></span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot g"></span> WebSocket / XHTTP</div></div>
    <div class="metric"><div class="m-icon suc"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<div class="m-unit" style="display:inline-block;margin-right:6px;font-size:13px;font-weight:500;color:var(--text-3)">MB</div></div><div class="m-sub">از راه‌اندازی</div></div>
    <div class="metric"><div class="m-icon dan"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div>
      <span class="badge" style="background:rgba(245,158,11,0.12);color:var(--yellow)"><span class="dot g"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">در حال دریافت...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ محدود</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> گروه‌های ساب</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع پروتکل</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:#34d399">● فعال · سخت‌گیرانه</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS</span><span class="sr-v" style="color:#34d399">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Siz10a XHTTP Ultra</span><span class="sr-v" style="color:#34d399">● فعال · 3 mode</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:#34d399">● فعال v9.3</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:#34d399">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:5px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div style="width:100%;height:6px;border-radius:4px;background:var(--red-dim);overflow:hidden"><div style="height:100%;background:var(--grad-red);border-radius:4px;transition:width .6s;width:0%" id="bw-bar"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge" style="background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)">0</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">VaslZone Gateway v9.3 · Railway Cloud · 2026</span>
    <a class="df-link" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/VaslZone</a>
  </div>
</section>

<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی</div></div>
    <div class="tb-right"><span class="badge" style="background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-fire"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub" style="background:rgba(0,0,0,0.45)"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit" style="background:rgba(0,0,0,0.45)">
            <option value="MB" selected>MB</option>
            <option value="GB">GB</option>
          </select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
          <option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
          <option value="trojan-ws">Trojan / WebSocket</option>
          <option value="ss-ws">Shadowsocks / WebSocket</option>
        </select>
        <div class="proto-cards">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">سازگار با CDN</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">تاخیر پایین‌تر</div>
          </div>
          <div class="proto-card" data-val="trojan-ws" onclick="selectProto('trojan-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-shield-lock"></i></div>
            <div class="proto-card-title">Trojan / WS</div>
            <div class="proto-card-desc">مبتنی بر رمز عبور</div>
          </div>
          <div class="proto-card" data-val="ss-ws" onclick="selectProto('ss-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-eye-off"></i></div>
            <div class="proto-card-title">Shadowsocks</div>
            <div class="proto-card-desc">ساده و سریع</div>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-server-2"></i> تنظیمات پیشرفته</div>
        <div class="cp-mini-row">
          <input class="cp-input-full" id="nl-ips" placeholder="IPها: 1.1.1.1,2.2.2.2">
          <input class="cp-input-full" id="nl-port" placeholder="پورت" style="max-width:90px">
          <input class="cp-input-full" id="nl-count" type="number" value="1" min="1" style="max-width:70px">
        </div>
        <label style="display:flex;align-items:center;gap:5px;margin-top:9px;font-size:12px;color:var(--text-2);cursor:pointer">
          <input type="checkbox" id="nl-personal" style="accent-color:var(--red);width:auto"> استفاده شخصی
        </label>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID تصادفی · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل قابل تغییر است.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-fire"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>

<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد</div></div>
    <div class="tb-right">
      <span class="badge" style="background:rgba(168,85,247,0.12);color:#c084fc;border:1px solid rgba(168,85,247,0.25)" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>
  </div>
</section>

<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div><div class="tb-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> سابسکریپشن تکی (هر کانفیگ)</div>
      <p style="font-size:11.5px;color:var(--text-3);line-height:1.8">هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون <i class="ti ti-rss"></i> کلیک کنید.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> سابسکریپشن کامل (ادمین)</div>
      <p style="font-size:11.5px;color:var(--text-3);line-height:1.8">شامل تمام کانفیگ‌های فعال.</p>
      <div style="background:rgba(0,0,0,0.40);border:1px solid var(--border);border-radius:10px;padding:11px 13px;margin-bottom:14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap">
        <span style="flex:1;font-family:ui-monospace,monospace;font-size:10.5px;color:var(--yellow-3);min-width:0;word-break:break-all" id="sub-all-url">در حال دریافت...</span>
        <div style="display:flex;gap:6px;flex-shrink:0">
          <button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button>
          <button class="btn btn-sm btn-g" onclick="window.open((location.protocol==='http:'?'http':'https')+'://'+(location.host||'localhost')+'/sub-all','_blank')" style="background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)"><i class="ti ti-external-link"></i></button>
        </div>
      </div>
      <div class="cl" style="background:var(--yellow-d);border:1px solid rgba(245,158,11,0.30);color:var(--yellow);margin-top:11px"><i class="ti ti-alert-triangle" style="color:var(--yellow)"></i><span>این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> لینک سابسکریپشن گروه‌ها</div>
    <div id="sub-groups-list">در حال بارگذاری...</div>
  </div>
</section>

<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>
  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span class="traf-main-val-unit">MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>
  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item" style="color:var(--red-3)"><span class="traf-legend-dot" style="background:var(--red);box-shadow:0 0 6px var(--red-3)"></span> مصرف</div>
        <div class="traf-legend-item" style="color:var(--yellow)"><span class="traf-legend-dot" style="background:var(--yellow);box-shadow:0 0 6px var(--yellow)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>

<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge" style="background:rgba(16,185,129,0.12);color:#34d399;border:1px solid rgba(16,185,129,0.25)" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>
  <div class="conn-hero">
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div><div class="conn-hero-label">اتصالات زنده</div><div class="conn-hero-val" id="ch-count">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-transfer"></i></div><div class="conn-hero-label">ترافیک لحظه‌ای</div><div class="conn-hero-val" id="ch-traffic">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-clock"></i></div><div class="conn-hero-label">میانگین مدت</div><div class="conn-hero-val" id="ch-avgdur">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div><div class="conn-hero-label">IP یکتا</div><div class="conn-hero-val" id="ch-uniq">—</div></div>
  </div>
  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>
  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none"><div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div><div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div><div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div></div>
</section>

<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:#34d399">● فعال (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · ۷ روز</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth سخت‌گیرانه</span><span class="sr-v" style="color:#34d399">● فعال v9.3</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال کانفیگ</span><span class="sr-v" style="color:#34d399">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:#34d399">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:#34d399">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز صفحه پابلیک ساب</span><span class="sr-v" style="color:#34d399">● اختیاری · SHA-256</span></div>
    </div>
  </div>
</section>

<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div><div class="tb-sub">تاریخچه‌ی کامل رخدادهای پنل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div></div>
</section>

<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge" style="background:var(--red-dim);color:var(--red-3);border:1px solid var(--border-2)" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div>
</section>

<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:720px">
    <div class="cl" style="background:var(--yellow-d);border:1px solid rgba(245,158,11,0.30);color:var(--yellow);margin-top:0;margin-bottom:14px"><i class="ti ti-alert-triangle" style="color:var(--yellow)"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).</span></div>
    <div class="form-row" style="margin-bottom:14px">
      <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها وجود داشته باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:14px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
    </div>
    <div style="background:rgba(0,0,0,0.40);border:1px solid var(--border);border-radius:10px;padding:15px;height:260px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--text-3)">منتظر اتصال...</p>
    </div>
  </div>
</section>

<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings-2"></i> تنظیمات</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot g"></span> آنلاین · Railway Cloud</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت</div><div class="srv-tile-val">443 (TLS)</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v9.3</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">MongoDB Atlas Cloud</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز فعلی</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی را وارد کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:7px">
          <label>رمز جدید</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>تکرار رمز جدید</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="تکرار رمز جدید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>

<section class="pg" id="pg-resellers">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-users"></i> نمایندگان</div></div>
  <div class="tb-right"><button class="btn btn-pur" onclick="openModal('modal-res')"><i class="ti ti-user-plus"></i> جدید</button></div></div>
  <div class="card"><div id="res-list">بارگذاری...</div></div>
</section>

<section class="pg" id="pg-ipsettings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-world"></i> IP سراسری</div></div></div>
  <div class="card" style="max-width:780px">
    <div class="card-title"><i class="ti ti-server-pin"></i> تنظیمات IP سراسری</div>
    <p style="font-size:11.5px;color:var(--text-3);line-height:1.8">این IPها برای همه کانفیگ‌هایی که IP اختصاصی ندارند استفاده می‌شوند.</p>
    <div class="cl" style="background:rgba(245,158,11,0.10);border:1px solid rgba(245,158,11,0.30);color:var(--yellow);margin-top:14px"><i class="ti ti-info-circle" style="color:var(--yellow)"></i><span>فاصله با کاما (,) از هم جدا کنید. خالی بگذارید = فقط hostname سرور استفاده می‌شود.</span></div>
    <div class="form-row" style="margin-top:14px">
      <div class="fg" style="flex:1"><label>IPها (کاما جدا کن)</label><input class="fi" id="g-ips" placeholder="1.1.1.1,2.2.2.2,3.3.3.3" style="width:100%"></div>
      <div class="fg"><label>پورت</label><input class="fi" id="g-port" type="number" placeholder="443"></div>
      <button class="btn btn-p" onclick="saveGlobalIPs()" style="height:auto;margin-bottom:11px"><i class="ti ti-device-floppy"></i> ذخیره</button>
    </div>
    <div id="gips-list" style="margin-top:14px;padding-top:14px;border-top:1px solid var(--border);color:var(--text-3);font-size:10.5px">در حال بارگذاری IPهای فعلی...</div>
  </div>
</section>
"""
DASHBOARD_HTML = DASHBOARD_HTML + r"""
</main>

<script>
let isDark=localStorage.getItem('VaslZone-theme')!=='light';
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';
  const i=document.getElementById('theme-icon');if(i)i.className='ti '+icon;
  const t=document.getElementById('theme-label');if(t)t.textContent=label;
  const m=document.getElementById('theme-mob-icon');if(m)m.className='ti '+icon;
}
try{applyTheme(isDark);}catch(e){}
function toggleTheme(){isDark=!isDark;localStorage.setItem('VaslZone-theme',isDark?'dark':'light');applyTheme(isDark)}

function toast(m,t){
  const el=document.getElementById('toast');
  el.innerHTML='<i class="ti '+(t==='ok'?'ti-circle-check':'ti-alert-circle')+'"></i> '+m;
  el.className='toast show '+(t||'');
  setTimeout(()=>el.classList.remove('show'),2200);
}
function fmtB(b){if(!b||b===0)return'0 B';if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return'<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return'<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return'<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return'<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> '+toFa(d)+' روز مانده</span>';
  return'<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> '+toFa(d)+' روز مانده</span>';
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · PUP','pc-xhttp'],'xhttp-stream-up':['XHTTP · SUP','pc-xhttp'],'xhttp-stream-one':['XHTTP ULTRA','pc-xhttp'],'trojan-ws':['TROJAN','pc-trojan'],'ss-ws':['SHADOWSOCKS','pc-ss']};
  const v=m[p]||m['vless-ws'];
  return'<span class="proto-chip '+v[1]+'">'+v[0]+'</span>';
}

async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value=val===0?'':val;
  document.getElementById('nl-unit').value=unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value=days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value=val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}

const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);

function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));

function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}

let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    const mb=d.total_traffic_mb.toFixed(1);
    document.getElementById('m-traffic').innerHTML=mb+'<div class="m-unit" style="display:inline-block;margin-right:4px;font-size:13px;font-weight:500;color:var(--text-3)">MB</div>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').innerHTML=toFa(d.total_errors)+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').innerHTML='🔥 '+d.uptime;
    document.getElementById('last-upd').innerHTML='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML='<span class="dot g"></span> '+toFa(d.active_connections)+' اتصال';
    document.getElementById('t-traffic').innerHTML=mb+'<span style="font-size:14px;font-weight:500;color:var(--text-3)"> ← MB</span>';
    const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=toFa(pct)+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1048576).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);
        document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span style="font-size:9px;color:var(--text-3);margin-right:3px">MB</span>';
        document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span style="font-size:9px;color:var(--text-3);margin-right:3px">MB</span>';
      }
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:#34d399;padding:11px;font-size:12px;display:flex;align-items:center;gap:6px"><i class="ti ti-circle-check" style="font-size:16px"></i> هیچ خطایی نیست · سیستم سالمه</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>'<div class="erow"><div class="etime"><i class="ti ti-clock"></i>'+new Date(e.time).toLocaleString('fa-IR')+'</div><div class="emsg">'+esc(e.error)+(e.url?' → '+esc(e.url):'')+'</div></div>').join('');
}

let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    allSubsList=subs;allLinksList=links;
    const nlSub=document.getElementById('nl-sub');
    const curSub=nlSub.value;
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>'<option value="'+esc(s.sub_id)+'">'+esc(s.name)+'</option>').join('');
    if(curSub)nlSub.value=curSub;
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
    document.getElementById('connections').innerHTML='<div style="background:linear-gradient(145deg,var(--card-2),var(--card));border:1px solid var(--border);border-radius:14px;padding:24px 32px;position:relative;overflow:hidden;margin-bottom:18px;box-shadow:var(--shadow)"><div style="position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--red-dim),transparent 70%);pointer-events:none"></div><div style="position:relative;z-index:1;font-size:11px;color:var(--red-3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:10px;display:flex;align-items:center;gap:6px"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div><div style="position:relative;z-index:1;font-size:34px;font-weight:900;color:var(--text);line-height:1;letter-spacing:-.03em">'+toFa(links.filter(l=>l.limit_bytes===0&&l.active&&!l.expired).length)+'<span style="font-size:14px;font-weight:500;color:var(--text-3)"> بدون محدودیت</span></div></div>';
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';
      document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}
    empty.style.display='none';
    const subMap=Object.fromEntries(subs.map(s=>[s.sub_id,s.name]));
    grid.innerHTML=links.map(l=>{
      const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
      const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
      const bc=pct>90?'var(--red)':pct>70?'var(--yellow)':'var(--green)';
      const allowed=l.active&&!l.expired;
      const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
      return'<div class="cfg-card '+cardCls+'">'+
  '<div class="cfg-row">'+
  '<span class="cfg-status-dot'+(allowed?' pulse':'')+'"></span>'+
  '<div class="cfg-identity">'+
  '  <div class="cfg-label">'+(l.label||'بدون نام')+'</div>'+
  '  <div class="cfg-sub-meta">'+
  '    <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText(\''+l.uuid+'\').then(()=>toast(\'UUID کپی شد\',\'ok\'))" title="'+l.uuid+'"><i class="ti ti-fingerprint"></i> '+l.uuid.slice(0,10)+'…</span>'+
  '    <span>'+new Date(l.created_at).toLocaleDateString('fa-IR')+'</span>'+
  '  </div>'+
  '</div>'+
  '<div class="cfg-divider-v"></div>'+
  '<div class="cfg-usage-col">'+
  '  <div class="ubar"><div class="ubar-f" style="width:'+pct+'%;background:'+bc+'"></div></div>'+
  '  <div class="utxt"><span><b>'+l.used_fmt+'</b></span><span>از <b>'+lim+'</b></span></div>'+
  '</div>'+
  '<div class="cfg-divider-v"></div>'+
  '<div class="cfg-exp-col">'+expChip(l.expires_at,l.expired)+'</div>'+
  '<div class="cfg-divider-v"></div>'+
  '<div class="cfg-badges-col">'+
  protoBadge(l.protocol)+
  (l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?'<span class="cfg-sub-tag"><i class="ti ti-folder"></i> '+esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)+'</span>':'')+
  '</div>'+
  '<div class="cfg-actions">'+
  '<button class="tog'+(allowed?' on':'')+'" onclick="toggleActive(\''+l.uuid+'\','+!l.active+')" title="فعال/غیرفعال"></button>'+
  '<button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link||\'\')+'\').then(()=>toast(\'لینک کپی شد\',\'ok\'))" title="کپی لینک"><i class="ti ti-copy"></i></button>'+
  '<button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText(\''+esc(l.sub_url||\'\')+'\').then(()=>toast(\'Sub کپی شد\',\'ok\'))" title="Sub URL"><i class="ti ti-rss"></i></button>'+
  '<button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(l.vless_link||\'\')+'\')" title="QR"><i class="ti ti-qrcode"></i></button>'+
  '<button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink(\''+l.uuid+'\')" title="ویرایش"><i class="ti ti-edit"></i></button>'+
  '<button class="btn btn-sm btn-g btn-icon" style="background:var(--yellow-d);color:var(--yellow);border:1px solid rgba(245,158,11,0.30)" onclick="resetUsage(\''+l.uuid+'\')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>'+
  '<button class="btn btn-sm btn-d btn-icon" onclick="deleteLink(\''+l.uuid+'\')" title="حذف"><i class="ti ti-trash"></i></button>'+
  '</div>'+
  '</div>'+
  '</div>';
    }).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>'<div class="sr"><span class="sr-k" style="gap:6px"><i class="ti '+(l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x')+'" style="color:'+(l.expired?'var(--yellow)':l.active?'var(--green)':'var(--red)')+'"></i>'+esc(l.label)+'</span><span class="sr-v" style="font-size:10px">'+fmtB(l.used_bytes)+' / '+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</span></div>').join('');
  }catch(e){console.error(e)}
}

async function createLink(){
  const label=(document.getElementById('nl-label').value||'').trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=(document.getElementById('nl-note').value||'').trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const addr=(document.getElementById('nl-ips').value||'').split(',').map(s=>s.trim()).filter(s=>s);
  const port=(document.getElementById('nl-port').value||'').trim()||undefined;
  const is_personal=document.getElementById('nl-personal').checked;
  const body={label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,ips:addr,port,is_personal};
  try{
    const count=parseInt(document.getElementById('nl-count').value)||1;
    if(count>1){body.count=count;
      const r=await fetch('/api/links/bulk',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const d=await r.json();
      toast(toFa(count)+' کانفیگ ساخته شد 🔥','ok');
    }else{
      const r=await fetch('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      const d=await r.json();
      if(d.sub_url){try{navigator.clipboard.writeText(d.sub_url).then(()=>toast('ساخته شد · لینک ساب کپی شد','ok'));}catch(e){toast('✅ کانفیگ ساخته شد','ok');}}
      else if(d.vless_link){try{navigator.clipboard.writeText(d.vless_link).then(()=>toast('✅ ساخته شد','ok'));}catch(e){toast('✅ ساخته شد','ok');}}
    }
    ['nl-label','nl-val','nl-exp','nl-note','nl-ips','nl-port'].forEach(id=>{const el=document.getElementById(id);if(el)el.value=''});
    const ce=document.getElementById('nl-count');if(ce)ce.value='1';
    const cp=document.getElementById('nl-personal');if(cp)cp.checked=false;
    loadLinks();
  }catch(e){toast('❌ خطا','err')}
}

function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label||'';
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1048576).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=(document.getElementById('el-label').value||'').trim();
  const note=(document.getElementById('el-note').value||'').trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const body={label,note,limit_value:val||0,limit_unit:unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'🔥 فعال شد':'غیرفعال شد',newState?'ok':'err');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}

function showQR(link){if(!link)return;window.open('https://api.qrserver.com/v1/create-qr-code/?size=320x320&data='+encodeURIComponent(link),'_blank')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2" style="grid-column:1/-1"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>{
    const subLinkIds=s.link_ids||[];
    return '<div class="sub-card">'+
      '<div class="sub-card-top">'+
      '<div class="sub-card-head-v2">'+
      '<div class="sub-card-icon"><i class="ti ti-folder"></i></div>'+
      '<div class="sub-card-titles">'+
      '<div class="sub-card-name-v2">'+esc(s.name||'?')+'</div>'+
      (s.desc?'<div class="sub-card-desc-v2">'+esc(s.desc)+'</div>':'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیحات</div>')+
      '</div>'+
      '<div class="sub-card-lock-badge '+(s.has_password?'locked':'open')+'" title="'+(s.has_password?'رمزدار':'پابلیک')+'">'+
      '<i class="ti '+(s.has_password?'ti-lock':'ti-lock-open')+'"></i></div>'+
      '</div>'+
      '<div class="sub-card-stats">'+
      '<div class="sub-card-stat"><div class="sub-card-stat-val">'+toFa(s.links_count||0)+'</div><div class="sub-card-stat-label">کانفیگ</div></div>'+
      '<div class="sub-card-stat"><div class="sub-card-stat-val" style="color:#34d399">'+toFa(s.active_count||0)+'</div><div class="sub-card-stat-label">فعال</div></div>'+
      '<div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:11px">'+esc(s.total_used_fmt||'0 B')+'</div><div class="sub-card-stat-label">مصرف</div></div>'+
      '</div>'+
      '</div>'+
      '<div class="sub-card-url-row">'+
      '<span class="sub-card-url-text">'+esc(s.public_url)+'</span>'+
      '<button class="sub-card-url-copy" onclick="navigator.clipboard.writeText(\''+esc(s.public_url||\'\')+'\').then(()=>toast(\'لینک پابلیک کپی شد\',\'ok\'))" title="کپی"><i class="ti ti-copy"></i></button>'+
      '<button class="sub-card-url-copy" onclick="window.open(\''+esc(s.public_url||\'\')+'\',\'_blank\')" title="باز کردن"><i class="ti ti-external-link"></i></button>'+
      '</div>'+
      '<div class="sub-card-bottom">'+
      '<button class="btn btn-sm btn-g" onclick="openSubLinks(\''+esc(s.sub_id)+'\',\''+esc(s.name)+'\')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>'+
      '<button class="btn btn-sm btn-pur" onclick="copyAllSubLinks(\''+esc(s.sub_id)+'\')"><i class="ti ti-copy"></i> کپی همه ساب‌ها</button>'+
      '<button class="btn btn-sm btn-g btn-icon" onclick="showQR(\''+esc(s.sub_url)+'\')" title="QR"><i class="ti ti-qrcode"></i></button>'+
      '<button class="btn btn-sm btn-d btn-icon" onclick="deleteSub(\''+esc(s.sub_id)+'\')" title="حذف"><i class="ti ti-trash"></i></button>'+
      '</div>'+
      '</div>';
  }).join('');
}
function filterSubs(q){
  if(!q){renderSubsGrid(allSubsRaw);return}
  const lq=q.trim().toLowerCase();
  if(!lq){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>(s.name||'').toLowerCase().includes(lq)||(s.desc||'').toLowerCase().includes(lq)));
}

async function createSub(){
  const name=(document.getElementById('ns-name').value||'').trim()||'گروه جدید';
  const desc=(document.getElementById('ns-desc').value||'').trim();
  const pw=(document.getElementById('ns-pw').value||'').trim();
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>{const e=document.getElementById(id);if(e)e.value=''});
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓','ok');loadSubs();
  }catch(e){toast('خطا در ساخت گروه','err')}
}
async function deleteSub(sub_id){
  if(!confirm('حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ✓','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}

let lmodalLinks=[],lmodalSubId=null,lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  lmodalSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name||'بدون نام';
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--text-3);font-size:12px;padding:24px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:24px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:34px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    return'<div class="lrow-v2'+(checked?' checked':'')+'" data-uuid="'+l.uuid+'" data-name="'+esc(l.label).toLowerCase()+'" onclick="toggleLrow(\''+l.uuid+'\',this)">'+
      '<div class="lrow-v2-check"><i class="ti ti-check"></i></div>'+
      '<div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>'+
      '<div class="lrow-v2-info">'+
      '<div class="lrow-v2-name">'+esc(l.label)+'</div>'+
      '<div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> '+fmtB(l.used_bytes)+'</div>'+
      '</div>'+
      '<span class="lrow-v2-status '+(on?'on':'off')+'">'+(on?'فعال':'غیرفعال')+'</span>'+
      '</div>';
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده';
}
function filterLmodal(q){
  const lq=(q||'').trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{
    const name=row.dataset.name||'';
    row.style.display=(!lq||name.includes(lq))?'':'none';
  });
}
async function saveSubLinks(){
  if(!lmodalSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+lmodalSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    closeModal('modal-links');
    toast('کانفیگ‌های گروه ذخیره شدند ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره','err')}
}
async function loadSubsPage(){
  const el=document.getElementById('sub-all-url');
  if(el)el.textContent=(location.protocol==='http:'?'http':'https')+'://'+(location.host||'localhost')+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}
    el.innerHTML=subs.map(s=>
      '<div style="padding:14px 16px;background:var(--red-dim);border:1px solid var(--border-2);border-radius:11px;margin-bottom:9px;display:flex;align-items:center;justify-content:space-between;gap:11px;flex-wrap:wrap;transition:.15s;cursor:default" onmouseover="this.style.borderColor=\'var(--red)\'" onmouseout="this.style.borderColor=\'var(--border-2)\'">'+
      '<div style="min-width:0;flex:1">'+
        '<div style="font-weight:700;font-size:13px;margin-bottom:3px;display:flex;align-items:center;gap:6px"><i class="ti ti-folder" style="color:#c084fc;font-size:14px"></i> '+esc(s.name)+'</div>'+
        '<div style="font-family:ui-monospace,monospace;font-size:9.5px;color:#c084fc;word-break:break-all;direction:ltr;text-align:left">'+esc(s.sub_url||'')+'</div>'+
        '<div style="font-size:10px;color:var(--text-3);margin-top:3px;display:flex;align-items:center;gap:6px">'+
          '<span style="display:inline-flex;align-items:center;gap:3px;padding:1px 6px;background:rgba(0,0,0,0.40);border-radius:8px"><i class="ti ti-link" style="font-size:9px"></i> '+toFa(s.links_count)+'</span>'+
          '<span style="display:inline-flex;align-items:center;gap:3px;padding:1px 6px;background:rgba(245,158,11,0.10);color:var(--yellow);border-radius:8px"><i class="ti ti-transfer" style="font-size:9px"></i> '+esc(s.total_used_fmt||'0')+'</span>'+
          (s.has_password?'<span style="display:inline-flex;align-items:center;gap:3px;padding:1px 6px;background:var(--yellow-d);color:var(--yellow);border-radius:8px"><i class="ti ti-lock" style="font-size:9px"></i> رمزدار</span>':'')+
        '</div>'+
      '</div>'+
      '<div style="display:flex;gap:5px;flex-wrap:wrap">'+
        '<button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.sub_url||\'\')+'\').then(()=>toast(\'کپی شد\',\'ok\'))"><i class="ti ti-copy"></i> ساب</button>'+
        '<button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText(\''+esc(s.public_url||\'\')+'\').then(()=>toast(\'کپی شد\',\'ok\'))"><i class="ti ti-globe"></i> پابلیک</button>'+
        '<button class="btn btn-sm btn-g" onclick="showQR(\''+esc(s.sub_url)+'\')"><i class="ti ti-qrcode"></i></button>'+
      '</div>'+
      '</div>'
    ).join('');
  }catch(e){console.error(e)}
}
function cpSubAll(){try{navigator.clipboard.writeText((location.protocol==='http:'?'http':'https')+'://'+(location.host||'localhost')+'/sub-all').then(()=>toast('کپی شد ✓','ok'));}catch(e){toast('خطا','err')}}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=(m[2]||'').toUpperCase();
  const mult={B:1,KB:1024,MB:1048576,GB:1073741824,TB:1099511627776};
  return n*(mult[u]||1);
}

async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot g"></span> '+toFa(d.count)+' اتصال';
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt||'0 B'),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return'<div class="conn-card-v2">'+
        '<div class="conn-card-v2-glow"></div>'+
        '<div class="conn-card-v2-top">'+
        '<div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>'+
        '<div class="conn-card-v2-id">'+
        '<div class="conn-ip-v2">'+esc(c.ip||'?')+
        '<button class="conn-ip-copy" onclick="navigator.clipboard.writeText(\''+esc(c.ip||\'\')+'\').then(()=>toast(\'IP کپی شد\',\'ok\'))" title="کپی IP"><i class="ti ti-copy"></i></button>'+
        '</div>'+
        '<div class="conn-label-v2">'+esc(c.label||'?')+'</div>'+
        '</div>'+
        '<span class="conn-status-pill"><span class="dot g"></span> زنده</span>'+
        '</div>'+
        '<div class="conn-card-v2-divider"></div>'+
        '<div class="conn-card-v2-body">'+
        '<div class="conn-proto-row">'+protoBadge(protoVal)+'</div>'+
        '<div class="conn-stat-row">'+
        '<div class="conn-stat-box">'+
        '<div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>'+
        '<div>'+
        '<div class="conn-stat-text-label">ترافیک</div>'+
        '<div class="conn-stat-text-val">'+esc(c.bytes_fmt||'0 B')+'</div>'+
        '</div>'+
        '</div>'+
        '<div class="conn-stat-box">'+
        '<div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>'+
        '<div>'+
        '<div class="conn-stat-text-label">مدت اتصال</div>'+
        '<div class="conn-stat-text-val">'+dur+'</div>'+
        '</div>'+
        '</div>'+
        '</div>'+
        '<div class="conn-duration-track"><div class="conn-duration-fill" style="width:'+durPct+'%"></div></div>'+
        '</div>'+
        '</div>';
    }).join('');
  }catch(e){console.error(e)}
}

async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}

async function fetchDefaultVless(){
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];
  const el=document.getElementById('vless-main');if(el){if(def&&def.vless_link){el.textContent=def.vless_link;}else{el.textContent='هنوز کانفیگی وجود ندارد';}}}catch(e){}
}

function cpText(id){try{navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'));}catch(e){toast('خطا در کپی','err')}}
function qrFor(id){const t=document.getElementById(id)?.textContent||'';if(t)showQR(t)}

function refreshAll(){
  fetchStats();fetchDefaultVless();loadLinks();
  if(document.getElementById('pg-subgroups')?.classList.contains('on'))loadSubs();
  if(document.getElementById('pg-subscriptions')?.classList.contains('on'))loadSubsPage();
  if(document.getElementById('pg-connections')?.classList.contains('on'))loadConns();
  if(document.getElementById('pg-logs')?.classList.contains('on'))loadActivity();
  toast('🔥 رفرش شد','ok');
}

let ws;
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list');
    const em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
    el.innerHTML=logs.map(l=>
      '<div class="log-item">'+
      '<div class="log-ic '+l.level+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div>'+
      '<div class="log-body">'+
      '<div class="log-msg">'+esc(l.message)+'</div>'+
      '<div class="log-time"><i class="ti ti-clock"></i> '+new Date(l.time).toLocaleString('fa-IR')+
      ' <span class="log-kind">'+esc(kindFa[l.kind]||l.kind||'')+'</span></div>'+
      '</div>'+
      '</div>'
    ).join('');
  }catch(e){console.error(e)}
}
</script>

<script>
console.log("Script loaded");
document.body.style.borderTop = "10px solid red";
document.addEventListener('DOMContentLoaded', function(){
  setTimeout(function(){
    try{checkAuth();}catch(e){}
    try{initCharts();}catch(e){}
    try{fetchStats();}catch(e){}
    try{fetchDefaultVless();}catch(e){}
    try{loadLinks();}catch(e){}
    try{loadSubs();}catch(e){}
    var sh=document.getElementById('set-host');if(sh)sh.textContent=location.host;
    var sa=document.getElementById('sub-all-url');if(sa)sa.textContent=location.protocol+'//'+location.host+'/sub-all';
  },200);
  setInterval(function(){try{fetchStats();}catch(e){}},4000);
  setInterval(function(){
    try{
      var p=document.querySelector('.pg.on');
      if(p){
        var id=p.id;
        if(id==='pg-links')loadLinks();
        if(id==='pg-subgroups')loadSubs();
        if(id==='pg-connections')loadConns();
        if(id==='pg-logs')loadActivity();
      }
    }catch(e){}
  },5000);
});

async function saveGlobalIPs(){
  const ips=(document.getElementById('g-ips').value||'').split(',').map(s=>s.trim()).filter(s=>s);
  const port=parseInt(document.getElementById('g-port').value)||443;
  try{
    const r=await authF('/api/settings/global-ips',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({ips,port})});
    if(!r.ok)throw new Error();
    toast('تنظیمات IP سراسری ذخیره شد ✓','ok');
    const el=document.getElementById('gips-list');if(el)el.innerHTML='📡 IPها: '+(ips.join(', ')||'(پیش‌فرض) '+(location.host||''))+' · پورت: '+port;
  }catch(e){toast('❌ خطا','err')}
}

async function copyAllSubLinks(subId){
  try{
    const r=await authF('/api/links');const d=await r.json();const links=d.links||[];
    const sub=allSubsRaw.find(s=>s.sub_id===subId);
    if(!sub){toast('گروه پیدا نشد','err');return}
    const subLinkIds=sub.link_ids||[];
    const urls=links.filter(l=>subLinkIds.includes(l.uuid)&&l.active&&!l.expired).map(l=>l.sub_url||l.vless_link).filter(x=>x);
    if(!urls.length){toast('کانفیگ فعالی نیست','err');return}
    navigator.clipboard.writeText(urls.join('\n')).then(()=>toast(toFa(urls.length)+' لینک کپی شد ✓','ok'));
  }catch(e){toast('❌ خطا','err')}
}

async function changePw(){
  const cur=(document.getElementById('cp-cur').value||''),nw=(document.getElementById('cp-new').value||''),cf=(document.getElementById('cp-cf').value||'');
  if(!cur||!nw||!cf){toast('همه فیلدها الزامی','err');return}
  if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
  if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('🔥 رمز تغییر کرد ✓','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>{const e=document.getElementById(id);if(e)e.value=''});
  }catch(e){toast('✗ '+e.message,'err')}
}
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const go=inp.type==='password';
  inp.type=go?'text':'password';
  if(icon)icon.className='ti '+(go?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label=document.getElementById('pw-strength-label');
  const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  if(reqLen)reqLen.classList.toggle('met',hasLen);
  if(reqNum)reqNum.classList.toggle('met',hasNum);
  if(reqCase)reqCase.classList.toggle('met',hasCase);
  let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  const colors=['#dc2626','#f59e0b','#fbbf24','#22c55e'];
  const labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,100,100,.20)'});
  if(val.length===0){if(label)label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}
  if(label)label.innerHTML='<i class="ti ti-shield-check" style="color:'+colors[Math.max(0,score-1)]+'"></i> '+(labels[Math.max(0,score-1)]||'');
}

async function createReseller(){
  await fetch('/api/resellers',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:(document.getElementById('r-name')?.value||''),password:(document.getElementById('r-pw')?.value||''),limit_gb:document.getElementById('r-gb')?.value||0})});
  closeModal('modal-res');
  try{const r=await authF('/api/resellers');const el=document.getElementById('res-list');
  document.getElementById('res-nb').textContent=(r.resellers||[]).length;
  const rs=r.resellers||[];
  if(!rs.length){el.innerHTML='<div class="empty" style="padding:55px"><i class="ti ti-users"></i><p>هنوز نماینده‌ای نیست</p></div>';return}
  el.innerHTML='<div style="overflow-x:auto;margin-top:14px"><table style="width:100%;border-collapse:collapse;font-size:12px"><thead><tr style="background:var(--red-dim);color:var(--red-3)"><th style="padding:13px 16px;text-align:right;border-bottom:1px solid var(--border-2)">نام</th><th style="padding:13px 16px;text-align:center;border-bottom:1px solid var(--border-2)">حجم</th><th style="padding:13px 16px;text-align:center;border-bottom:1px solid var(--border-2)">مصرف</th><th style="padding:13px 16px;text-align:center;border-bottom:1px solid var(--border-2)">باقی</th><th style="padding:13px 16px;text-align:center;border-bottom:1px solid var(--border-2)">وضعیت</th><th style="padding:13px 16px;text-align:left;border-bottom:1px solid var(--border-2)">عملیات</th></tr></thead><tbody>'+rs.map(r=>'<tr style="border-top:1px solid var(--border)"><td style="padding:14px 16px;font-weight:700"><div style="display:flex;align-items:center;gap:7px"><div style="width:30px;height:30px;border-radius:9px;background:var(--red-dim);color:var(--red-3);display:flex;align-items:center;justify-content:center;font-size:13px"><i class="ti ti-user"></i></div>'+esc(r.name)+'</div></td><td style="padding:14px 16px;text-align:center;color:var(--yellow);font-weight:700">'+esc(r.total_fmt||'0')+'</td><td style="padding:14px 16px;text-align:center;color:#c084fc;font-weight:700">'+esc(r.allocated_fmt||'0')+'</td><td style="padding:14px 16px;text-align:center;color:'+(r.remaining_bytes>0?'#34d399':'var(--red-3)')+';font-weight:700">'+esc(r.remaining_fmt||'0')+'</td><td style="padding:14px 16px;text-align:center">'+(((r.active??true)?'<span class="dot g"></span>':'<span class="dot" style="background:var(--red-3)"></span>'))+(r.active??true)+'</td><td style="padding:14px 16px;text-align:left"><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="navigator.clipboard.writeText(\''+esc(r.login_link||\'\')+'\').then(()=>toast(\'کپی شد\',\'ok\'))"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-amber" onclick="resetResToken(\''+esc(r.id)+'\')"><i class="ti ti-refresh"></i></button><button class="btn btn-sm btn-d" onclick="deleteReseller(\''+esc(r.id)+'\')"><i class="ti ti-trash"></i></button></div></td></tr>').join('')+'</tbody></table></div>';
  }catch(e){toast('❌ خطا','err')}
}
async function resetResToken(id){
  if(!confirm('لینک اختصاصی تغییر کنه؟'))return;
  try{const r=await fetch('/api/resellers/'+id+'/reset-token',{method:'POST'});if(!r.ok)throw new Error();toast('لینک جدید ساخته شد ✓','ok');createReseller();}catch(e){toast('❌ خطا','err')}
}
async function deleteReseller(id){if(!confirm('حذف?'))return;try{await fetch('/api/resellers/'+id,{method:'DELETE'});toast('حذف شد ✓','ok');createReseller();}catch(e)}}

function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,280);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  const c1=document.getElementById('ch1').getContext('2d');
  const grad1=makeGradient(c1,'rgba(220,38,38,.40)','rgba(220,38,38,0)');
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(13,13,13,0.97)',borderColor:'rgba(239,68,68,0.40)',borderWidth:1,
        titleColor:'#fff',bodyColor:'#c084fc',padding:12,cornerRadius:12,
        displayColors:false,titleFont:{family:'Vazirmatn',size:12,weight:'700'},
        bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:v=>'🟥 '+v.parsed.y.toFixed(2)+' MB'}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#a3a3a3',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(239,68,68,0.06)'},border:{display:false},ticks:{color:'#a3a3a3',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[{label:'MB',data:[],borderColor:'#ef4444',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#ef4444',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5}]},options:opts});

  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradient(c3ctx,'rgba(220,38,38,.45)','rgba(220,38,38,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'مصرف',data:[],borderColor:'#ef4444',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#ef4444',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#f59e0b',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(13,13,13,0.97)',borderColor:'rgba(239,68,68,0.40)',borderWidth:1,
          titleColor:'#fff',bodyColor:'#c084fc',padding:14,cornerRadius:12,
          displayColors:true,boxPadding:6,
          titleFont:{family:'Vazirmatn',size:12,weight:'700'},
          bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:v=>' '+(v.dataset.label||'')+': '+v.parsed.y.toFixed(2)+' MB'}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#a3a3a3',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{grid:{color:'rgba(239,68,68,0.05)'},border:{display:false},ticks:{color:'#a3a3a3',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}
      }
    }
  });

  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
      data:[55,35,10],
      backgroundColor:['#dc2626','#a855f7','#f59e0b'],
      borderColor:getComputedStyle(document.documentElement).getPropertyValue('--card').trim()||'#0d0d0d',
      borderWidth:4,hoverOffset:12,borderRadius:6,spacing:3
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'72%',
      plugins:{
        legend:{position:'bottom',labels:{color:'#a3a3a3',font:{size:10,family:'Vazirmatn'},padding:14,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:'rgba(13,13,13,0.97)',borderColor:'rgba(239,68,68,0.40)',borderWidth:1,padding:11,cornerRadius:11,
        bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });
}

function wsConn(){
  const u=(document.getElementById('ws-uuid').value||'').trim();
  if(!u){toast('UUID را وارد کنید','err');return}
  const proto=location.protocol==='https:'?'wss':'ws';
  const url=proto+'://'+location.host+'/ws/'+u;
  const log=document.getElementById('ws-log');
  log.innerHTML='<p style="color:var(--yellow)">[Connecting] '+url+'</p>';
  try{ws=new WebSocket(url);ws.onopen=()=>{log.innerHTML+='<p style="color:#34d399">[<i class="ti ti-circle-check"></i>] متصل · UUID معتبر</p>';};
  ws.onerror=(e)=>{log.innerHTML+='<p style="color:var(--red-3)">[Error] UUID نامعتبر یا غیرفعال</p>';};
  ws.onmessage=(m)=>{log.innerHTML+='<p style="color:#c084fc">[Received] '+(m.data?(m.data.length||m.data.byteLength)+' bytes':'empty')+'</p>';log.scrollTop=log.scrollHeight;};
  ws.onclose=(e)=>{log.innerHTML+='<p style="color:var(--red-3)">[Closed] code='+e.code+'</p>';};}catch(e){log.innerHTML+='<p style="color:var(--red-3)">[Exception] '+e.message+'</p>';}
}
function wsSend(){
  const m=(document.getElementById('ws-msg').value||'');if(!m||!ws||ws.readyState!==1)return;
  ws.send(m);
  const log=document.getElementById('ws-log');log.innerHTML+='<p style="color:var(--yellow)">[Sent] '+esc(m)+'</p>';
  document.getElementById('ws-msg').value='';
}
function wsDisc(){if(ws){ws.close();ws=null;}}
</script>
</body></html>"""
