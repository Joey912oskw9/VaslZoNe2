from fastapi.responses import HTMLResponse

def get_sub_page_html(api_url):
    return (r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>VaslZone</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#070704;--card:#0f0f0b;--gold:#ffd700;--text:#f5f5dc;--text2:#bdb76b;--text3:#5a5a35;--green:#66bb6a;--red:#ef5350;--border:rgba(255,215,0,0.10)}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
body{font-family:Vazirmatn,sans-serif;background:radial-gradient(ellipse 70% 30% at 50% -5%,rgba(255,215,0,0.05),transparent),var(--bg);color:var(--text);direction:rtl;min-height:100vh;padding:0 0 50px}
.wrap{max-width:560px;margin:0 auto;padding:16px 12px;animation:fade .6s}
.hd{text-align:center;padding:20px 0}
.av{width:72px;height:72px;border-radius:20px;margin:0 auto 10px;background:linear-gradient(135deg,var(--gold),#ffc107);display:flex;align-items:center;justify-content:center;font-size:34px;color:#000;animation:float 5s ease-in-out infinite;box-shadow:0 0 0 4px rgba(255,215,0,0.1)}
.cn{font-size:24px;font-weight:900;background:linear-gradient(135deg,var(--gold),#ffe44d);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.tg{display:inline-flex;align-items:center;gap:5px;margin-top:6px;padding:4px 12px;border-radius:20px;background:rgba(255,215,0,0.06);border:1px solid var(--border);color:var(--gold);text-decoration:none;font-size:9px;font-weight:600}
.cd{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 15px;margin-bottom:10px;animation:fade .4s}
.cd:hover{border-color:rgba(255,215,0,0.2)}
.s3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:12px}
.s3>div{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px 8px;text-align:center}
.s3>div .l{font-size:7.5px;color:var(--text3);font-weight:700;text-transform:uppercase;margin-bottom:5px}
.s3>div .v{font-size:18px;font-weight:800;color:var(--gold)}
.cfg{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:8px;border-right:2px solid var(--gold)}
.cfg .r1{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.cfg .nm{font-size:13px;font-weight:700}
.cfg .st{font-size:8px;padding:2px 7px;border-radius:10px;font-weight:700}
.cfg .st.on{background:rgba(102,187,106,0.1);color:var(--green)}
.cfg .st.off{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg .u{font-size:9.5px;color:var(--text2);display:flex;justify-content:space-between;margin-bottom:4px}
.cfg .u b{color:#ffe44d}
.cfg .bar{height:4px;border-radius:2px;background:rgba(255,215,0,0.06);overflow:hidden;margin-bottom:4px}
.cfg .bar .f{height:100%;background:var(--gold);border-radius:2px;transition:width .4s}
.cfg .rm{font-size:9px;padding:2px 8px;border-radius:5px;display:inline-block;margin-bottom:5px}
.cfg .rm.g{background:rgba(102,187,106,0.1);color:var(--green)}
.cfg .rm.y{background:rgba(255,215,0,0.06);color:var(--gold)}
.cfg .rm.r{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg .vl{display:none;background:rgba(0,0,0,0.3);border:1px solid var(--border);border-radius:7px;padding:7px 9px;font-family:monospace;font-size:8.5px;color:#ffe44d;word-break:break-all;margin-top:6px;max-height:55px;overflow-y:auto;direction:ltr;text-align:left}
.cfg .vl.s{display:block}
.btns{display:flex;gap:5px;margin-top:6px}
.btns button{font-family:inherit;font-size:9.5px;font-weight:700;padding:6px 12px;border-radius:7px;cursor:pointer;border:none;flex:1;display:flex;align-items:center;gap:3px;justify-content:center;transition:.15s}
.btns .y{background:linear-gradient(135deg,var(--gold),#ffc107);color:#000}
.btns .y:hover{transform:translateY(-1px)}
.btns .o{background:transparent;border:1px solid var(--border);color:var(--text2)}
.btns .o:hover{background:rgba(255,215,0,0.06)}
.spd{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-top:6px}
.spd .tp{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.spd .tp .tt{font-size:10px;font-weight:700;color:var(--text2);display:flex;align-items:center;gap:5px}
.spd .tp .tt i{color:var(--gold)}
.spd .res{font-family:monospace;font-size:13px;font-weight:800;color:var(--gold);padding:8px;background:rgba(0,0,0,0.25);border-radius:7px;text-align:center;direction:ltr}
.cp-all{background:linear-gradient(135deg,var(--gold),#ffc107);border-radius:10px;padding:12px 14px;margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.cp-all .t{font-size:11px;font-weight:800;color:#000}
.cp-all button{background:#000;color:var(--gold);border:none;padding:8px 16px;border-radius:8px;font-weight:700;cursor:pointer;font-size:9.5px;font-family:inherit}
.tt{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);border:1px solid rgba(255,215,0,0.2);color:var(--text);border-radius:10px;padding:7px 16px;font-size:10px;opacity:0;transition:.25s;z-index:999;white-space:nowrap}
.tt.s{opacity:1;transform:translateX(-50%) translateY(0)}
.rkt{position:fixed;left:6px;top:50%;z-index:50}
.rkt div{font-size:34px;color:var(--gold);cursor:pointer;animation:float 3.5s ease-in-out infinite;filter:drop-shadow(0 0 10px rgba(255,215,0,0.3))}
.ft{text-align:center;padding:20px 0;font-size:9px;color:var(--text3)}
.ft a{color:var(--gold);font-weight:700;text-decoration:none}
@media(max-width:500px){.rkt{display:none}.s3{grid-template-columns:1fr 1fr}}
@keyframes spin{to{transform:rotate(360deg)}}
</style></head>
<body>
<audio id="m" autoplay loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"></audio>
<script>var _m=document.getElementById('m');_m.volume=0.06;</script>
<div class="tt" id="tt"></div>
<div class="rkt"><div id="rk" onclick="fr()"><i class="ti ti-rocket"></i></div></div>
<div class="wrap">
<div class="hd">
  <div class="av"><i class="ti ti-bolt"></i></div>
  <div class="cn">VaslZone</div>
  <a class="tg" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
</div>
<div id="root"><div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-loader-2" style="font-size:32px;color:var(--gold);display:inline-block;animation:spin 1.2s linear infinite"></i><p style="margin-top:8px;font-size:11px">\u0644\u0648\u062f...</p></div></div>
<div class="ft"><a href="https://t.me/VaslZone">@VaslZone</a> \u00b7 v9.3</div>
</div>
<script>
var A="API_URL",L=[];
function B(b){if(!b||b===0)return'0';if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function E(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function N(n){return String(n).replace(/\d/g,function(d){return'\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669'[d]})}
function T(m){var t=document.getElementById('tt');t.textContent='\u2705 '+m;t.className='tt s';setTimeout(function(){t.classList.remove('s')},1800)}
async function GD(){try{var r=await fetch(A);if(!r.ok)throw Error();return await r.json()}catch(e){return null}}
function Q(u){if(u)window.open('https://api.qrserver.com/v1/create-qr-code/?size=240x240&data='+encodeURIComponent(u),'_blank')}
function SV(i){var e=document.getElementById('v-'+i);if(e)e.classList.toggle('s')}
function CP(t){navigator.clipboard.writeText(t).then(function(){T('\u06a9\u067e\u06cc \u0634\u062f')})}
function CA(){var t=L.map(function(l){return l.vless_link||''}).filter(Boolean).join('\n');if(t)navigator.clipboard.writeText(t).then(function(){T('\u0647\u0645\u0647 \u06a9\u067e\u06cc \u0634\u062f')})}
function fr(){var r=document.getElementById('rk');if(r.dataset.f)return;r.dataset.f='1';r.style.animation='launch 1.2s ease-in forwards';setTimeout(function(){r.style.animation='';r.dataset.f=''},1500)}
function TS(){var b=document.getElementById('sB'),r=document.getElementById('sR');if(b.disabled)return;b.disabled=true;r.textContent='\u23f3...';try{var s=Date.now();fetch(A+'?_='+s).then(function(re){re.json().then(function(){var ms=Date.now()-s;r.textContent=(ms<50?'\ud83d\udfe2':ms<150?'\ud83d\udfe1':'\ud83d\udd34')+' '+ms+'ms';b.disabled=false})})}catch(e){r.textContent='\ud83d\udd34 \u062e\u0637\u0627';b.disabled=false}}
function R(d){
if(!d||!d.links||!d.links.length){document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-link-off" style="font-size:36px;display:block;margin-bottom:12px;opacity:.3"></i><p>\u06a9\u0627\u0646\u0641\u06cc\u06af\u06cc \u0646\u06cc\u0633\u062a</p></div>';return}
L=d.links;var a=d.links.filter(function(l){return l.active}).length;var u=d.links.reduce(function(s,l){return s+(l.used_bytes||0)},0);
var h='<div class="cd" style="text-align:center"><div style="font-size:14px;font-weight:800">'+E(d.name||'')+'</div>'+(d.desc?'<div style="font-size:10px;color:var(--text2);margin-top:2px">'+E(d.desc)+'</div>':'')+'</div>';
h+='<div class="s3"><div><div class="l">\u0648\u0636\u0639\u06cc\u062a</div><div class="v">'+(d.links.length===1?(d.links[0].active?'\u0641\u0639\u0627\u0644':'\u063a\u06cc\u0631\u0641\u0639\u0627\u0644'):N(a)+'/'+N(d.links.length))+'</div></div><div><div class="l">\u0645\u0635\u0631\u0641</div><div class="v" style="font-size:16px">'+B(u)+'</div></div><div><div class="l">\u0627\u062a\u0635\u0627\u0644\u0627\u062a</div><div class="v">'+N(d.active_connections||0)+'</div></div></div>';
if(d.links.length>1)h+='<div class="cp-all"><div class="t"><i class="ti ti-copy"></i> \u06a9\u067e\u06cc \u0647\u0645\u0647</div><button onclick="CA()">\u06a9\u067e\u06cc ('+N(a)+')</button></div>';
for(var i=0;i<d.links.length;i++){var l=d.links[i];var p=l.limit_bytes>0?Math.min(100,(l.used_bytes/l.limit_bytes)*100):0;var rm=l.limit_bytes>0?Math.max(0,l.limit_bytes-l.used_bytes):-1;var rc=rm<0?'g':(rm<1048576?'r':(rm<1073741824?'y':'g'));h+='<div class="cfg"><div class="r1"><span class="nm">'+E(l.label)+'</span><span class="st '+(l.active?'on':'off')+'">'+(l.active?'\u25cf \u0641\u0639\u0627\u0644':'\u25cb \u063a\u06cc\u0631\u0641\u0639\u0627\u0644')+'</span></div><div class="u"><span>\u0645\u0635\u0631\u0641: <b>'+l.used_fmt+'</b></span><span>\u0627\u0632 <b>'+(l.limit_bytes===0?'\u221e':l.limit_fmt)+'</b></span></div><div class="bar"><div class="f" style="width:'+p+'%"></div></div><span class="rm '+rc+'"><i class="ti ti-'+(rm<0?'infinity':'database')+'"></i> '+(rm<0?'\u221e \u0646\u0627\u0645\u062d\u062f\u0648\u062f':'\u0628\u0627\u0642\u06cc: '+B(rm))+'</span><div class="vl" id="v-'+i+'">'+E(l.vless_link||'')+'</div><div class="btns"><button class="y" onclick="SV('+i+')"><i class="ti ti-eye"></i></button><button class="y" onclick="CP(L['+i+'].vl)"><i class="ti ti-copy"></i> \u06a9\u067e\u06cc</button><button class="o" onclick="Q(L['+i+'].vl)"><i class="ti ti-qrcode"></i></button></div></div>'}
h+='<div class="spd"><div class="tp"><div class="tt"><i class="ti ti-bolt"></i> \u067e\u06cc\u0646\u06af</div><button style="padding:5px 12px;border-radius:7px;border:1px solid var(--border);background:rgba(255,215,0,0.06);color:var(--gold);font:inherit;font-size:9.5px;font-weight:700;cursor:pointer" id="sB" onclick="TS()">\u0634\u0631\u0648\u0639</button></div><div class="res" id="sR">-</div></div>';
document.getElementById('root').innerHTML=h;window._L=d.links.map(function(l,i){return{vl:l.vless_link||''}})}
(async function(){var d=await GD();if(d)R(d);else document.getElementById('root').innerHTML='<div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-alert-circle" style="font-size:36px;color:var(--red);display:block;margin-bottom:10px"></i><p>\u062e\u0637\u0627</p></div>'})();
</script>
</body></html>"""
    ).replace("API_URL", api_url)

def get_public_page_html(u):
    return get_sub_page_html(f"/api/public/sub/{u}")
def get_single_sub_page_html(u):
    return get_sub_page_html(f"/api/public/sub-single/{u}")
