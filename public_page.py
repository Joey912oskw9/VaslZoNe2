from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url: str, title: str) -> str:
    return (r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VaslZone</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#070704;--card:#0f0f0b;--card2:#151510;--gold:#ffd700;--gold2:#ffc107;--gold3:#ffe44d;--text:#f5f5dc;--text2:#bdb76b;--text3:#5a5a35;--green:#66bb6a;--red:#ef5350;--border:rgba(255,215,0,0.10);--border2:rgba(255,215,0,0.30)}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
@keyframes launch{0%{transform:translateY(0) rotate(0)}25%{transform:translateY(-30px) rotate(-5deg)}50%{transform:translateY(-60px) rotate(8deg) scale(1.1)}100%{transform:translateY(calc(100vh - 200px)) rotate(5deg) scale(0.4);opacity:0}}
@keyframes explode{0%{transform:scale(0);opacity:1}40%{transform:scale(3);opacity:.8}100%{transform:scale(5);opacity:0}}
body{font-family:Vazirmatn,sans-serif;background:radial-gradient(ellipse 70% 30% at 50% -8%,rgba(255,215,0,0.05),transparent),var(--bg);color:var(--text);direction:rtl;min-height:100vh;overflow-x:hidden;padding:0 0 60px}
.wrap{max-width:560px;margin:0 auto;padding:16px 12px 40px;position:relative;z-index:10}
.header{text-align:center;padding:24px 0 12px}
.avatar{width:76px;height:76px;border-radius:22px;margin:0 auto 12px;background:linear-gradient(135deg,var(--gold),var(--gold2));display:flex;align-items:center;justify-content:center;font-size:36px;color:#000;animation:float 5s ease-in-out infinite;box-shadow:0 0 0 4px rgba(255,215,0,0.12),0 12px 32px rgba(255,215,0,0.15)}
.chan{font-size:26px;font-weight:900;background:linear-gradient(135deg,var(--gold),var(--gold3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.sub{font-size:9px;color:var(--text3);letter-spacing:.2em;text-transform:uppercase;margin-top:4px}
.tg{display:inline-flex;align-items:center;gap:6px;margin-top:8px;padding:5px 14px;border-radius:20px;background:rgba(255,215,0,0.06);border:1px solid var(--border);color:var(--gold);text-decoration:none;font-size:10px;font-weight:600;transition:.2s}
.tg:hover{background:rgba(255,215,0,0.12);border-color:var(--border2)}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:16px 17px;margin-bottom:12px;transition:.2s}
.card:hover{border-color:var(--border2)}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}
.g3>div{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 10px;text-align:center}
.g3>div .l{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:6px}
.g3>div .v{font-size:20px;font-weight:800;color:var(--gold)}
.cfg{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 15px;margin-bottom:10px;border-right:3px solid var(--gold)}
.cfg .h{display:flex;align-items:center;justify-content:space-between;margin-bottom:7px;flex-wrap:wrap;gap:6px}
.cfg .h .nm{font-size:14px;font-weight:700;color:var(--text)}
.cfg .h .st{font-size:8.5px;padding:3px 9px;border-radius:15px;font-weight:700}
.cfg .h .st.on{background:rgba(102,187,106,0.1);color:var(--green);border:1px solid rgba(102,187,106,0.2)}
.cfg .h .st.off{background:rgba(239,83,80,0.1);color:var(--red);border:1px solid rgba(239,83,80,0.2)}
.cfg .u{font-size:10px;color:var(--text2);display:flex;justify-content:space-between;margin-bottom:5px}
.cfg .u b{color:var(--gold3)}
.cfg .bar{height:5px;border-radius:3px;background:rgba(255,215,0,0.06);overflow:hidden;margin-bottom:5px}
.cfg .bar .f{height:100%;border-radius:3px;background:var(--gold);transition:width .5s}
.cfg .rm{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;padding:3px 10px;border-radius:6px;margin-top:5px}
.cfg .rm.g{background:rgba(102,187,106,0.1);color:var(--green)}
.cfg .rm.y{background:rgba(255,215,0,0.08);color:var(--gold)}
.cfg .rm.r{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg .vls{display:none;background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:7px;padding:8px 10px;font-family:monospace;font-size:9px;color:var(--gold3);word-break:break-all;margin-top:8px;max-height:65px;overflow-y:auto;direction:ltr;text-align:left}
.cfg .vls.s{display:block}
.ac{display:flex;gap:6px;margin-top:8px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:10.5px;font-weight:700;padding:7px 14px;border-radius:8px;cursor:pointer;border:none;display:flex;align-items:center;gap:4px;transition:.15s;flex:1;justify-content:center}
.btn-g{background:linear-gradient(135deg,var(--gold),var(--gold2));color:#000;box-shadow:0 3px 12px rgba(255,215,0,0.2)}
.btn-g:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(255,215,0,0.3)}
.btn-o{background:transparent;border:1px solid var(--border);color:var(--text2)}
.btn-o:hover{background:rgba(255,215,0,0.06);color:var(--gold);border-color:var(--border2)}
.btn-s{padding:5px 10px;font-size:9px;flex:0}
.cp-all{background:linear-gradient(135deg,var(--gold),var(--gold2));border-radius:12px;padding:14px 16px;margin-bottom:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;box-shadow:0 6px 24px rgba(255,215,0,0.15)}
.cp-all .t{flex:1}.cp-all .t div{font-size:12px;font-weight:800;color:#000;display:flex;align-items:center;gap:5px}.cp-all .t span{font-size:9px;color:rgba(0,0,0,0.55)}
.cp-all button{background:#000;color:var(--gold);border:none;padding:9px 18px;border-radius:10px;font-weight:800;cursor:pointer;font-size:10px;font-family:inherit;transition:.15s}
.cp-all button:hover{transform:translateY(-2px)}
.spd{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 16px;margin-bottom:12px}
.spd .top{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.spd .top .tt{font-size:11px;font-weight:800;color:var(--text2);display:flex;align-items:center;gap:6px;text-transform:uppercase}
.spd .top .tt i{color:var(--gold)}
.spd .res{font-family:monospace;font-size:13px;font-weight:800;color:var(--gold3);padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;text-align:center;direction:ltr}
.section{font-size:11px;font-weight:800;color:var(--text2);margin-bottom:12px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.section i{color:var(--gold);font-size:15px}
.ft{text-align:center;padding:24px 0 8px;font-size:9px;color:var(--text3)}
.ft a{color:var(--gold);font-weight:700;text-decoration:none}
.tt{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);border:1px solid var(--border2);color:var(--text);border-radius:10px;padding:8px 16px;font-size:11px;opacity:0;transition:.25s;z-index:999}
.tt.s{opacity:1;transform:translateX(-50%) translateY(0)}
.rocket{position:fixed;left:6px;top:50%;z-index:50;text-align:center}
.rocket .rkt{font-size:38px;color:var(--gold);cursor:pointer;animation:float 3.5s ease-in-out infinite;filter:drop-shadow(0 0 12px rgba(255,215,0,0.4));transition:.3s}
@media(max-width:500px){.rocket{display:none}.g3{grid-template-columns:1fr 1fr}}
</style></head>
<body>
<audio id="bgMusic" autoplay loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"></audio>
<script>var m=document.getElementById('bgMusic');m.volume=0.07;</script>
<div class="tt" id="tt"></div>
<div class="rocket"><div class="rkt" id="rkt" onclick="fireRocket()"><i class="ti ti-rocket"></i></div></div>
<div class="wrap">
<div class="header">
  <div class="avatar"><i class="ti ti-bolt"></i></div>
  <div class="chan">VaslZone</div>
  <div class="sub">اشتراک اختصاصی</div>
  <a class="tg" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
</div>
<div id="root"><div style="text-align:center;padding:70px 20px;color:var(--text3)"><i class="ti ti-loader-2" style="font-size:36px;color:var(--gold);display:inline-block;animation:spin 1.2s linear infinite"></i><p style="margin-top:10px;font-size:12px">در حال بارگذاری...</p></div></div>
<div class="ft"><a href="https://t.me/VaslZone" target="_blank">@VaslZone</a> · v9.3</div>
</div>
<style>@keyframes spin{to{transform:rotate(360deg)}}</style>
<script>
var API="API_URL";
var L=[];

function B(b){if(!b||b===0)return'0';if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function E(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function N(n){return String(n).replace(/\d/g,function(d){return'۰۱۲۳۴۵۶۷۸۹'[d]})}
function T(m){var t=document.getElementById('tt');t.textContent='✅ '+m;t.className='tt s';setTimeout(function(){t.classList.remove('s')},1800)}

async function getData(){try{var r=await fetch(API);if(!r.ok)throw Error();return await r.json()}catch(e){return null}}

function Q(u){if(u)window.open('https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(u),'_blank')}
function V(i){var e=document.getElementById('v-'+i);if(e)e.classList.toggle('s')}
function C(t){navigator.clipboard.writeText(t).then(function(){T('کپی شد')})}
function CA(){var t=L.map(function(l){return l.vless_link||''}).filter(Boolean).join('\n');if(t)navigator.clipboard.writeText(t).then(function(){T('همه کپی شد')})}

function fireRocket(){
  var r=document.getElementById('rkt');
  if(r.dataset.f)return;r.dataset.f='1';
  r.style.animation='launch 1.2s ease-in forwards';
  setTimeout(function(){
    var exp=document.createElement('div');
    exp.style.cssText='position:fixed;left:10px;width:100px;height:100px;pointer-events:none;z-index:60;animation:explode .7s ease-out forwards;border-radius:50%;background:radial-gradient(circle,#ffd700,transparent 70%)';
    exp.style.top=(window.innerHeight/2)+'px';
    document.body.appendChild(exp);
    setTimeout(function(){exp.remove();r.style.animation='';r.dataset.f='';window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'})},800);
  },1200);
}

async function speedTest(){
  var btn=document.getElementById('sBtn'),r=document.getElementById('sRes');
  if(btn.disabled)return;
  btn.disabled=true;r.textContent='⏳ تست...';
  try{var s=Date.now();var re=await fetch(API+'?_='+s);var d=await re.json();var ms=Date.now()-s;r.textContent=(ms<50?'🟢':ms<150?'🟡':'🔴')+' پینگ: '+ms+'ms'}catch(e){r.textContent='🔴 خطا'}
  btn.disabled=false;
}

function render(d){
  if(!d||!d.links||!d.links.length){
    document.getElementById('root').innerHTML='<div style="text-align:center;padding:80px 20px;color:var(--text3)"><i class="ti ti-link-off" style="font-size:40px;display:block;margin-bottom:14px;opacity:.3"></i><p>کانفیگی موجود نیست</p></div>';return}
  L=d.links;
  var a=d.links.filter(function(l){return l.active}).length;
  var u=d.links.reduce(function(s,l){return s+(l.used_bytes||0)},0);
  var h='';
  h+='<div class="card" style="text-align:center"><div style="font-size:15px;font-weight:800">'+E(d.name||'VaslZone')+'</div>'+(d.desc?'<div style="font-size:11px;color:var(--text2);margin-top:3px;line-height:1.6">'+E(d.desc)+'</div>':'')+'</div>';
  h+='<div class="g3"><div><div class="l">وضعیت</div><div class="v">'+(d.links.length===1?(d.links[0].active?'فعال':'غیرفعال'):N(a)+'/'+N(d.links.length))+'</div></div><div class="l" style="display:none"></div><div><div class="l">مصرف</div><div class="v" style="font-size:17px">'+B(u)+'</div></div><div><div class="l">اتصالات</div><div class="v">'+N(d.active_connections||0)+'</div></div></div>';
  if(d.links.length>1)h+='<div class="cp-all"><div class="t"><div><i class="ti ti-copy"></i> کپی همه کانفیگ‌ها</div><span>یکبار کلیک</span></div><button onclick="CA()"><i class="ti ti-clipboard-copy"></i> کپی ('+N(a)+')</button></div>';
  h+='<div class="section"><i class="ti ti-link"></i> کانفیگ‌ها</div>';
  for(var i=0;i<d.links.length;i++){
    var l=d.links[i];
    var p=l.limit_bytes>0?Math.min(100,(l.used_bytes/l.limit_bytes)*100):0;
    var rm=l.limit_bytes>0?Math.max(0,l.limit_bytes-l.used_bytes):-1;
    var rc=rm<0?'g':(rm<1048576?'r':(rm<1073741824?'y':'g'));
    var rf=rm<0?'∞':B(rm);
    h+='<div class="cfg"><div class="h"><span class="nm">'+E(l.label)+'</span><span class="st '+(l.active?'on':'off')+'">'+(l.active?'● فعال':'○ غیرفعال')+'</span></div><div class="u"><span>مصرف: <b>'+l.used_fmt+'</b></span><span>از <b>'+l.limit_fmt+'</b></span></div><div class="bar"><div class="f" style="width:'+p+'%"></div></div><span class="rm '+rc+'"><i class="ti ti-'+(rm<0?'infinity':'database')+'"></i> '+(rm<0?'نامحدود':'باقی: '+rf)+'</span><div class="vls" id="v-'+i+'">'+E(l.vless_link||'')+'</div><div class="ac"><button class="btn btn-g" onclick="V('+i+')"><i class="ti ti-eye"></i> نمایش</button><button class="btn btn-g" onclick="C(L['+i+'].vl)"><i class="ti ti-copy"></i> کپی</button><button class="btn btn-o btn-s" onclick="Q(L['+i+'].vl)"><i class="ti ti-qrcode"></i></button></div></div>'
  }
  h+='<div class="spd"><div class="top"><div class="tt"><i class="ti ti-speedtest"></i> تست سرعت</div><button style="padding:6px 14px;border-radius:8px;border:1px solid var(--border);background:rgba(255,215,0,0.06);color:var(--gold);font:inherit;font-size:10px;font-weight:700;cursor:pointer" id="sBtn" onclick="speedTest()"><i class="ti ti-player-play"></i> شروع</button></div><div class="res" id="sRes">کلیک کنید</div></div>';
  document.getElementById('root').innerHTML=h;
  window._L=d.links.map(function(l,i){return{vl:l.vless_link||''}});
}

(async function(){var d=await getData();if(d)render(d);else document.getElementById('root').innerHTML='<div style="text-align:center;padding:80px 20px;color:var(--text3)"><i class="ti ti-alert-circle" style="font-size:40px;color:var(--red);display:block;margin-bottom:14px"></i><p>خطا در بارگذاری</p></div>'})();
</script>
</body></html>"""
    ).replace("API_URL", api_url)

def get_public_page_html(uuid_key: str) -> str:
    return get_sub_page_html(api_url=f"/api/public/sub/{uuid_key}")

def get_single_sub_page_html(uuid: str) -> str:
    return get_sub_page_html(api_url=f"/api/public/sub-single/{uuid}")
