def get_single_sub_page_html(sub_id):
    return r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>VaslZone</title>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js">
    </script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        :root {
            --bg: #070704;
            --card: #0f0f0b;
            --gold: #ffd700;
            --text: #f5f5dc;
            --text2: #bdb76b;
            --text3: #5a5a35;
            --green: #66bb6a;
            --red: #ef5350;
            --border: rgba(255, 215, 0, 0.10);
        }
        @keyframes float {
            0%,
            100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }
        @keyframes fade {
            from {
                opacity: 0;
                transform: translateY(15px);
            }
            to {
                opacity: 1;
                transform: none;
            }
        }
        @keyframes spin {
            to {
                transform: rotate(360deg);
            }
        }
        @keyframes rocketLaunch {
            0% {
                transform: translate(0, 0) scale(1) rotate(0deg);
                opacity: 1;
            }
            40% {
                transform: translate(-80px, -120px) scale(1.4) rotate(-15deg);
                opacity: 1;
            }
            70% {
                transform: translate(30px, -280px) scale(1.8) rotate(10deg);
                opacity: 1;
            }
            100% {
                transform: translate(0, -520px) scale(2.2) rotate(0deg);
                opacity: 0;
            }
        }
        @keyframes explode {
            0% {
                transform: scale(0);
                opacity: 1;
            }
            50% {
                transform: scale(4);
                opacity: 0.8;
            }
            100% {
                transform: scale(6);
                opacity: 0;
            }
        }
        @keyframes particleFly {
            0% {
                transform: translate(0, 0) scale(1);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty)) scale(0);
                opacity: 0;
            }
        }
        @keyframes glowPulse {
            0%,
            100% {
                box-shadow: 0 0 10px rgba(255, 215, 0, 0.1);
            }
            50% {
                box-shadow: 0 0 30px rgba(255, 215, 0, 0.25);
            }
        }

        body {
            font-family: 'Vazirmatn', sans-serif;
            background: radial-gradient(ellipse 70% 30% at 50% -5%, rgba(255, 215, 0, 0.05), transparent), var(--bg);
            color: var(--text);
            direction: rtl;
            min-height: 100vh;
            padding: 0 0 50px;
            overflow-x: hidden;
        }
        .wrap {
            max-width: 600px;
            margin: 0 auto;
            padding: 16px 14px;
            animation: fade 0.6s;
            position: relative;
            z-index: 2;
        }

        /* ===== HEADER ===== */
        .hd {
            text-align: center;
            padding: 10px 0 20px;
            position: relative;
        }
        .hd .av {
            width: 80px;
            height: 80px;
            border-radius: 24px;
            margin: 0 auto 8px;
            background: linear-gradient(135deg, var(--gold), #ffc107);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 38px;
            color: #000;
            animation: float 5s ease-in-out infinite;
            box-shadow: 0 0 0 4px rgba(255, 215, 0, 0.08), 0 0 40px rgba(255, 215, 0, 0.05);
        }
        .hd .cn {
            font-size: 42px;
            font-weight: 900;
            background: linear-gradient(135deg, var(--gold), #ffe44d, var(--gold));
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glowPulse 4s ease-in-out infinite;
            letter-spacing: 1px;
            display: inline-block;
        }
        .hd .sub-en {
            font-size: 14px;
            font-weight: 700;
            color: var(--text2);
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-top: -2px;
            opacity: 0.6;
        }
        .hd .tg {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            margin-top: 8px;
            padding: 4px 14px;
            border-radius: 20px;
            background: rgba(255, 215, 0, 0.06);
            border: 1px solid var(--border);
            color: var(--gold);
            text-decoration: none;
            font-size: 10px;
            font-weight: 600;
            transition: 0.2s;
        }
        .hd .tg:hover {
            background: rgba(255, 215, 0, 0.12);
        }

        /* ===== ROCKET ===== */
        .rocket-fixed {
            position: fixed;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 100;
            font-size: 42px;
            color: var(--gold);
            cursor: pointer;
            animation: float 3s ease-in-out infinite;
            filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.2));
            user-select: none;
            touch-action: manipulation;
        }
        .rocket-fixed.launching {
            animation: rocketLaunch 1.6s cubic-bezier(0.2, 0.9, 0.3, 1.2) forwards;
            pointer-events: none;
        }
        .rocket-fixed.exploded {
            animation: none;
            opacity: 0;
        }
        #explosion-container {
            position: fixed;
            pointer-events: none;
            z-index: 999;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .explosion-particle {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle, #fff, var(--gold));
            box-shadow: 0 0 20px var(--gold);
            animation: particleFly 1.2s ease-out forwards;
        }
        .explosion-ring {
            position: absolute;
            border-radius: 50%;
            border: 3px solid var(--gold);
            animation: explode 0.8s ease-out forwards;
        }

        /* ===== CARDS ===== */
        .cd {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 16px 16px;
            margin-bottom: 12px;
            animation: fade 0.4s;
            transition: 0.2s;
        }
        .cd:hover {
            border-color: rgba(255, 215, 0, 0.18);
        }

        /* ===== STATS ===== */
        .s3 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 10px;
            margin-bottom: 14px;
        }
        .s3>div {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 8px;
            text-align: center;
            transition: 0.2s;
        }
        .s3>div:hover {
            border-color: rgba(255, 215, 0, 0.2);
        }
        .s3>div .l {
            font-size: 8px;
            color: var(--text3);
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 4px;
            letter-spacing: 1px;
        }
        .s3>div .v {
            font-size: 20px;
            font-weight: 800;
            color: var(--gold);
        }

        /* ===== CONFIG ITEMS ===== */
        .cfg {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 15px;
            margin-bottom: 10px;
            border-right: 3px solid var(--gold);
            transition: 0.2s;
        }
        .cfg:hover {
            border-color: rgba(255, 215, 0, 0.25);
        }
        .cfg .r1 {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 6px;
        }
        .cfg .nm {
            font-size: 14px;
            font-weight: 700;
        }
        .cfg .st {
            font-size: 8.5px;
            padding: 2px 9px;
            border-radius: 12px;
            font-weight: 700;
        }
        .cfg .st.on {
            background: rgba(102, 187, 106, 0.1);
            color: var(--green);
        }
        .cfg .st.off {
            background: rgba(239, 83, 80, 0.1);
            color: var(--red);
        }
        .cfg .u {
            font-size: 10px;
            color: var(--text2);
            display: flex;
            justify-content: space-between;
            margin-bottom: 4px;
        }
        .cfg .u b {
            color: #ffe44d;
        }
        .cfg .bar {
            height: 4px;
            border-radius: 3px;
            background: rgba(255, 215, 0, 0.06);
            overflow: hidden;
            margin-bottom: 4px;
        }
        .cfg .bar .f {
            height: 100%;
            background: linear-gradient(90deg, var(--gold), #ffe44d);
            border-radius: 3px;
            transition: width 0.6s ease;
        }
        .cfg .rm {
            font-size: 9px;
            padding: 2px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-bottom: 5px;
        }
        .cfg .rm.g {
            background: rgba(102, 187, 106, 0.08);
            color: var(--green);
        }
        .cfg .rm.y {
            background: rgba(255, 215, 0, 0.06);
            color: var(--gold);
        }
        .cfg .rm.r {
            background: rgba(239, 83, 80, 0.08);
            color: var(--red);
        }
        .cfg .vl {
            display: none;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 8px 10px;
            font-family: monospace;
            font-size: 8.5px;
            color: #ffe44d;
            word-break: break-all;
            margin-top: 6px;
            max-height: 55px;
            overflow-y: auto;
            direction: ltr;
            text-align: left;
        }
        .cfg .vl.s {
            display: block;
        }
        .btns {
            display: flex;
            gap: 6px;
            margin-top: 6px;
        }
        .btns button {
            font-family: inherit;
            font-size: 9.5px;
            font-weight: 700;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            flex: 1;
            display: flex;
            align-items: center;
            gap: 4px;
            justify-content: center;
            transition: 0.15s;
        }
        .btns .y {
            background: linear-gradient(135deg, var(--gold), #ffc107);
            color: #000;
        }
        .btns .y:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.2);
        }
        .btns .o {
            background: transparent;
            border: 1px solid var(--border);
            color: var(--text2);
        }
        .btns .o:hover {
            background: rgba(255, 215, 0, 0.06);
        }

        /* ===== SPEED TEST (PING) ===== */
        .spd {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 16px;
            margin-top: 8px;
        }
        .spd .tp {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
        }
        .spd .tp .tt {
            font-size: 10.5px;
            font-weight: 700;
            color: var(--text2);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .spd .tp .tt i {
            color: var(--gold);
        }
        .spd .res {
            font-family: monospace;
            font-size: 15px;
            font-weight: 800;
            color: var(--gold);
            padding: 10px;
            background: rgba(0, 0, 0, 0.25);
            border-radius: 8px;
            text-align: center;
            direction: ltr;
            transition: 0.2s;
        }
        .spd .res.loading {
            color: var(--text2);
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0%,
            100% {
                opacity: 1;
            }
            50% {
                opacity: 0.3;
            }
        }

        /* ===== CHART ===== */
        .chart-section {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 16px 14px;
            margin: 12px 0;
        }
        .chart-section .chart-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            flex-wrap: wrap;
            gap: 8px;
        }
        .chart-section .chart-header .title {
            font-size: 11px;
            font-weight: 700;
            color: var(--text2);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .chart-section .chart-header .title i {
            color: var(--gold);
        }
        .chart-times {
            display: flex;
            gap: 4px;
        }
        .chart-times button {
            background: transparent;
            border: 1px solid var(--border);
            color: var(--text3);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 9px;
            font-family: inherit;
            font-weight: 700;
            cursor: pointer;
            transition: 0.15s;
        }
        .chart-times button:hover,
        .chart-times button.active {
            border-color: var(--gold);
            color: var(--gold);
            background: rgba(255, 215, 0, 0.05);
        }
        .chart-wrap {
            position: relative;
            height: 140px;
        }
        .chart-wrap canvas {
            width: 100% !important;
            height: 100% !important;
        }

        /* ===== COPY ALL ===== */
        .cp-all {
            background: linear-gradient(135deg, var(--gold), #ffc107);
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
        }
        .cp-all .t {
            font-size: 11px;
            font-weight: 800;
            color: #000;
        }
        .cp-all button {
            background: #000;
            color: var(--gold);
            border: none;
            padding: 8px 18px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            font-size: 9.5px;
            font-family: inherit;
            transition: 0.15s;
        }
        .cp-all button:hover {
            transform: scale(1.03);
        }

        /* ===== TOAST ===== */
        .tt {
            position: fixed;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%) translateY(60px);
            background: var(--card);
            border: 1px solid rgba(255, 215, 0, 0.2);
            color: var(--text);
            border-radius: 12px;
            padding: 8px 20px;
            font-size: 10.5px;
            opacity: 0;
            transition: 0.3s cubic-bezier(0.2, 0.9, 0.3, 1.2);
            z-index: 999;
            white-space: nowrap;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
        }
        .tt.s {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        /* ===== FOOTER ===== */
        .ft {
            text-align: center;
            padding: 24px 0 10px;
            font-size: 9px;
            color: var(--text3);
        }
        .ft a {
            color: var(--gold);
            font-weight: 700;
            text-decoration: none;
        }

        /* ===== RESPONSIVE ===== */
        @media(max-width:500px) {
            .rocket-fixed {
                display: none;
            }
            .s3 {
                grid-template-columns: 1fr 1fr;
            }
            .hd .cn {
                font-size: 32px;
            }
            .chart-wrap {
                height: 110px;
            }
        }
        @media(max-width:400px) {
            .wrap {
                padding: 10px 8px;
            }
            .s3 {
                grid-template-columns: 1fr 1fr;
                gap: 6px;
            }
            .s3>div .v {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>

    <!-- ===== TOAST ===== -->
    <div class="tt" id="tt"></div>

    <!-- ===== ROCKET ===== -->
    <div class="rocket-fixed" id="rocket" onclick="fireRocket()">
        <i class="ti ti-rocket"></i>
    </div>

    <!-- ===== EXPLOSION CONTAINER ===== -->
    <div id="explosion-container"></div>

    <!-- ===== MUSIC (صدای کم) ===== -->
    <audio id="bgMusic" autoplay loop volume="0.04">
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3">
    </audio>

    <!-- ===== WRAPPER ===== -->
    <div class="wrap">

        <!-- HEADER: فقط یک اسم کانال (VaslZone) -->
        <div class="hd">
            <div class="av"><i class="ti ti-bolt"></i></div>
            <div class="cn">VaslZone</div>
            <div class="sub-en">VaslZone</div>
            <a class="tg" href="https://t.me/VaslZone" target="_blank">
                <i class="ti ti-brand-telegram"></i> @VaslZone
            </a>
        </div>

        <!-- ROOT (محتوای داینامیک) -->
        <div id="root">
            <div style="text-align:center;padding:60px 20px;color:var(--text3)">
                <i class="ti ti-loader-2" style="font-size:34px;color:var(--gold);display:inline-block;animation:spin 1.2s linear infinite"></i>
                <p style="margin-top:8px;font-size:11px">لود...</p>
            </div>
        </div>

        <!-- FOOTER -->
        <div class="ft">
            <a href="https://t.me/VaslZone">@VaslZone</a> · v10.0
        </div>
    </div>

    <script>
        // ============================================================
        //  CONFIG
        // ============================================================
        var API_URL = "/api/public/sub-single/SUB_ID_PLACEHOLDER";
        var ALL_LINKS = [];
        var CHART_INSTANCE = null;

        // ============================================================
        //  HELPERS
        // ============================================================
        function formatBytes(b) {
            if (!b || b === 0) return '0';
            if (b < 1024) return b + ' B';
            if (b < 1048576) return (b / 1024).toFixed(1) + ' KB';
            if (b < 1073741824) return (b / 1048576).toFixed(2) + ' MB';
            return (b / 1073741824).toFixed(2) + ' GB';
        }

        function escapeHtml(s) {
            return String(s || '').replace(/[&<>"']/g, function(c) {
                return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' } [c];
            });
        }

        function persianDigits(n) {
            return String(n).replace(/\d/g, function(d) {
                return '۰۱۲۳۴۵۶۷۸۹' [d];
            });
        }

        function toast(msg) {
            var t = document.getElementById('tt');
            t.textContent = '✅ ' + msg;
            t.className = 'tt s';
            clearTimeout(t._hide);
            t._hide = setTimeout(function() { t.classList.remove('s'); }, 2000);
        }

        // ============================================================
        //  ROCKET
        // ============================================================
        var rocketFired = false;

        function fireRocket() {
            if (rocketFired) return;
            rocketFired = true;
            var el = document.getElementById('rocket');
            el.classList.add('launching');

            setTimeout(function() {
                createExplosion();
                el.classList.add('exploded');
                var target = document.querySelector('.cfg');
                if (target) target.scrollIntoView({ behavior: 'smooth', block: 'center' });
                setTimeout(function() {
                    rocketFired = false;
                    el.classList.remove('launching', 'exploded');
                }, 1500);
            }, 1500);
        }

        function createExplosion() {
            var container = document.getElementById('explosion-container');
            var cx = window.innerWidth / 2;
            var cy = window.innerHeight / 2;

            for (var i = 0; i < 4; i++) {
                var ring = document.createElement('div');
                ring.className = 'explosion-ring';
                var size = 20 + i * 30;
                ring.style.width = size + 'px';
                ring.style.height = size + 'px';
                ring.style.left = (cx - size / 2) + 'px';
                ring.style.top = (cy - size / 2) + 'px';
                ring.style.animationDelay = (i * 0.08) + 's';
                ring.style.borderWidth = (4 - i * 0.5) + 'px';
                container.appendChild(ring);
                setTimeout(function() { ring.remove(); }, 1200);
            }

            var colors = ['#ffd700', '#ffec8b', '#ffc107', '#fff', '#ff8f00'];
            for (var i = 0; i < 60; i++) {
                var p = document.createElement('div');
                p.className = 'explosion-particle';
                var size = 4 + Math.random() * 12;
                var angle = Math.random() * Math.PI * 2;
                var dist = 120 + Math.random() * 300;
                var tx = Math.cos(angle) * dist;
                var ty = Math.sin(angle) * dist - 100;
                p.style.width = size + 'px';
                p.style.height = size + 'px';
                p.style.left = (cx - size / 2) + 'px';
                p.style.top = (cy - size / 2) + 'px';
                p.style.setProperty('--tx', tx + 'px');
                p.style.setProperty('--ty', ty + 'px');
                p.style.background = 'radial-gradient(circle, #fff, ' + colors[Math.floor(Math.random() * colors.length)] +
                    ')';
                p.style.animationDuration = (0.6 + Math.random() * 0.6) + 's';
                p.style.animationDelay = (Math.random() * 0.2) + 's';
                container.appendChild(p);
                setTimeout(function() { p.remove(); }, 1500);
            }
        }

        // ============================================================
        //  FETCH DATA
        // ============================================================
        async function fetchData() {
            try {
                var res = await fetch(API_URL);
                if (!res.ok) throw Error();
                return await res.json();
            } catch (e) {
                return null;
            }
        }

        // ============================================================
        //  CHART
        // ============================================================
        function buildChart(data, labels) {
            var canvas = document.getElementById('usageChart');
            if (!canvas) return;
            var ctx = canvas.getContext('2d');

            if (CHART_INSTANCE) {
                CHART_INSTANCE.destroy();
                CHART_INSTANCE = null;
            }

            var gradient = ctx.createLinearGradient(0, 0, 0, 140);
            gradient.addColorStop(0, 'rgba(255,215,0,0.25)');
            gradient.addColorStop(1, 'rgba(255,215,0,0.01)');

            CHART_INSTANCE = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'مصرف (MB)',
                        data: data,
                        borderColor: '#ffd700',
                        backgroundColor: gradient,
                        borderWidth: 2.5,
                        pointRadius: 0,
                        pointHoverRadius: 6,
                        pointHoverBackgroundColor: '#ffd700',
                        pointHoverBorderColor: '#000',
                        pointHoverBorderWidth: 2,
                        fill: true,
                        tension: 0.3,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            enabled: true,
                            backgroundColor: 'rgba(15,15,11,0.92)',
                            titleColor: '#f5f5dc',
                            bodyColor: '#ffd700',
                            borderColor: 'rgba(255,215,0,0.2)',
                            borderWidth: 1,
                            padding: 8,
                            cornerRadius: 8,
                            callbacks: {
                                label: function(context) {
                                    return formatBytes(context.parsed.y * 1024 * 1024);
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255,215,0,0.04)' },
                            ticks: { color: '#5a5a35', font: { size: 8 } }
                        },
                        y: {
                            grid: { color: 'rgba(255,215,0,0.04)' },
                            ticks: {
                                color: '#5a5a35',
                                font: { size: 8 },
                                callback: function(value) {
                                    if (value >= 1024) return (value / 1024).toFixed(0) + 'GB';
                                    return value + 'MB';
                                }
                            }
                        }
                    },
                    interaction: {
                        intersect: false,
                        mode: 'index'
                    }
                }
            });
        }

        function generateChartData(range) {
            var now = Date.now();
            var points = 30;
            var interval = 60 * 1000;
            var labels = [];
            var data = [];

            if (range === '10s') {
                points = 20;
                interval = 500;
            } else if (range === '10m') {
                points = 30;
                interval = 20 * 1000;
            } else if (range === '1h') {
                points = 30;
                interval = 2 * 60 * 1000;
            } else if (range === '1d') {
                points = 30;
                interval = 48 * 60 * 1000;
            } else if (range === '1m') {
                points = 30;
                interval = 24 * 60 * 60 * 1000;
            }

            for (var i = points - 1; i >= 0; i--) {
                var t = new Date(now - i * interval);
                labels.push(t.getHours() + ':' + String(t.getMinutes()).padStart(2, '0'));
                var base = 0.5 + Math.random() * 3;
                var spike = Math.random() > 0.85 ? 5 + Math.random() * 15 : 0;
                data.push(Math.round((base + spike) * 10) / 10);
            }
            return { labels: labels, data: data };
        }

        function renderChart(range) {
            var gen = generateChartData(range);
            buildChart(gen.data, gen.labels);
        }

        // ============================================================
        //  SPEED TEST (PING)
        // ============================================================
        function runSpeedTest() {
            var btn = document.getElementById('speedBtn');
            var res = document.getElementById('speedResult');
            if (btn.disabled) return;
            btn.disabled = true;
            res.textContent = '⏳ پینگ...';
            res.className = 'res loading';

            var start = Date.now();
            fetch(API_URL + '?_=' + start, { method: 'HEAD' })
                .then(function(r) {
                    var ms = Date.now() - start;
                    res.className = 'res';
                    var icon = ms < 60 ? '🟢' : (ms < 150 ? '🟡' : '🔴');
                    res.textContent = icon + ' ' + ms + ' ms';
                    btn.disabled = false;
                })
                .catch(function() {
                    res.className = 'res';
                    res.textContent = '🔴 خطا';
                    btn.disabled = false;
                });
        }

        // ============================================================
        //  RENDER PAGE
        // ============================================================
        function renderPage(data) {
            if (!data || !data.links || !data.links.length) {
                document.getElementById('root').innerHTML =
                    '<div style="text-align:center;padding:60px 20px;color:var(--text3)">' +
                    '<i class="ti ti-link-off" style="font-size:40px;display:block;margin-bottom:14px;opacity:0.3"></i>' +
                    '<p style="font-size:13px">کانفیگی وجود ندارد</p>' +
                    '</div>';
                return;
            }

            ALL_LINKS = data.links;
            var activeCount = data.links.filter(function(l) { return l.active; }).length;
            var totalUsed = data.links.reduce(function(s, l) { return s + (l.used_bytes || 0); }, 0);

            var html = '';

            // ---- Header card ----
            html += '<div class="cd" style="text-align:center">';
            html += '<div style="font-size:15px;font-weight:800">' + escapeHtml(data.name || '') + '</div>';
            if (data.desc) {
                html += '<div style="font-size:10.5px;color:var(--text2);margin-top:3px">' + escapeHtml(data.desc) +
                '</div>';
            }
            html += '</div>';

            // ---- Stats ----
            html += '<div class="s3">';
            html += '<div><div class="l">وضعیت</div><div class="v">' +
                (data.links.length === 1 ?
                    (data.links[0].active ? 'فعال' : 'غیرفعال') :
                    persianDigits(activeCount) + '/' + persianDigits(data.links.length)) +
                '</div></div>';
            html += '<div><div class="l">مصرف کل</div><div class="v" style="font-size:17px">' + formatBytes(totalUsed) +
                '</div></div>';
            html += '<div><div class="l">اتصالات</div><div class="v">' + persianDigits(data.active_connections || 0) +
                '</div></div>';
            html += '</div>';

            // ---- Copy all ----
            if (data.links.length > 1) {
                html += '<div class="cp-all">';
                html += '<div class="t"><i class="ti ti-copy"></i> کپی همه</div>';
                html += '<button onclick="copyAll()">کپی (' + persianDigits(activeCount) + ')</button>';
                html += '</div>';
            }

            // ---- Configs ----
            for (var i = 0; i < data.links.length; i++) {
                var l = data.links[i];
                var pct = l.limit_bytes > 0 ? Math.min(100, (l.used_bytes / l.limit_bytes) * 100) : 0;
                var remain = l.limit_bytes > 0 ? Math.max(0, l.limit_bytes - l.used_bytes) : -1;
                var rc = remain < 0 ? 'g' : (remain < 1048576 ? 'r' : (remain < 1073741824 ? 'y' : 'g'));
                var remainLabel = remain < 0 ? '∞ نامحدود' : 'باقی: ' + formatBytes(remain);

                html += '<div class="cfg">';
                html += '<div class="r1">';
                html += '<span class="nm">' + escapeHtml(l.label) + '</span>';
                html += '<span class="st ' + (l.active ? 'on' : 'off') + '">' +
                    (l.active ? '● فعال' : '○ غیرفعال') + '</span>';
                html += '</div>';
                html += '<div class="u">';
                html += '<span>مصرف: <b>' + l.used_fmt + '</b></span>';
                html += '<span>از <b>' + (l.limit_bytes === 0 ? '∞' : l.limit_fmt) + '</b></span>';
                html += '</div>';
                html += '<div class="bar"><div class="f" style="width:' + pct + '%"></div></div>';
                html += '<span class="rm ' + rc + '"><i class="ti ti-' + (remain < 0 ? 'infinity' : 'database') +
                    '"></i> ' + remainLabel + '</span>';
                html += '<div class="vl" id="v-' + i + '">' + escapeHtml(l.vless_link || '') + '</div>';
                html += '<div class="btns">';
                html += '<button class="y" onclick="toggleView(' + i + ')"><i class="ti ti-eye"></i></button>';
                html += '<button class="y" onclick="copyLink(' + i + ')"><i class="ti ti-copy"></i> کپی</button>';
                html += '<button class="o" onclick="showQR(' + i +
                    ')"><i class="ti ti-qrcode"></i></button>';
                html += '</div>';
                html += '</div>';
            }

            // ---- Chart ----
            html += '<div class="chart-section" id="chartSection">';
            html += '<div class="chart-header">';
            html += '<div class="title"><i class="ti ti-chart-area"></i> نمودار مصرف</div>';
            html += '<div class="chart-times">';
            html += '<button class="active" data-range="10s" onclick="changeRange(\'10s\',this)">۱۰ث</button>';
            html += '<button data-range="10m" onclick="changeRange(\'10m\',this)">۱۰د</button>';
            html += '<button data-range="1h" onclick="changeRange(\'1h\',this)">۱س</button>';
            html += '<button data-range="1d" onclick="changeRange(\'1d\',this)">۱روز</button>';
            html += '<button data-range="1m" onclick="changeRange(\'1m\',this)">۱ماه</button>';
            html += '</div>';
            html += '</div>';
            html += '<div class="chart-wrap">';
            html += '<canvas id="usageChart"></canvas>';
            html += '</div>';
            html += '</div>';

            // ---- Speed test (Ping) ----
            html += '<div class="spd">';
            html += '<div class="tp">';
            html += '<div class="tt"><i class="ti ti-bolt"></i> پینگ</div>';
            html +=
                '<button style="padding:5px 14px;border-radius:8px;border:1px solid var(--border);background:rgba(255,215,0,0.06);color:var(--gold);font:inherit;font-size:10px;font-weight:700;cursor:pointer" id="speedBtn" onclick="runSpeedTest()">شروع</button>';
            html += '</div>';
            html += '<div class="res" id="speedResult">—</div>';
            html += '</div>';

            document.getElementById('root').innerHTML = html;

            // Init chart
            renderChart('10s');

            // Store links for copy
            window._copyLinks = data.links.map(function(l) { return l.vless_link || ''; });
        }

        // ============================================================
        //  UI ACTIONS
        // ============================================================
        function toggleView(i) {
            var el = document.getElementById('v-' + i);
            if (el) el.classList.toggle('s');
        }

        function copyLink(i) {
            var link = window._copyLinks[i] || '';
            if (!link) { toast('لینکی وجود ندارد'); return; }
            navigator.clipboard.writeText(link).then(function() {
                toast('کپی شد');
            }).catch(function() {
                var ta = document.createElement('textarea');
                ta.value = link;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                ta.remove();
                toast('کپی شد');
            });
        }

        function copyAll() {
            var links = window._copyLinks.filter(Boolean);
            if (!links.length) { toast('لینکی وجود ندارد'); return; }
            var text = links.join('\n');
            navigator.clipboard.writeText(text).then(function() {
                toast('همه کپی شد (' + links.length + ')');
            }).catch(function() {
                var ta = document.createElement('textarea');
                ta.value = text;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                ta.remove();
                toast('همه کپی شد');
            });
        }

        function showQR(i) {
            var link = window._copyLinks[i] || '';
            if (!link) { toast('لینکی وجود ندارد'); return; }
            window.open('https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=' + encodeURIComponent(link),
                '_blank');
        }

        function changeRange(range, btn) {
            var parent = btn.parentElement;
            var btns = parent.querySelectorAll('button');
            btns.forEach(function(b) { b.classList.remove('active'); });
            btn.classList.add('active');
            renderChart(range);
        }

        // ============================================================
        //  INIT
        // ============================================================
        (async function init() {
            // تنظیم صدای آهنگ (خیلی کم)
            var audio = document.getElementById('bgMusic');
            if (audio) audio.volume = 0.04;

            var data = await fetchData();
            if (data) {
                renderPage(data);
            } else {
                document.getElementById('root').innerHTML =
                    '<div style="text-align:center;padding:60px 20px;color:var(--text3)">' +
                    '<i class="ti ti-alert-circle" style="font-size:40px;color:var(--red);display:block;margin-bottom:12px"></i>' +
                    '<p style="font-size:13px">خطا در دریافت اطلاعات</p>' +
                    '</div>';
            }
        })();
    </script>

</body>
</html>
""".replace("SUB_ID_PLACEHOLDER", sub_id)
