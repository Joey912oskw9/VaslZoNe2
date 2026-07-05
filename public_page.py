from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url, title="VaslZone", subtitle=""):
    return (r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>VaslZone</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050504;--card:#0d0d0a;--card2:#141410;--accent:#FFD700;--accent2:#FFC107;--text:#F5F5DC;--text2:#C8C8A0;--text3:#6B6B40;--green:#66BB6A;--red:#EF5350;--border:rgba(255,215,0,0.08);--border2:rgba(255,215,0,0.25)}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes rLaunch{0%{transform:translateY(0) rotate(0)}25%{transform:translateY(-30px) rotate(-8deg)}60%{transform:translateY(-60px) rotate(10deg) scale(1.1)}100%{transform:translateY(calc(100vh - 120px)) rotate(5deg) scale(0.3);opacity:0}}
@keyframes rExplode{0%{transform:scale(0);opacity:1}30%{transform:scale(3);opacity:.8}100%{transform:scale(5);opacity:0}}
body{font-family:Vazirmatn,sans-serif;background:radial-gradient(ellipse 80% 35% at 50% -8%,rgba(255,215,0,0.04),transparent),var(--bg);color:var(--text);direction:rtl;min-height:100vh;overflow-x:hidden}
.wrap{max-width:560px;margin:0 auto;padding:16px 14px 50px}
.hd{text-align:center;padding:28px 0 10px}
.av{width:72px;height:72px;border-radius:20px;margin:0 auto 12px;background:linear-gradient(145deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:34px;color:#000;animation:fl 4s ease-in-out infinite;box-shadow:0 0 0 3px rgba(255,215,0,0.1)}
.cn{font-size:22px;font-weight:900;background:linear-gradient(135deg,var(--text),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.tg{display:inline-flex;align-items:center;gap:6px;margin-top:8px;padding:5px 14px;border-radius:20px;background:rgba(255,215,0,0.06);border:1px solid var(--border);color:var(--accent);text-decoration:none;font-size:10px;font-weight:600}
.cd{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:18px 20px;margin-bottom:12px}
.s3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}
.s3>div{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 10px;text-align:center}
.s3>div .l{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;margin-bottom:6px}
.s3>div .v{font-size:20px;font-weight:800;color:var(--accent)}
.cfg{background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:14px 15px;margin-bottom:10px;border-right:3px solid var(--accent)}
.cfg .r1{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.cfg .nm{font-size:13px;font-weight:700}
.cfg .st{font-size:8px;padding:2px 8px;border-radius:12px;font-weight:700}
.cfg .st.on{background:rgba(102,187,106,0.1);color:var(--green)}
.cfg .st.off{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg .u{font-size:9.5px;color:var(--text2);display:flex;justify-content:space-between;margin-bottom:5px}
.cfg .u b{color:var(--text)}
.cfg .bar{height:4px;border-radius:3px;background:rgba(255,215,0,0.06);overflow:hidden;margin-bottom:5px}
.cfg .bar .f{height:100%;border-radius:3px;background:var(--accent);transition:width .5s}
.cfg .rm{font-size:9px;font-weight:700;padding:2px 9px;border-radius:5px;display:inline-block}
.cfg .rm.g{background:rgba(102,187,106,0.1);color:var(--green)}
.cfg .rm.y{background:rgba(255,215,0,0.08);color:var(--accent)}
.cfg .rm.r{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg .vl{display:none;background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:7px;padding:7px 9px;font-family:monospace;font-size:8.5px;color:var(--accent3);word-break:break-all;margin-top:7px;max-height:55px;overflow-y:auto;direction:ltr;text-align:left}
.cfg .vl.s{display:block}
.btns{display:flex;gap:5px;margin-top:7px}
.btns button{font:inherit;font-size:10px;font-weight:700;padding:6px 12px;border-radius:7px;cursor:pointer;border:none;flex:1;display:flex;align-items:center;gap:4px;justify-content:center;transition:.15s}
.btns .y{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000}
.btns .o{background:transparent;border:1px solid var(--border);color:var(--text2)}
.cp{background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:10px;padding:12px 14px;margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.cp .t{font-size:11px;font-weight:800;color:#000}
.cp button{background:#000;color:var(--accent);border:none;padding:8px 16px;border-radius:8px;font-weight:700;cursor:pointer;font-size:9px;font-family:inherit}
.chart-c{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 16px;margin-top:12px;margin-bottom:12px}
.chart-h{font-size:11px;font-weight:800;color:var(--text2);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.chart-h i{color:var(--accent)}
.chart-b{height:160px}
.spd{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px 14px;margin-top:4px}
.spd .tp{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.spd .tp .tt{font-size:10px;font-weight:700;color:var(--text2);display:flex;align-items:center;gap:5px}
.spd .tp .tt i{color:var(--accent)}
.spd .res{font-family:monospace;font-size:13px;font-weight:800;color:var(--accent);padding:8px;background:rgba(0,0,0,0.3);border-radius:7px;text-align:center;direction:ltr}
.ft{text-align:center;padding:20px 0;font-size:9px;color:var(--text3)}
.ft a{color:var(--accent);font-weight:700;text-decoration:none}
.tt{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);border:1px solid var(--border2);color:var(--text);border-radius:10px;padding:7px 16px;font-size:10px;font-weight:600;opacity:0;transition:.3s;z-index:999}
.tt.s{opacity:1;transform:translateX(-50%) translateY(0)}
.rkt{position:fixed;left:6px;top:50%;z-index:50;font-size:34px;color:var(--accent);cursor:pointer;animation:fl 3.5s ease-in-out infinite;filter:drop-shadow(0 0 10px rgba(255,215,0,0.3))}
@media(max-width:500px){.rkt{display:none}.s3{grid-template-columns:1fr 1fr}}
</style></head>
<body>
<audio id="bm" autoplay loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"></audio>
<script>var _m=document.getElementById('bm');_m.volume=0.07;</script>
<div class="tt" id="tt"></div>
<div class="rkt" id="rk" onclick="fr()">🚀</div>
<div id="ex" style="position:fixed;width:80px;height:80px;pointer-events:none;z-index:60;opacity:0;border-radius:50%;background:radial-gradient(circle,#ffd700,transparent 70%);left:0;top:0"></div>
<div class="wrap">
<div class="hd">
  <div class="av"><i class="ti ti-bolt"></i></div>
  <div class="cn">VaslZone</div>
  <div style="font-size:9px;color:var(--text3);letter-spacing:.2em;text-transform:uppercase;margin-top:4px">SUBSCRIPTION</div>
  <a class="tg" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
</div>
<div id="root"><div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-loader-2" style="font-size:32px;color:var(--accent);display:inline-block;animation:spin 1.2s linear infinite"></i><p style="margin-top:8px;font-size:11px">در حال بارگذاری...</p></div></div>
<div class="ft"><a href="https://t.me/VaslZone">@VaslZone</a> · v9.3</div>
</div>
<style>@keyframes spin{to{transform:rotate(360deg)}}</style>
<script>
document.body.innerHTML = '<div style="color:red;font-size:20px">JS RAN</div>' + document.body.innerHTML;
var A="API_URL",L=[],ch=null;
function B(b){if(!b||b===0)return'0';if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function E(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function N(n){return String(n).replace(/\d/g,function(d){return'۰۱۲۳۴۵۶۷۸۹'[d]})}
function T(m){var t=document.getElementById('tt');t.textContent='\u2705 '+m;t.className='tt s';setTimeout(function(){t.classList.remove('s')},1800)}
function GD(){return fetch(A).then(function(r){if(!r.ok)throw Error();return r.json()}).catch(function(){return null})}
function Q(u){if(u)window.open('https://api.qrserver.com/v1/create-qr-code/?size=240x240&data='+encodeURIComponent(u),'_blank')}
function SV(i){var e=document.getElementById('v-'+i);if(e)e.classList.toggle('s')}
function CP(t){navigator.clipboard.writeText(t).then(function(){T('کپی شد')})}
function CA(){var t=L.map(function(l){return l.vless_link||''}).filter(Boolean).join('\n');if(t)navigator.clipboard.writeText(t).then(function(){T('همه کپی شد')})}
function fr(){
  var r=document.getElementById('rk');if(r.dataset.f)return;r.dataset.f='1';
  r.style.animation='rLaunch 1.3s ease-in forwards';
  setTimeout(function(){
    var e=document.getElementById('ex');e.style.top=(window.innerHeight/2-40)+'px';
    e.style.opacity='1';e.style.animation='rExplode .7s ease-out forwards';r.style.display='none';
    setTimeout(function(){e.style.opacity='0';e.style.animation='';r.style.display='';r.style.animation='';r.dataset.f=''},800);
  },1300);
}
function TS(){var b=document.getElementById('sB'),r=document.getElementById('sR');if(b.disabled)return;b.disabled=true;r.textContent='⏳...';var s=Date.now();fetch(A+'?_='+s).then(function(re){re.json().then(function(){var ms=Date.now()-s;r.textContent=(ms<50?'🟢':ms<150?'🟡':'🔴')+' '+ms+'ms';b.disabled=false})}).catch(function(){r.textContent='🔴 خطا';b.disabled=false})}
function IC(){var c=document.getElementById('ch');if(!c||typeof Chart==='undefined')return;if(ch)ch.destroy();var v=[];for(var i=0;i<24;i++)v.push(Math.random()*50);ch=new Chart(c.getContext('2d'),{type:'line',data:{labels:Array(24).fill(''),datasets:[{label:'MB',data:v,borderColor:'#ffd700',backgroundColor:'rgba(255,215,0,0.1)',fill:true,tension:.4,pointRadius:2,borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(13,13,10,0.95)',titleColor:'#ffd700',bodyColor:'#c8c8a0',padding:10,cornerRadius:8,displayColors:false}}},scales:{x:{grid:{display:false},ticks:{color:'#6b6b40',font:{size:8}}},y:{grid:{color:'rgba(255,215,0,0.05)'},ticks:{color:'#6b6b40',font:{size:8}}}}}});}
function R(d){
if(!d||!d.links||!d.links.length){document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-link-off" style="font-size:36px;display:block;margin-bottom:12px;opacity:.3"></i><p>کانفیگی یافت نشد</p></div>';return}
L=d.links;var a=d.links.filter(function(l){return l.active}).length;var u=d.links.reduce(function(s,l){return s+(l.used_bytes||0)},0);
var h='<div class="cd" style="text-align:center"><div style="font-size:15px;font-weight:800">'+E(d.name||'')+'</div>'+(d.desc?'<div style="font-size:10px;color:var(--text2);margin-top:2px">'+E(d.desc)+'</div>':'')+'</div>';
h+='<div class="s3"><div><div class="l">وضعیت</div><div class="v">'+(d.links.length===1?(d.links[0].active?'فعال':'غیرفعال'):N(a)+'/'+N(d.links.length))+'</div></div><div><div class="l">مصرف</div><div class="v" style="font-size:17px">'+B(u)+'</div></div><div><div class="l">اتصالات</div><div class="v">'+N(d.active_connections||0)+'</div></div></div>';
if(d.links.length>1)h+='<div class="cp"><div class="t"><i class="ti ti-copy"></i> کپی همه</div><button onclick="CA()">کپی ('+N(a)+')</button></div>';
h+='<div class="chart-c"><div class="chart-h"><i class="ti ti-chart-bar"></i> نمودار مصرف</div><div class="chart-b"><canvas id="ch"></canvas></div></div>';
for(var i=0;i<d.links.length;i++){var l=d.links[i];var p=l.limit_bytes>0?Math.min(100,(l.used_bytes/l.limit_bytes)*100):0;var rm=l.limit_bytes>0?Math.max(0,l.limit_bytes-l.used_bytes):-1;var rc=rm<0?'g':(rm<1048576?'r':(rm<1073741824?'y':'g'));h+='<div class="cfg"><div class="r1"><span class="nm">'+E(l.label)+'</span><span class="st '+(l.active?'on':'off')+'">'+(l.active?'● فعال':'○ غیرفعال')+'</span></div><div class="u"><span>مصرف: <b>'+l.used_fmt+'</b></span><span>از <b>'+(l.limit_bytes===0?'∞':l.limit_fmt)+'</b></span></div><div class="bar"><div class="f" style="width:'+p+'%"></div></div><span class="rm '+rc+'">'+(rm<0?'∞':B(rm))+'</span><div class="vl" id="v-'+i+'">'+E(l.vless_link||'')+'</div><div class="btns"><button class="y" onclick="SV('+i+')"><i class="ti ti-eye"></i> نمایش</button><button class="y" onclick="CP(L['+i+'].vl)"><i class="ti ti-copy"></i> کپی</button><button class="o" onclick="Q(L['+i+'].vl)"><i class="ti ti-qrcode"></i></button></div></div>'}
h+='<div class="spd"><div class="tp"><div class="tt"><i class="ti ti-bolt"></i> تست سرعت</div><button style="padding:5px 12px;border-radius:7px;border:1px solid var(--border);background:rgba(255,215,0,0.06);color:var(--accent);font:inherit;font-size:9.5px;font-weight:700;cursor:pointer" id="sB" onclick="TS()">شروع</button></div><div class="res" id="sR">-</div></div>';
document.getElementById('root').innerHTML=h;window._L=d.links.map(function(l,i){return{vl:l.vless_link||''}});try{setTimeout(IC,300)}catch(e){}}
GD().then(function(d){if(d)R(d);else document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-alert-circle" style="font-size:36px;color:var(--red);display:block;margin-bottom:10px"></i><p>خطا</p></div>'});
</script>
</body></html>"""
    ).replace("API_URL", api_url)

def get_public_page_html(u):
    return get_sub_page_html(f"/api/public/sub/{u}")

def get_single_sub_page_html(u):
    return get_sub_page_html(f"/api/public/sub-single/{u}")
