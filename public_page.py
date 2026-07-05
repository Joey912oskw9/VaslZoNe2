from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url: str, title: str, subtitle: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>{{quote(title)}} · VaslZone</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{--bg:#050504;--card:#0d0d0a;--card2:#141410;--card3:#1a1a15;--border:rgba(255,215,0,0.08);--border2:rgba(255,215,0,0.30);--accent:#FFD700;--accent2:#FFC107;--accent3:#FFE44D;--text:#F5F5DC;--text2:#C8C8A0;--text3:#6B6B40;--green:#66BB6A;--green-bg:rgba(102,187,106,0.10);--red:#EF5350;--red-bg:rgba(239,83,80,0.10);--radius:16px}}
@keyframes fl{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-20px)}}}}
@keyframes rLaunch{{0%{{transform:translateY(0) rotate(0)}}25%{{transform:translateY(-30px) rotate(-8deg)}}60%{{transform:translateY(-60px) rotate(10deg) scale(1.1)}}100%{{transform:translateY(calc(100vh - 120px)) rotate(5deg) scale(0.3);opacity:0}}}}
@keyframes rExplode{{0%{{transform:scale(0);opacity:1}}30%{{transform:scale(3);opacity:.8}}100%{{transform:scale(5);opacity:0}}}}
.rkt{{position:fixed;left:6px;top:50%;z-index:50;font-size:34px;color:var(--accent);cursor:pointer;animation:fl 3.5s ease-in-out infinite;filter:drop-shadow(0 0 10px rgba(255,215,0,0.3))}}
@media(max-width:500px){{.rkt{{display:none}}}}
body{{font-family:Vazirmatn,sans-serif;background:radial-gradient(ellipse 80% 35% at 50% -8%,rgba(255,215,0,0.04),transparent 65%),radial-gradient(ellipse 50% 25% at 20% 100%,rgba(255,215,0,0.02),transparent),var(--bg);color:var(--text);min-height:100vh;direction:rtl;overflow-x:hidden}}
.wrap{{max-width:580px;margin:0 auto;padding:16px 14px 48px}}
.header{{text-align:center;padding:28px 0 8px}}
.ch-avatar{{width:74px;height:74px;border-radius:22px;margin:0 auto 14px;background:linear-gradient(145deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:34px;color:#000;animation:fl 4s ease-in-out infinite;box-shadow:0 0 0 3px rgba(255,215,0,0.12),0 12px 32px rgba(255,215,0,0.10)}}
.ch-name{{font-size:18px;font-weight:800;color:var(--text)}}
.ch-link{{display:inline-flex;align-items:center;gap:6px;font-size:11px;color:var(--accent);text-decoration:none;font-weight:600;padding:5px 14px;border-radius:20px;background:rgba(255,215,0,0.08);border:1px solid rgba(255,215,0,0.12)}}
.info-card{{background:var(--card);border:1px solid var(--border);border-radius:20px;padding:20px 22px;margin:18px 0 14px}}
.info-name{{font-size:20px;font-weight:800;color:var(--text)}}
.stats-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}}
.stat-box{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:15px 14px;text-align:center}}
.stat-box .sl{{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;margin-bottom:7px}}
.stat-box .sv{{font-size:20px;font-weight:800;color:var(--accent)}}
.cfg-card{{background:var(--card2);border:1px solid var(--border);border-radius:16px;padding:16px 18px;margin-bottom:10px;border-right:3px solid var(--green)}}
.cfg-card.inactive{{border-right-color:var(--red)}}
.cfg-label{{font-size:14px;font-weight:700;color:var(--text)}}
.cfg-status-pill{{font-size:9px;padding:4px 10px;border-radius:20px;font-weight:700}}
.cfg-status-pill.on{{background:var(--green-bg);color:var(--green)}}
.cfg-status-pill.off{{background:var(--red-bg);color:var(--red)}}
.bar{{height:5px;border-radius:4px;background:rgba(255,215,0,0.06);overflow:hidden;margin:5px 0}}
.bar-fill{{height:100%;border-radius:4px;transition:width .6s}}
.remaining-tag{{font-size:10px;font-weight:700;padding:3px 10px;border-radius:6px}}
.remaining-tag.ok{{background:var(--green-bg);color:var(--green)}}
.remaining-tag.warn{{background:rgba(255,215,0,0.10);color:var(--accent)}}
.remaining-tag.danger{{background:var(--red-bg);color:var(--red)}}
.copy-btn{{background:var(--accent);color:#000;border:none;padding:6px 12px;border-radius:8px;cursor:pointer;font-family:inherit;font-size:10px;font-weight:700}}
.copy-all-bar{{background:linear-gradient(135deg,rgba(255,215,0,0.08),rgba(255,193,7,0.04));border:1px solid rgba(255,215,0,0.12);border-radius:14px;padding:14px 16px;margin-bottom:14px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}}
.copy-all-btn{{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;border:none;padding:9px 18px;border-radius:10px;font-weight:800;cursor:pointer;font-family:inherit}}
.footer{{text-align:center;padding:24px 0 8px;font-size:9px;color:var(--text3)}}
.footer a{{color:var(--accent);font-weight:700;text-decoration:none}}
.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card2);border:1px solid var(--border);color:var(--text);padding:10px 20px;border-radius:12px;font-size:12px;font-weight:600;opacity:0;transition:all .3s;z-index:999}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(102,187,106,0.25);color:var(--green);background:rgba(102,187,106,0.10)}}
.chart-box{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 16px;margin:14px 0}}
.chart-box .ttl{{font-size:11px;font-weight:700;color:var(--text2);margin-bottom:10px;display:flex;align-items:center;gap:6px}}
.chart-box .ttl i{{color:var(--accent)}}
.chart-box .bd{{height:160px}}
.dot{{width:5px;height:5px;border-radius:50%;display:inline-block;background:var(--green);animation:pl 2s infinite}}
@keyframes pl{{0%,100%{{opacity:1}}50%{{opacity:.2}}}}
@media(max-width:500px){{.stats-row{{grid-template-columns:1fr 1fr}}.copy-all-bar{{flex-direction:column;align-items:stretch}}}}
</style></head>
<body>
<audio id="bm" autoplay loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"></audio>
<script>var _m=document.getElementById('bm');_m.volume=0.07;</script>
<div class="rkt" id="rk" onclick="fr()">🚀</div>
<div id="ex" style="position:fixed;width:80px;height:80px;pointer-events:none;z-index:60;opacity:0;border-radius:50%;background:radial-gradient(circle,#ffd700,transparent 70%);left:0;top:0"></div>
<div class="toast" id="toast"></div>
<div class="wrap">
<div class="header">
<div class="ch-avatar"><i class="ti ti-bolt"></i></div>
<div class="ch-name">VaslZone</div>
<a class="ch-link" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
</div>
<div id="root"><div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-loader-2" style="font-size:32px;color:var(--accent);display:inline-block;animation:spin 1.2s linear infinite"></i><p style="margin-top:8px">در حال بارگذاری...</p></div></div>
<div class="footer"><a href="https://t.me/VaslZone">@VaslZone</a></div>
</div>
<style>@keyframes spin{{to{{transform:rotate(360deg)}}}}</style>
<script>
const A="{api_url}",L=[];var ch=null;
function B(b){{if(!b||b===0)return'0';if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}}
function E(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}})[c])}}
function N(n){{return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function T(m){{var t=document.getElementById('toast');t.textContent='\u2705 '+m;t.className='toast show';setTimeout(()=>t.classList.remove('show'),1800)}}
async function LD(){{try{{var r=await fetch(A);if(!r.ok)throw Error();return await r.json()}}catch(e){{return null}}}}
function Q(u){{if(u)window.open('https://api.qrserver.com/v1/create-qr-code/?size=240x240&data='+encodeURIComponent(u),'_blank')}}
function SV(i){{var e=document.getElementById('v-'+i);if(e)e.classList.toggle('s')}}
function CP(t){{navigator.clipboard.writeText(t).then(()=>T('کپی شد'))}}
function CA(){{var t=L.map(l=>l.vless_link||'').filter(Boolean).join('\n');if(t)navigator.clipboard.writeText(t).then(()=>T('همه کپی شد'))}}
function fr(){{var r=document.getElementById('rk');if(r.dataset.f)return;r.dataset.f='1';r.style.animation='rLaunch 1.3s ease-in forwards';setTimeout(function(){{var e=document.getElementById('ex');e.style.top=(window.innerHeight/2-40)+'px';e.style.opacity='1';e.style.animation='rExplode .7s ease-out forwards';r.style.display='none';setTimeout(function(){{e.style.opacity='0';e.style.animation='';r.style.display='';r.style.animation='';r.dataset.f=''}},800)}},1300)}}
function IC(){{var c=document.getElementById('ch');if(!c||typeof Chart==='undefined')return;if(ch)ch.destroy();var v=[];for(var i=0;i<24;i++)v.push(Math.random()*50);ch=new Chart(c.getContext('2d'),{{type:'line',data:{{labels:Array(24).fill(''),datasets:[{{label:'MB',data:v,borderColor:'#ffd700',backgroundColor:'rgba(255,215,0,0.1)',fill:true,tension:.4,pointRadius:2,borderWidth:2}}]}},options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}},tooltip:{{backgroundColor:'rgba(13,13,10,0.95)',titleColor:'#ffd700',bodyColor:'#c8c8a0',padding:10,cornerRadius:8,displayColors:false}}}},scales:{{x:{{grid:{{display:false}},ticks:{{color:'#6b6b40',font:{{size:8}}}}}},y:{{grid:{{color:'rgba(255,215,0,0.05)'}},ticks:{{color:'#6b6b40',font:{{size:8}}}}}}}}}}}})}}
function R(d){{
if(!d||!d.links||!d.links.length){{document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-link-off" style="font-size:36px;display:block;margin-bottom:12px;opacity:.3"></i><p>کانفیگی یافت نشد</p></div>';return}}
L.length=0;d.links.forEach(l=>L.push(l));var a=d.links.filter(l=>l.active).length,u=d.links.reduce((s,l)=>s+(l.used_bytes||0),0);
var h='<div class="info-card"><div class="info-name">'+E(d.name||'VaslZone')+'</div>'+(d.desc?'<div style="font-size:11px;color:var(--text2);margin-top:4px">'+E(d.desc)+'</div>':'')+'</div>';
h+='<div class="stats-row"><div class="stat-box"><div class="sl">وضعیت</div><div class="sv">'+(d.links.length===1?(d.links[0].active?'فعال':'غیرفعال'):N(a)+'/'+N(d.links.length))+'</div></div><div class="stat-box"><div class="sl">مصرف</div><div class="sv" style="font-size:17px">'+B(u)+'</div></div><div class="stat-box"><div class="sl">اتصالات</div><div class="sv">'+N(d.active_connections||0)+'</div></div></div>';
if(d.links.length>1)h+='<div class="copy-all-bar"><div style="font-size:12px;font-weight:700;color:var(--text);flex:1;min-width:140px"><i class="ti ti-copy"></i> کپی همه</div><button class="copy-all-btn" onclick="CA()">کپی ('+N(a)+')</button></div>';
h+='<div class="chart-box"><div class="ttl"><i class="ti ti-chart-bar"></i> مصرف</div><div class="bd"><canvas id="ch"></canvas></div></div>';
h+='<div style="font-size:11px;font-weight:700;color:var(--text3);margin:14px 0 10px"><i class="ti ti-link"></i> کانفیگ‌ها</div>';
for(var i=0;i<d.links.length;i++){{var l=d.links[i],p=l.limit_bytes>0?Math.min(100,(l.used_bytes/l.limit_bytes)*100):0,rm=l.limit_bytes>0?Math.max(0,l.limit_bytes-l.used_bytes):-1,rc=rm<0?'ok':(rm<1048576?'danger':(rm<1073741824?'warn':'ok')),rf=rm<0?'∞':B(rm);h+='<div class="cfg-card'+(l.active?'':' inactive')+'"><div style="display:flex;justify-content:space-between;margin-bottom:8px"><span class="cfg-label">'+E(l.label)+'</span><span class="cfg-status-pill '+(l.active?'on':'off')+'">'+(l.active?'● فعال':'○ غیرفعال')+'</span></div><div style="font-size:10px;color:var(--text2);display:flex;justify-content:space-between;margin-bottom:4px"><span>مصرف: <b>'+l.used_fmt+'</b></span><span>از <b>'+(l.limit_bytes===0?'∞':l.limit_fmt)+'</b></span></div><div class="bar"><div class="bar-fill" style="width:'+p+'%;background:'+(p>90?'var(--red)':p>70?'var(--accent)':'var(--green)')+'"></div></div><span class="remaining-tag '+rc+'">'+(rm<0?'∞':rf)+'</span><div class="vl" id="v-'+i+'" style="display:none;background:rgba(0,0,0,0.4);border-radius:7px;padding:7px 9px;font-family:monospace;font-size:8.5px;color:var(--accent3);word-break:break-all;margin-top:7px;direction:ltr;text-align:left">'+E(l.vless_link||'')+'</div><div style="display:flex;gap:5px;margin-top:7px"><button style="background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;border:none;padding:6px 12px;border-radius:7px;cursor:pointer;font:inherit;font-size:10px;font-weight:700;flex:1" onclick="SV('+i+')"><i class="ti ti-eye"></i></button><button style="background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;border:none;padding:6px 12px;border-radius:7px;cursor:pointer;font:inherit;font-size:10px;font-weight:700;flex:1" onclick="CP(L['+i+'].vl)">کپی</button><button style="background:transparent;border:1px solid var(--border);color:var(--text2);padding:6px 12px;border-radius:7px;cursor:pointer;font:inherit;font-size:10px;font-weight:700;flex:0" onclick="Q(L['+i+'].vl)"><i class="ti ti-qrcode"></i></button></div></div>'}}
h+='<div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px 14px;margin-top:10px"><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px"><span style="font-size:10px;font-weight:700;color:var(--text2);display:flex;align-items:center;gap:5px"><i class="ti ti-bolt" style="color:var(--accent)"></i> تست</span><button style="padding:5px 12px;border-radius:7px;border:1px solid var(--border);background:rgba(255,215,0,0.06);color:var(--accent);font:inherit;font-size:9.5px;font-weight:700;cursor:pointer" id="sB" onclick="TS()">شروع</button></div><div id="sR" style="font-family:monospace;font-size:13px;font-weight:800;color:var(--accent);padding:8px;background:rgba(0,0,0,0.3);border-radius:7px;text-align:center;direction:ltr">-</div></div>';
document.getElementById('root').innerHTML=h;try{{setTimeout(IC,300)}}catch(e){{}}
}}
function TS(){{var b=document.getElementById('sB'),r=document.getElementById('sR');if(b.disabled)return;b.disabled=true;r.textContent='⏳...';var s=Date.now();fetch(A+'?_='+s).then(function(re){{re.json().then(function(){{var ms=Date.now()-s;r.textContent=(ms<50?'🟢':ms<150?'🟡':'🔴')+' '+ms+'ms';b.disabled=false}})}}).catch(function(){{r.textContent='🔴 خطا';b.disabled=false}})}}
(async function(){{var d=await LD();if(d){{d.links.forEach(l=>l.vless_lines=l.vless_link?l.vless_link.split('\n').filter(x=>x):[]);R(d)}}else document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-alert-circle" style="font-size:36px;color:var(--red);display:block;margin-bottom:10px"></i><p>خطا</p></div>'}})();
</script>
</body></html>"""

def get_public_page_html(u):
    return get_sub_page_html(api_url=f"/api/public/sub/{u}", title="VaslZone Group")

def get_single_sub_page_html(u):
    return get_sub_page_html(api_url=f"/api/public/sub-single/{u}", title="VaslZone Config")
