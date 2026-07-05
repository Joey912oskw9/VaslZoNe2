from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url, title="VaslZone", subtitle=""):
    return (r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>VaslZone</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050504;--card:#0d0d0a;--card2:#141410;--accent:#FFD700;--accent2:#FFC107;--text:#F5F5DC;--text2:#C8C8A0;--text3:#6B6B40;--green:#66BB6A;--red:#EF5350;--border:rgba(255,215,0,0.08)}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
body{font-family:Vazirmatn,sans-serif;background:radial-gradient(ellipse 80% 35% at 50% -5%,rgba(255,215,0,0.04),transparent),var(--bg);color:var(--text);direction:rtl;min-height:100vh;padding-bottom:40px}
.wrap{max-width:560px;margin:0 auto;padding:16px 14px}
.hd{text-align:center;padding:24px 0 10px}
.av{width:72px;height:72px;border-radius:20px;margin:0 auto 10px;background:linear-gradient(145deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:34px;color:#000;animation:fl 4s ease-in-out infinite}
.cn{font-size:22px;font-weight:900;background:linear-gradient(135deg,var(--accent),#ffe44d);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.cd{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:16px 18px;margin-bottom:10px}
.s3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}
.s3>div{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px 10px;text-align:center}
.s3>div .l{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;margin-bottom:5px}
.s3>div .v{font-size:18px;font-weight:800;color:var(--accent)}
.cfg{background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:12px 14px;margin-bottom:8px;border-right:2px solid var(--accent)}
.cfg .h{display:flex;justify-content:space-between;margin-bottom:6px}
.cfg .nm{font-size:13px;font-weight:700}
.cfg .st{font-size:8px;padding:2px 7px;border-radius:10px;font-weight:700}
.cfg .st.on{background:rgba(102,187,106,0.1);color:var(--green)}
.cfg .st.off{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg .u{font-size:9.5px;color:var(--text2);display:flex;justify-content:space-between;margin-bottom:4px}
.cfg .u b{color:var(--text)}
.cfg .bar{height:4px;border-radius:3px;background:rgba(255,215,0,0.06);overflow:hidden;margin-bottom:4px}
.cfg .bar .f{height:100%;background:var(--accent);border-radius:3px}
.cfg .rm{font-size:9px;font-weight:700;padding:2px 8px;border-radius:5px;display:inline-block}
.cfg .rm.g{background:rgba(102,187,106,0.1);color:var(--green)}
.cfg .rm.y{background:rgba(255,215,0,0.08);color:var(--accent)}
.cfg .rm.r{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg .vl{display:none;background:rgba(0,0,0,0.4);border-radius:7px;padding:7px 9px;font-family:monospace;font-size:8px;color:var(--accent);word-break:break-all;margin-top:6px;direction:ltr;text-align:left}
.cfg .vl.s{display:block}
.btns{display:flex;gap:5px;margin-top:6px}
.btns button{font:inherit;font-size:9.5px;font-weight:700;padding:6px 12px;border-radius:7px;cursor:pointer;border:none;flex:1;transition:.15s}
.btns .y{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000}
.btns .o{background:transparent;border:1px solid var(--border);color:var(--text2)}
.spd{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px 14px;margin-top:6px}
.spd .tp{display:flex;justify-content:space-between;margin-bottom:6px}
.spd .tt{font-size:10px;font-weight:700;color:var(--text2);display:flex;align-items:center;gap:5px}
.spd .tt i{color:var(--accent)}
.spd .res{font-family:monospace;font-size:13px;font-weight:800;color:var(--accent);padding:8px;background:rgba(0,0,0,0.3);border-radius:7px;text-align:center;direction:ltr}
.ft{text-align:center;padding:20px 0;font-size:9px;color:var(--text3)}
.ft a{color:var(--accent);font-weight:700;text-decoration:none}
.tt{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);border:1px solid var(--border);color:var(--text);border-radius:10px;padding:7px 16px;font-size:10px;opacity:0;transition:.25s;z-index:999}
.tt.s{opacity:1;transform:translateX(-50%) translateY(0)}
@media(max-width:500px){.s3{grid-template-columns:1fr 1fr}}
</style></head>
<body>
<audio id="m" autoplay loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"></audio>
<script>document.getElementById('m').volume=0.07;</script>
<div class="tt" id="tt"></div>
<div class="wrap">
<div class="hd"><div class="av"><i class="ti ti-bolt"></i></div><div class="cn">VaslZone</div><a style="color:var(--accent);font-size:10px;font-weight:600;text-decoration:none;margin-top:6px;display:inline-block" href="https://t.me/VaslZone" target="_blank">@VaslZone</a></div>
<div id="root"><div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-loader-2" style="font-size:32px;color:var(--accent);display:inline-block;animation:spin 1.2s linear infinite"></i><p style="margin-top:8px;font-size:11px">بارگذاری...</p></div></div>
<div class="ft"><a href="https://t.me/VaslZone">@VaslZone</a> v9.3</div>
</div>
<style>@keyframes spin{to{transform:rotate(360deg)}}</style>
<script>
var A="API_URL",L=[];
function B(b){if(!b||b===0)return'0';if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function E(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function N(n){return String(n).replace(/\d/g,function(d){return'۰۱۲۳۴۵۶۷۸۹'[d]})}
function T(m){var t=document.getElementById('tt');t.textContent='\u2705 '+m;t.className='tt s';setTimeout(function(){t.classList.remove('s')},1800)}
async function LD(){try{var r=await fetch(A);if(!r.ok)throw Error();return await r.json()}catch(e){return null}}
function Q(u){if(u)window.open('https://api.qrserver.com/v1/create-qr-code/?size=240x240&data='+encodeURIComponent(u),'_blank')}
function SV(i){var e=document.getElementById('v-'+i);if(e)e.classList.toggle('s')}
function CP(t){navigator.clipboard.writeText(t).then(function(){T('کپی شد')})}
function CA(){var t=L.map(function(l){return l.vless_link||''}).filter(Boolean).join('\n');if(t)navigator.clipboard.writeText(t).then(function(){T('همه کپی شد')})}
function TS(){var b=document.getElementById('sB'),r=document.getElementById('sR');if(b.disabled)return;b.disabled=true;r.textContent='⏳...';var s=Date.now();fetch(A+'?_='+s).then(function(re){re.json().then(function(){r.textContent=(Date.now()-s<50?'🟢':Date.now()-s<150?'🟡':'🔴')+' '+(Date.now()-s)+'ms';b.disabled=false})}).catch(function(){r.textContent='🔴 خطا';b.disabled=false})}
function R(d){
if(!d||!d.links||!d.links.length){document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-link-off" style="font-size:36px;display:block;margin-bottom:12px;opacity:.3"></i><p>کانفیگی نیست</p></div>';return}
L=d.links;var a=d.links.filter(function(l){return l.active}).length,u=d.links.reduce(function(s,l){return s+(l.used_bytes||0)},0);
var h='<div class="cd" style="text-align:center"><div style="font-size:15px;font-weight:800">'+E(d.name||'')+'</div>'+(d.desc?'<div style="font-size:10px;color:var(--text2);margin-top:2px">'+E(d.desc)+'</div>':'')+'</div>';
h+='<div class="s3"><div><div class="l">وضعیت</div><div class="v">'+(d.links.length===1?(d.links[0].active?'فعال':'غیرفعال'):N(a)+'/'+N(d.links.length))+'</div></div><div><div class="l">مصرف</div><div class="v" style="font-size:16px">'+B(u)+'</div></div><div><div class="l">اتصالات</div><div class="v">'+N(d.active_connections||0)+'</div></div></div>';
for(var i=0;i<d.links.length;i++){var l=d.links[i];var p=l.limit_bytes>0?Math.min(100,(l.used_bytes/l.limit_bytes)*100):0;var rm=l.limit_bytes>0?Math.max(0,l.limit_bytes-l.used_bytes):-1;var rc=rm<0?'g':(rm<1048576?'r':(rm<1073741824?'y':'g'));h+='<div class="cfg"><div class="h"><span class="nm">'+E(l.label)+'</span><span class="st '+(l.active?'on':'off')+'">'+(l.active?'● فعال':'○ غیرفعال')+'</span></div><div class="u"><span>مصرف: <b>'+l.used_fmt+'</b></span><span>از <b>'+(l.limit_bytes===0?'∞':l.limit_fmt)+'</b></span></div><div class="bar"><div class="f" style="width:'+p+'%"></div></div><span class="rm '+rc+'">'+(rm<0?'∞':B(rm))+'</span><div class="vl" id="v-'+i+'">'+E(l.vless_link||'')+'</div><div class="btns"><button class="y" onclick="SV('+i+')">نمایش</button><button class="y" onclick="CP(L['+i+'].vless_link)">کپی</button><button class="o" onclick="Q(L['+i+'].vless_link)">QR</button></div></div>'}
h+='<div class="spd"><div class="tp"><div class="tt"><i class="ti ti-bolt"></i> تست</div><button style="padding:5px 12px;border-radius:7px;border:1px solid var(--border);background:rgba(255,215,0,0.06);color:var(--accent);font:inherit;font-size:9.5px;font-weight:700;cursor:pointer" id="sB" onclick="TS()">start</button></div><div class="res" id="sR">-</div></div>';
document.getElementById('root').innerHTML=h}
(async function(){var d=await LD();if(d)R(d);else document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-alert-circle" style="font-size:36px;color:var(--red);display:block;margin-bottom:10px"></i><p>خطا</p></div>'})();
</script>
</body></html>"""
    ).replace("API_URL", api_url)

def get_public_page_html(u):
    return get_sub_page_html(f"/api/public/sub/{u}")
def get_single_sub_page_html(u):
    return get_sub_page_html(f"/api/public/sub-single/{u}")
