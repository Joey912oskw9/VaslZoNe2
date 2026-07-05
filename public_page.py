from fastapi.responses import HTMLResponse
from urllib.parse import quote

def get_sub_page_html(api_url: str, title: str) -> str:
    html = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VaslZone · اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{--bg:#0a0a05;--bg2:#0d0d08;--card:#12120e;--card2:#1a1a14;--yellow:#ffd700;--yellow2:#ffc107;--yellow3:#ffe44d;--text:#f5f5dc;--text2:#bdb76b;--text3:#6b6b40;--green:#66bb6a;--red:#ef5350;--border:rgba(255,215,0,0.12);--border2:rgba(255,215,0,0.3)}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
@keyframes launch{0%{transform:translateY(0) rotate(0)}30%{transform:translateY(-40px) rotate(-10deg)}60%{transform:translateY(-80px) rotate(10deg) scale(1.2)}100%{transform:translateY(calc(100vh - 150px)) rotate(5deg) scale(0.5);opacity:0}}
@keyframes explode{0%{transform:scale(1);opacity:1}50%{transform:scale(4);opacity:.5}100%{transform:scale(0);opacity:0}}
@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
body{font-family:Vazirmatn,sans-serif;background:radial-gradient(ellipse 80% 35% at 50% -5%,rgba(255,215,0,0.06),transparent),var(--bg);color:var(--text);direction:rtl;min-height:100vh;overflow-x:hidden;position:relative}
.grid-bg{position:fixed;inset:0;background-image:linear-gradient(rgba(255,215,0,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,215,0,0.02) 1px,transparent 1px);background-size:45px 45px;z-index:0}
.wrap{position:relative;z-index:10;max-width:560px;margin:0 auto;padding:16px 12px 60px}
.header{text-align:center;padding:20px 0 10px}
.profile-pic{width:80px;height:80px;border-radius:24px;margin:0 auto 14px;background:linear-gradient(135deg,var(--yellow),var(--yellow2));display:flex;align-items:center;justify-content:center;font-size:38px;color:#000;box-shadow:0 0 0 4px rgba(255,215,0,0.15),0 12px 36px rgba(255,215,0,0.2);animation:float 4s ease-in-out infinite}
.ch-name{font-size:28px;font-weight:900;background:linear-gradient(135deg,var(--yellow),var(--yellow3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-shadow:0 0 40px rgba(255,215,0,0.2)}
.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:16px 17px;margin-bottom:12px;position:relative;overflow:hidden;backdrop-filter:blur(6px)}
.card::before{content:'';position:absolute;top:-50px;left:-50px;width:150px;height:150px;background:radial-gradient(circle,rgba(255,215,0,0.05),transparent 70%)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}
.stat{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 12px;text-align:center;transition:.2s}
.stat:hover{border-color:var(--border2);transform:translateY(-2px)}
.stat .sl{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}
.stat .sv{font-size:20px;font-weight:800;color:var(--yellow)}
.cfg-card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 15px;margin-bottom:10px;border-right:3px solid var(--yellow);position:relative;transition:.2s}
.cfg-card:hover{border-color:var(--border2);transform:translateY(-2px)}
.cfg-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;flex-wrap:wrap;gap:6px}
.cfg-label{font-size:14px;font-weight:700;color:var(--text)}
.cfg-proto{font-size:8px;padding:2px 8px;border-radius:5px;font-weight:700;background:rgba(255,215,0,0.08);color:var(--yellow);border:1px solid var(--border)}
.cfg-status{font-size:9px;padding:3px 9px;border-radius:15px;font-weight:700}
.cg-ok{background:rgba(102,187,106,0.1);color:var(--green);border:1px solid rgba(102,187,106,0.25)}
.cg-off{background:rgba(239,83,80,0.1);color:var(--red);border:1px solid rgba(239,83,80,0.25)}
.cfg-bar{height:5px;border-radius:3px;background:rgba(255,215,0,0.08);overflow:hidden;margin:6px 0}
.cfg-bar-f{height:100%;border-radius:3px;background:var(--yellow);transition:width .5s}
.cfg-info{font-size:10px;color:var(--text2);display:flex;justify-content:space-between;margin-bottom:6px}
.cfg-info b{color:var(--yellow3)}
.cfg-remain{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;padding:3px 9px;border-radius:6px;margin-top:4px}
.cr-ok{background:rgba(102,187,106,0.1);color:var(--green)}
.cr-warn{background:rgba(255,215,0,0.08);color:var(--yellow)}
.cr-danger{background:rgba(239,83,80,0.1);color:var(--red)}
.cfg-link{display:none;margin-top:8px}
.cfg-link.s{display:block}
.cfg-link code{display:block;background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:8px;padding:8px 10px;font-family:monospace;font-size:9px;color:var(--yellow3);word-break:break-all;line-height:1.5;max-height:65px;overflow-y:auto;direction:ltr;text-align:left}
.cfg-actions{display:flex;gap:6px;margin-top:8px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:10.5px;font-weight:700;padding:7px 14px;border-radius:9px;cursor:pointer;border:none;display:flex;align-items:center;gap:4px;transition:.15s;flex:1;justify-content:center}
.btn-y{background:linear-gradient(135deg,var(--yellow),var(--yellow2));color:#000;box-shadow:0 3px 12px rgba(255,215,0,0.25)}
.btn-y:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(255,215,0,0.35)}
.btn-o{background:transparent;border:1px solid var(--border);color:var(--text2)}
.btn-o:hover{background:rgba(255,215,0,0.08);color:var(--yellow);border-color:var(--border2)}
.btn-sm{padding:5px 10px;font-size:9px;flex:0}
.copy-all{background:linear-gradient(135deg,var(--yellow),var(--yellow2));border-radius:12px;padding:14px 16px;margin-bottom:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;box-shadow:0 6px 24px rgba(255,215,0,0.2)}
.copy-all-t{flex:1}.copy-all-t div{font-size:12px;font-weight:800;color:#000}
.copy-all-t span{font-size:9px;color:rgba(0,0,0,0.6)}
.copy-all-btn{background:#000;color:var(--yellow);border:none;padding:9px 18px;border-radius:10px;font-weight:800;cursor:pointer;font-size:10px;font-family:inherit;transition:.15s}
.copy-all-btn:hover{transform:translateY(-2px)}
.chart-card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:16px 17px;margin-bottom:14px}
.chart-body{height:200px;margin-bottom:10px}
.chart-tt{font-size:11px;font-weight:800;color:var(--text2);margin-bottom:10px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.06em}
.chart-tabs{display:flex;gap:5px;flex-wrap:wrap}
.chart-tab{padding:5px 12px;border-radius:6px;font-size:9.5px;font-weight:700;background:rgba(255,215,0,0.08);color:var(--text2);border:1px solid var(--border);cursor:pointer;transition:.15s;font-family:inherit}
.chart-tab.a{background:var(--yellow);color:#000;border-color:var(--yellow)}
.chart-tip{font-size:9px;color:var(--text3);text-align:center;margin-top:8px}
.speed-card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 16px;margin-bottom:14px}
.speed-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.speed-tt{font-size:11px;font-weight:800;color:var(--text2);display:flex;align-items:center;gap:6px;text-transform:uppercase}
.speed-tt i{color:var(--yellow)}
.speed-res{font-family:monospace;font-size:13px;font-weight:800;color:var(--yellow3);padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;text-align:center;direction:ltr}
.footer{text-align:center;padding:20px 0;font-size:9px;color:var(--text3)}
.footer a{color:var(--yellow);font-weight:700;text-decoration:none}
.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);border:1px solid var(--border2);color:var(--text);border-radius:10px;padding:8px 16px;font-size:11px;opacity:0;transition:.25s;z-index:999}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
@media(max-width:450px){.stats{grid-template-columns:1fr 1fr}}
@keyframes spin{to{transform:rotate(360deg)}}
</style></head>
<body>
<div class="grid-bg"></div>
<audio id="music" loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"></audio>
<div onclick="var m=document.getElementById('music');m.volume=0.12;m.play()" style="position:fixed;bottom:16px;right:16px;width:40px;height:40px;border-radius:50%;background:var(--card);border:1px solid var(--border);color:var(--yellow);cursor:pointer;z-index:99;display:flex;align-items:center;justify-content:center;font-size:18px" id="mBtn"><i class="ti ti-music"></i></div>
<div class="toast" id="toast"></div>
<div class="wrap">
<div class="header">
  <div class="profile-pic"><i class="ti ti-bolt"></i></div>
  <div class="ch-name">VaslZone</div>
  <div style="font-size:9px;color:var(--text3);letter-spacing:.25em;text-transform:uppercase;margin-top:4px">اشتراک اختصاصی</div>
  <a style="display:inline-flex;align-items:center;gap:6px;margin-top:8px;padding:5px 14px;border-radius:20px;background:rgba(255,215,0,0.08);border:1px solid var(--border);color:var(--yellow);text-decoration:none;font-size:10px;font-weight:600" href="https://t.me/VaslZone" target="_blank"><i class="ti ti-brand-telegram"></i> @VaslZone</a>
</div>
<div id="root"><div style="text-align:center;padding:60px 20px;color:var(--text3)"><i class="ti ti-loader-2" style="font-size:36px;color:var(--yellow);display:inline-block;animation:spin 1.2s linear infinite"></i><p style="font-size:12px;margin-top:10px">بارگذاری...</p></div></div>
<div class="footer"><a href="https://t.me/VaslZone" target="_blank">@VaslZone</a> · v9.3</div>
</div>
<script>
var API = "API_URL_PLACEHOLDER";
var allLinks = [];

function fmtB(b){if(!b||b===0)return'0 B';if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function esc(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function toFa(n){return String(n).replace(/\d/g,function(d){return'۰۱۲۳۴۵۶۷۸۹'[d]})}
function toast(m){var t=document.getElementById('toast');t.textContent=m;t.className='toast show';setTimeout(function(){t.classList.remove('show')},1800)}

async function loadData(){try{var r=await fetch(API);if(!r.ok)throw Error();return await r.json()}catch(e){return null}}

function render(d){
  if(!d||!d.links||!d.links.length){
    document.getElementById('root').innerHTML='<div style="text-align:center;padding:70px 20px;color:var(--text3)"><i class="ti ti-link-off" style="font-size:40px;display:block;margin-bottom:14px;opacity:.3"></i><p>کانفیگی یافت نشد</p></div>';return}
  allLinks=d.links;
  var active=d.links.filter(function(l){return l.active}).length;
  var totalUsed=d.links.reduce(function(s,l){return s+(l.used_bytes||0)},0);
  var h='';
  h+='<div class="card" style="text-align:center"><div style="font-size:16px;font-weight:800">'+esc(d.name||'VaslZone')+'</div>'+(d.desc?'<div style="font-size:11px;color:var(--text2);margin-top:4px">'+esc(d.desc)+'</div>':'')+'</div>';
  h+='<div class="stats"><div class="stat"><div class="sl">وضعیت</div><div class="sv">'+(d.links.length===1?(d.links[0].active?'فعال':'غیرفعال'):active+'/'+d.links.length)+'</div></div><div class="stat"><div class="sl">مصرف</div><div class="sv" style="font-size:17px">'+fmtB(totalUsed)+'</div></div><div class="stat"><div class="sl">اتصالات</div><div class="sv">'+(d.active_connections||0)+'</div></div></div>';
  if(d.links.length>1)h+='<div class="copy-all"><div class="copy-all-t"><div><i class="ti ti-copy"></i> کپی همه</div><span>یکبار کلیک</span></div><button class="copy-all-btn" onclick="copyAll()"><i class="ti ti-clipboard-copy"></i> کپی ('+active+')</button></div>';
  for(var i=0;i<d.links.length;i++){
    var l=d.links[i];
    var pct=l.limit_bytes>0?Math.min(100,(l.used_bytes/l.limit_bytes)*100):0;
    var remain=l.limit_bytes>0?Math.max(0,l.limit_bytes-l.used_bytes):-1;
    var rc=remain<0?'cr-ok':(remain<1048576?'cr-danger':(remain<1073741824?'cr-warn':'cr-ok'));
    var rf=remain<0?'∞':fmtB(remain);
    h+='<div class="cfg-card"><div class="cfg-head"><span class="cfg-label">'+esc(l.label)+'</span><span class="cfg-status '+(l.active?'cg-ok':'cg-off')+'">'+(l.active?'فعال':'غیرفعال')+'</span></div><div class="cfg-info"><span>مصرف: <b>'+l.used_fmt+'</b></span><span>سهمیه: <b>'+l.limit_fmt+'</b></span></div><div class="cfg-bar"><div class="cfg-bar-f" style="width:'+pct+'%"></div></div><span class="cfg-remain '+rc+'"><i class="ti ti-'+(remain<0?'infinity':'database')+'"></i> '+(remain<0?'∞':'باقی: '+rf)+'</span><div class="cfg-link" id="vl-'+i+'"><code>'+esc(l.vless_link||'')+'</code></div><div class="cfg-actions"><button class="btn btn-y" onclick="showVl('+i+')"><i class="ti ti-eye"></i> نمایش</button><button class="btn btn-y" onclick="cp(links['+i+'].vl)"><i class="ti ti-copy"></i> کپی</button><button class="btn btn-o btn-sm" onclick="qr(links['+i+'].vl)"><i class="ti ti-qrcode"></i></button></div></div>'
  }
  h+='<div class="speed-card"><div class="speed-head"><div class="speed-tt"><i class="ti ti-speedtest"></i> تست سرعت</div><button style="padding:6px 14px;border-radius:8px;border:1px solid var(--border);background:rgba(255,215,0,0.08);color:var(--yellow);font-family:inherit;font-size:10px;font-weight:700;cursor:pointer" onclick="speedTest()" id="spBtn">شروع</button></div><div class="speed-res" id="spRes">کلیک کنید</div></div>';
  h+='<div class="chart-card"><div class="chart-tt"><i class="ti ti-chart-bar"></i> نمودار مصرف</div><div class="chart-body"><canvas id="usageChart"></canvas></div><div class="chart-tabs" id="ctabs"><button class="chart-tab" data-r="10s" onclick="setRange(\'10s\',this)">۱۰ث</button><button class="chart-tab" data-r="10m" onclick="setRange(\'10m\',this)">۱۰د</button><button class="chart-tab a" data-r="1h" onclick="setRange(\'1h\',this)">۱س</button><button class="chart-tab" data-r="1d" onclick="setRange(\'1d\',this)">۱روز</button></div><div class="chart-tip" id="chartTip">نگهدار ۲ ثانیه = مقدار دقیق</div></div>';
  document.getElementById('root').innerHTML=h;
  window._links=d.links.map(function(l,i){return{vl:l.vless_link||''}});
  try{setTimeout(function(){try{initChart()}catch(e){}},300)}catch(e){}
}
function showVl(i){var e=document.getElementById('vl-'+i);if(e)e.classList.toggle('s')}
function cp(t){navigator.clipboard.writeText(t).then(function(){toast('✅ کپی شد')})}
function copyAll(){var t=allLinks.map(function(l){return l.vless_link||''}).filter(Boolean).join('\n');if(t)navigator.clipboard.writeText(t).then(function(){toast('✅ همه کپی شد')})}
function qr(u){if(u)window.open('https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(u),'_blank')}

async function speedTest(){var btn=document.getElementById('spBtn'),res=document.getElementById('spRes');btn.disabled=true;res.textContent='⏳...';try{var s=Date.now();var r=await fetch(API+'?_='+s);var d=await r.json();var ms=Date.now()-s;res.textContent=(ms<50?'🟢':ms<150?'🟡':'🔴')+' پینگ: '+ms+'ms'}catch(e){res.textContent='🔴 خطا'}btn.disabled=false}

var chart=null,range='1h';
function setRange(r,b){range=r;var a=document.querySelectorAll('.chart-tab');for(var i=0;i<a.length;i++)a[i].classList.remove('a');b.classList.add('a');updateChart()}
function initChart(){var c=document.getElementById('usageChart');if(!c||typeof Chart==='undefined')return;if(chart)chart.destroy();var v=[];for(var i=0;i<30;i++)v.push(Math.random()*80);chart=new Chart(c.getContext('2d'),{type:'line',data:{labels:new Array(30).fill(''),datasets:[{label:'MB',data:v,borderColor:'#ffd700',backgroundColor:'rgba(255,215,0,0.1)',fill:true,tension:.4,pointRadius:3,pointBackgroundColor:'#ffd700',borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(12,12,10,0.95)',titleColor:'#ffd700',bodyColor:'#bdb76b',padding:12,cornerRadius:8,displayColors:false,titleFont:{size:11},bodyFont:{size:11},callbacks:{label:function(ctx){return ctx.parsed.y.toFixed(2)+' MB'}}}},scales:{x:{grid:{display:false},ticks:{color:'#6b6b40',maxTicksLimit:6,font:{size:9}}},y:{grid:{color:'rgba(255,215,0,0.05)'},ticks:{color:'#6b6b40',font:{size:9},callback:function(v){return v.toFixed(0)}}}}}})}
function updateChart(){if(!chart)return;var v=[];var n={10:10,10:20,1:30,1:48}[{30000:10,600000:20,3600000:30,86400000:48}[1000]]||20;for(var i=0;i<n;i++)v.push(Math.random()*80);chart.data.labels=new Array(n).fill('');chart.data.datasets[0].data=v;chart.update()}

(async function(){var d=await loadData();if(d)render(d);else document.getElementById('root').innerHTML='<div style="text-align:center;padding:70px 20px;color:var(--text3)"><i class="ti ti-alert-circle" style="font-size:40px;color:var(--red);display:block;margin-bottom:14px"></i><p>خطا در بارگذاری</p></div>'})();
</script>
</body></html>"""
    return html.replace("API_URL_PLACEHOLDER", api_url)

def get_public_page_html(uuid_key: str) -> str:
    return get_sub_page_html(api_url=f"/api/public/sub/{uuid_key}", title="VaslZone Group")

def get_single_sub_page_html(uuid: str) -> str:
    return get_sub_page_html(api_url=f"/api/public/sub-single/{uuid}", title="VaslZone Config")
