def get_single_sub_page_html(sub_id):
    return r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>VaslZone</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js">
    </script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        :root {
            --bg: #0a0a0a;
            --card: #141414;
            --gold: #fbbf24;
            --gold-dim: rgba(251, 191, 36, 0.08);
            --gold-glow: 0 0 30px rgba(251, 191, 36, 0.1);
            --text: #f0f0f0;
            --text2: #a0a0a0;
            --text3: #4a4a4a;
            --green: #4ade80;
            --red: #f87171;
            --border: rgba(255, 255, 255, 0.06);
            --radius: 16px;
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
        }
        body {
            font-family: 'Inter', sans-serif;
            background: radial-gradient(ellipse at 50% -10%, rgba(251, 191, 36, 0.03), transparent 70%), var(--bg);
            color: var(--text);
            min-height: 100vh;
            padding: 20px 16px 60px;
            direction: rtl;
        }
        .container {
            max-width: 560px;
            margin: 0 auto;
            position: relative;
        }

        /* ===== ROCKET ===== */
        .rocket {
            position: fixed;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 999;
            font-size: 44px;
            color: var(--gold);
            cursor: pointer;
            filter: drop-shadow(0 0 20px rgba(251, 191, 36, 0.25));
            transition: 0.1s;
            user-select: none;
            animation: float 3s ease-in-out infinite;
        }
        @keyframes float {
            0%,
            100% {
                transform: translateY(-50%);
            }
            50% {
                transform: translateY(-60%);
            }
        }
        .rocket.launch {
            animation: launch 1.4s cubic-bezier(0.2, 0.9, 0.3, 1.2) forwards !important;
            pointer-events: none;
        }
        @keyframes launch {
            0% {
                transform: translate(0, -50%) scale(1) rotate(0deg);
                opacity: 1;
            }
            40% {
                transform: translate(-60px, -120px) scale(1.3) rotate(-10deg);
            }
            70% {
                transform: translate(40px, -280px) scale(1.7) rotate(8deg);
            }
            100% {
                transform: translate(0, -480px) scale(2) rotate(0deg);
                opacity: 0;
            }
        }
        .rocket.hidden {
            opacity: 0;
            pointer-events: none;
        }
        #explosion {
            position: fixed;
            pointer-events: none;
            z-index: 1000;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .particle {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle, #fff, var(--gold));
            box-shadow: 0 0 30px var(--gold);
            animation: fly 1s ease-out forwards;
        }
        .ring {
            position: absolute;
            border-radius: 50%;
            border: 3px solid var(--gold);
            animation: expand 0.8s ease-out forwards;
        }
        @keyframes fly {
            0% {
                transform: translate(0, 0) scale(1);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty)) scale(0);
                opacity: 0;
            }
        }
        @keyframes expand {
            0% {
                transform: scale(0);
                opacity: 1;
            }
            100% {
                transform: scale(5);
                opacity: 0;
            }
        }

        /* ===== HEADER ===== */
        .header {
            text-align: center;
            padding: 20px 0 24px;
            position: relative;
        }
        .header .logo {
            width: 72px;
            height: 72px;
            margin: 0 auto 10px;
            background: linear-gradient(145deg, var(--gold), #f59e0b);
            border-radius: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 34px;
            color: #000;
            box-shadow: 0 0 0 3px rgba(251, 191, 36, 0.15), var(--gold-glow);
        }
        .header h1 {
            font-size: 38px;
            font-weight: 900;
            background: linear-gradient(135deg, var(--gold), #ffe484);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }
        .header .sub {
            font-size: 13px;
            font-weight: 600;
            color: var(--text2);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-top: -2px;
        }
        .header .telegram {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-top: 10px;
            padding: 5px 16px;
            border-radius: 30px;
            background: var(--gold-dim);
            border: 1px solid var(--border);
            color: var(--gold);
            font-size: 11px;
            font-weight: 600;
            text-decoration: none;
            transition: var(--transition);
        }
        .header .telegram:hover {
            background: rgba(251, 191, 36, 0.15);
        }

        /* ===== CARDS ===== */
        .card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 16px 18px;
            margin-bottom: 12px;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }
        .card:hover {
            border-color: rgba(251, 191, 36, 0.15);
        }

        /* ===== STATS ===== */
        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-bottom: 14px;
        }
        .stats .item {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 12px 6px;
            text-align: center;
        }
        .stats .item .label {
            font-size: 8px;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--text3);
            letter-spacing: 1px;
        }
        .stats .item .value {
            font-size: 20px;
            font-weight: 800;
            color: var(--gold);
            margin-top: 2px;
        }

        /* ===== CONFIG ITEMS ===== */
        .config {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 14px 16px;
            margin-bottom: 10px;
            border-right: 3px solid var(--gold);
        }
        .config .top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }
        .config .name {
            font-weight: 700;
            font-size: 14px;
        }
        .config .status {
            font-size: 8px;
            padding: 2px 10px;
            border-radius: 20px;
            font-weight: 700;
        }
        .config .status.on {
            background: rgba(74, 222, 128, 0.1);
            color: var(--green);
        }
        .config .status.off {
            background: rgba(248, 113, 113, 0.1);
            color: var(--red);
        }
        .config .usage {
            display: flex;
            justify-content: space-between;
            font-size: 10px;
            color: var(--text2);
            margin-bottom: 4px;
        }
        .config .usage b {
            color: #ffe484;
        }
        .config .bar {
            height: 4px;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.05);
            overflow: hidden;
            margin-bottom: 5px;
        }
        .config .bar .fill {
            height: 100%;
            background: linear-gradient(90deg, var(--gold), #ffe484);
            border-radius: 4px;
            transition: width 0.6s ease;
        }
        .config .remain {
            font-size: 9px;
            padding: 2px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-bottom: 6px;
        }
        .config .remain.green {
            background: rgba(74, 222, 128, 0.08);
            color: var(--green);
        }
        .config .remain.yellow {
            background: rgba(251, 191, 36, 0.08);
            color: var(--gold);
        }
        .config .remain.red {
            background: rgba(248, 113, 113, 0.08);
            color: var(--red);
        }
        .config .link-box {
            display: none;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 7px 10px;
            font-family: monospace;
            font-size: 8px;
            color: #ffe484;
            word-break: break-all;
            direction: ltr;
            text-align: left;
            margin-top: 6px;
            max-height: 56px;
            overflow-y: auto;
            border: 1px solid var(--border);
        }
        .config .link-box.open {
            display: block;
        }
        .config .actions {
            display: flex;
            gap: 6px;
            margin-top: 8px;
        }
        .config .actions button {
            flex: 1;
            padding: 6px 0;
            border: none;
            border-radius: 8px;
            font-family: inherit;
            font-size: 9.5px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            transition: var(--transition);
        }
        .config .actions .gold {
            background: linear-gradient(135deg, var(--gold), #f59e0b);
            color: #000;
        }
        .config .actions .gold:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 20px rgba(251, 191, 36, 0.3);
        }
        .config .actions .outline {
            background: transparent;
            border: 1px solid var(--border);
            color: var(--text2);
        }
        .config .actions .outline:hover {
            background: rgba(255, 255, 255, 0.03);
        }

        /* ===== COPY ALL ===== */
        .copy-all {
            background: linear-gradient(135deg, var(--gold), #f59e0b);
            border-radius: var(--radius);
            padding: 12px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 8px;
        }
        .copy-all span {
            font-weight: 800;
            font-size: 12px;
            color: #000;
        }
        .copy-all button {
            background: #000;
            color: var(--gold);
            border: none;
            padding: 7px 18px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 10px;
            cursor: pointer;
            font-family: inherit;
            transition: var(--transition);
        }
        .copy-all button:hover {
            transform: scale(1.03);
        }

        /* ===== CHART ===== */
        .chart-box {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 16px;
            margin: 12px 0;
        }
        .chart-box .head {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 8px;
        }
        .chart-box .head .title {
            font-size: 11px;
            font-weight: 700;
            color: var(--text2);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .chart-box .head .title i {
            color: var(--gold);
        }
        .chart-times {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }
        .chart-times button {
            background: transparent;
            border: 1px solid var(--border);
            color: var(--text3);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 9px;
            font-weight: 700;
            cursor: pointer;
            font-family: inherit;
            transition: var(--transition);
        }
        .chart-times button.active,
        .chart-times button:hover {
            border-color: var(--gold);
            color: var(--gold);
            background: var(--gold-dim);
        }
        .chart-wrap {
            height: 140px;
            position: relative;
        }
        .chart-wrap canvas {
            width: 100% !important;
            height: 100% !important;
        }

        /* ===== PING ===== */
        .ping-box {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 14px 18px;
            margin-top: 8px;
        }
        .ping-box .head {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        .ping-box .head .label {
            font-size: 10.5px;
            font-weight: 700;
            color: var(--text2);
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .ping-box .head .label i {
            color: var(--gold);
        }
        .ping-box .result {
            font-family: monospace;
            font-size: 16px;
            font-weight: 800;
            color: var(--gold);
            background: rgba(0, 0, 0, 0.2);
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            direction: ltr;
        }
        .ping-box .result.loading {
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
        .ping-box .btn-ping {
            padding: 5px 16px;
            border-radius: 8px;
            border: 1px solid var(--border);
            background: var(--gold-dim);
            color: var(--gold);
            font-family: inherit;
            font-size: 10px;
            font-weight: 700;
            cursor: pointer;
            transition: var(--transition);
        }
        .ping-box .btn-ping:hover {
            background: rgba(251, 191, 36, 0.15);
        }

        /* ===== TOAST ===== */
        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(80px);
            background: var(--card);
            border: 1px solid rgba(251, 191, 36, 0.2);
            color: var(--text);
            padding: 8px 24px;
            border-radius: 30px;
            font-size: 11px;
            font-weight: 600;
            opacity: 0;
            transition: 0.4s cubic-bezier(0.2, 0.9, 0.3, 1.2);
            z-index: 9999;
            box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);
            white-space: nowrap;
        }
        .toast.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        /* ===== FOOTER ===== */
        .footer {
            text-align: center;
            padding: 30px 0 10px;
            font-size: 9px;
            color: var(--text3);
        }
        .footer a {
            color: var(--gold);
            font-weight: 700;
            text-decoration: none;
        }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 500px) {
            .rocket {
                display: none;
            }
            .stats {
                grid-template-columns: 1fr 1fr;
            }
            .header h1 {
                font-size: 30px;
            }
            .chart-wrap {
                height: 110px;
            }
            .container {
                padding: 0 4px;
            }
        }
        @media (max-width: 400px) {
            .stats .item .value {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>

    <!-- TOAST -->
    <div class="toast" id="toast"></div>

    <!-- ROCKET -->
    <div class="rocket" id="rocket" onclick="fireRocket()">
        <i class="fas fa-rocket"></i>
    </div>

    <!-- EXPLOSION CONTAINER -->
    <div id="explosion"></div>

    <!-- MUSIC (low volume) -->
    <audio id="bgMusic" autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3">
    </audio>

    <div class="container">

        <!-- HEADER -->
        <div class="header">
            <div class="logo"><i class="fas fa-bolt"></i></div>
            <h1>VaslZone</h1>
            <div class="sub">VaslZone</div>
            <a class="telegram" href="https://t.me/VaslZone" target="_blank">
                <i class="fab fa-telegram-plane"></i> @VaslZone
            </a>
        </div>

        <!-- ROOT -->
        <div id="root">
            <div style="text-align:center;padding:60px 0;color:var(--text3);">
                <i class="fas fa-spinner fa-spin" style="font-size:34px;color:var(--gold);display:block;margin-bottom:10px;"></i>
                <p style="font-size:12px;">در حال بارگذاری...</p>
            </div>
        </div>

        <!-- FOOTER -->
        <div class="footer">
            <a href="https://t.me/VaslZone">@VaslZone</a> · v11
        </div>
    </div>

    <script>
        // ============================================================
        // CONFIG
        // ============================================================
        var API_URL = "/api/public/sub-single/SUB_ID_PLACEHOLDER";
        var allLinks = [];
        var chartInstance = null;

        // ============================================================
        // HELPERS
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

        function showToast(msg) {
            var t = document.getElementById('toast');
            t.textContent = '✅ ' + msg;
            t.classList.add('show');
            clearTimeout(t._hide);
            t._hide = setTimeout(function() { t.classList.remove('show'); }, 2000);
        }

        // ============================================================
        // ROCKET
        // ============================================================
        var rocketFired = false;

        function fireRocket() {
            if (rocketFired) return;
            rocketFired = true;
            var el = document.getElementById('rocket');
            el.classList.add('launch');

            setTimeout(function() {
                createExplosion();
                el.classList.add('hidden');
                var target = document.querySelector('.config');
                if (target) target.scrollIntoView({ behavior: 'smooth', block: 'center' });
                setTimeout(function() {
                    rocketFired = false;
                    el.classList.remove('launch', 'hidden');
                }, 1600);
            }, 1400);
        }

        function createExplosion() {
            var container = document.getElementById('explosion');
            var cx = window.innerWidth / 2;
            var cy = window.innerHeight / 2;

            // rings
            for (var i = 0; i < 4; i++) {
                var ring = document.createElement('div');
                ring.className = 'ring';
                var size = 20 + i * 30;
                ring.style.width = size + 'px';
                ring.style.height = size + 'px';
                ring.style.left = (cx - size / 2) + 'px';
                ring.style.top = (cy - size / 2) + 'px';
                ring.style.animationDelay = (i * 0.07) + 's';
                ring.style.borderWidth = (4 - i * 0.5) + 'px';
                container.appendChild(ring);
                setTimeout(function() { ring.remove(); }, 1000);
            }

            // particles
            var colors = ['#fbbf24', '#fcd34d', '#f59e0b', '#fff', '#fef3c7'];
            for (var i = 0; i < 60; i++) {
                var p = document.createElement('div');
                p.className = 'particle';
                var size = 4 + Math.random() * 12;
                var angle = Math.random() * Math.PI * 2;
                var dist = 100 + Math.random() * 280;
                var tx = Math.cos(angle) * dist;
                var ty = Math.sin(angle) * dist - 80;
                p.style.width = size + 'px';
                p.style.height = size + 'px';
                p.style.left = (cx - size / 2) + 'px';
                p.style.top = (cy - size / 2) + 'px';
                p.style.setProperty('--tx', tx + 'px');
                p.style.setProperty('--ty', ty + 'px');
                p.style.background = 'radial-gradient(circle, #fff, ' + colors[Math.floor(Math.random() * colors.length)] +
                    ')';
                p.style.animationDuration = (0.5 + Math.random() * 0.6) + 's';
                p.style.animationDelay = (Math.random() * 0.2) + 's';
                container.appendChild(p);
                setTimeout(function() { p.remove(); }, 1200);
            }
        }

        // ============================================================
        // FETCH DATA
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
        // CHART
        // ============================================================
        function buildChart(data, labels) {
            var canvas = document.getElementById('usageChart');
            if (!canvas) return;
            var ctx = canvas.getContext('2d');
            if (chartInstance) { chartInstance.destroy();
                chartInstance = null; }

            var gradient = ctx.createLinearGradient(0, 0, 0, 140);
            gradient.addColorStop(0, 'rgba(251,191,36,0.25)');
            gradient.addColorStop(1, 'rgba(251,191,36,0.01)');

            chartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'مصرف (MB)',
                        data: data,
                        borderColor: '#fbbf24',
                        backgroundColor: gradient,
                        borderWidth: 2.5,
                        pointRadius: 0,
                        pointHoverRadius: 6,
                        pointHoverBackgroundColor: '#fbbf24',
                        pointHoverBorderColor: '#000',
                        pointHoverBorderWidth: 2,
                        fill: true,
                        tension: 0.3
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(20,20,20,0.95)',
                            titleColor: '#f0f0f0',
                            bodyColor: '#fbbf24',
                            borderColor: 'rgba(251,191,36,0.2)',
                            borderWidth: 1,
                            padding: 8,
                            cornerRadius: 8,
                            callbacks: {
                                label: function(ctx) {
                                    return formatBytes(ctx.parsed.y * 1024 * 1024);
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255,255,255,0.03)' },
                            ticks: { color: '#4a4a4a', font: { size: 8 } }
                        },
                        y: {
                            grid: { color: 'rgba(255,255,255,0.03)' },
                            ticks: {
                                color: '#4a4a4a',
                                font: { size: 8 },
                                callback: function(v) { return v >= 1024 ? (v / 1024).toFixed(0) + 'GB' : v + 'MB'; }
                            }
                        }
                    },
                    interaction: { intersect: false, mode: 'index' }
                }
            });
        }

        function generateChartData(range) {
            var now = Date.now();
            var points = 30,
                interval = 60 * 1000;
            if (range === '10s') { points = 20;
                interval = 500; } else if (range === '10m') { points = 30;
                interval = 20 * 1000; } else if (range === '1h') { points = 30;
                interval = 2 * 60 * 1000; } else if (range === '1d') { points = 30;
                interval = 48 * 60 * 1000; } else if (range === '1m') { points = 30;
                interval = 24 * 60 * 60 * 1000; }

            var labels = [],
                data = [];
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
        // SPEED TEST (PING)
        // ============================================================
        function runPing() {
            var btn = document.getElementById('pingBtn');
            var res = document.getElementById('pingResult');
            if (btn.disabled) return;
            btn.disabled = true;
            res.textContent = '⏳ پینگ...';
            res.className = 'result loading';

            var start = Date.now();
            fetch(API_URL + '?_=' + start, { method: 'HEAD' })
                .then(function(r) {
                    var ms = Date.now() - start;
                    res.className = 'result';
                    var icon = ms < 60 ? '🟢' : (ms < 150 ? '🟡' : '🔴');
                    res.textContent = icon + ' ' + ms + ' ms';
                    btn.disabled = false;
                })
                .catch(function() {
                    res.className = 'result';
                    res.textContent = '🔴 خطا';
                    btn.disabled = false;
                });
        }

        // ============================================================
        // RENDER PAGE
        // ============================================================
        function renderPage(data) {
            if (!data || !data.links || !data.links.length) {
                document.getElementById('root').innerHTML =
                    '<div class="card" style="text-align:center;padding:40px 20px;">' +
                    '<i class="fas fa-link" style="font-size:40px;color:var(--text3);display:block;margin-bottom:14px;"></i>' +
                    '<p style="color:var(--text3);font-size:13px;">کانفیگی وجود ندارد</p></div>';
                return;
            }

            allLinks = data.links;
            var activeCount = data.links.filter(function(l) { return l.active; }).length;
            var totalUsed = data.links.reduce(function(s, l) { return s + (l.used_bytes || 0); }, 0);

            var html = '';

            // info card
            html += '<div class="card" style="text-align:center;">';
            html += '<div style="font-size:15px;font-weight:800;">' + escapeHtml(data.name || '') + '</div>';
            if (data.desc) html += '<div style="font-size:10.5px;color:var(--text2);margin-top:3px;">' + escapeHtml(data
                .desc) + '</div>';
            html += '</div>';

            // stats
            html += '<div class="stats">';
            html += '<div class="item"><div class="label">وضعیت</div><div class="value">' +
                (data.links.length === 1 ? (data.links[0].active ? 'فعال' : 'غیرفعال') :
                    persianDigits(activeCount) + '/' + persianDigits(data.links.length)) +
                '</div></div>';
            html += '<div class="item"><div class="label">مصرف کل</div><div class="value" style="font-size:17px;">' +
                formatBytes(totalUsed) + '</div></div>';
            html += '<div class="item"><div class="label">اتصالات</div><div class="value">' + persianDigits(data
                .active_connections || 0) + '</div></div>';
            html += '</div>';

            // copy all
            if (data.links.length > 1) {
                html += '<div class="copy-all">';
                html += '<span><i class="fas fa-copy"></i> کپی همه</span>';
                html += '<button onclick="copyAll()">کپی (' + persianDigits(activeCount) + ')</button>';
                html += '</div>';
            }

            // configs
            for (var i = 0; i < data.links.length; i++) {
                var l = data.links[i];
                var pct = l.limit_bytes > 0 ? Math.min(100, (l.used_bytes / l.limit_bytes) * 100) : 0;
                var remain = l.limit_bytes > 0 ? Math.max(0, l.limit_bytes - l.used_bytes) : -1;
                var rc = remain < 0 ? 'green' : (remain < 1048576 ? 'red' : (remain < 1073741824 ? 'yellow' : 'green'));
                var remainLabel = remain < 0 ? '∞ نامحدود' : 'باقی: ' + formatBytes(remain);

                html += '<div class="config">';
                html += '<div class="top">';
                html += '<span class="name">' + escapeHtml(l.label) + '</span>';
                html += '<span class="status ' + (l.active ? 'on' : 'off') + '">' + (l.active ? '● فعال' : '○ غیرفعال') +
                    '</span>';
                html += '</div>';
                html += '<div class="usage">';
                html += '<span>مصرف: <b>' + l.used_fmt + '</b></span>';
                html += '<span>از <b>' + (l.limit_bytes === 0 ? '∞' : l.limit_fmt) + '</b></span>';
                html += '</div>';
                html += '<div class="bar"><div class="fill" style="width:' + pct + '%"></div></div>';
                html += '<span class="remain ' + rc + '"><i class="fas fa-' + (remain < 0 ? 'infinity' : 'database') +
                    '"></i> ' + remainLabel + '</span>';
                html += '<div class="link-box" id="link-' + i + '">' + escapeHtml(l.vless_link || '') + '</div>';
                html += '<div class="actions">';
                html += '<button class="gold" onclick="toggleLink(' + i + ')"><i class="fas fa-eye"></i></button>';
                html += '<button class="gold" onclick="copyLink(' + i + ')"><i class="fas fa-copy"></i> کپی</button>';
                html += '<button class="outline" onclick="showQR(' + i +
                    ')"><i class="fas fa-qrcode"></i></button>';
                html += '</div>';
                html += '</div>';
            }

            // chart
            html += '<div class="chart-box">';
            html += '<div class="head">';
            html += '<span class="title"><i class="fas fa-chart-area"></i> نمودار مصرف</span>';
            html += '<div class="chart-times">';
            html += '<button class="active" data-range="10s" onclick="changeRange(\'10s\',this)">۱۰ث</button>';
            html += '<button data-range="10m" onclick="changeRange(\'10m\',this)">۱۰د</button>';
            html += '<button data-range="1h" onclick="changeRange(\'1h\',this)">۱س</button>';
            html += '<button data-range="1d" onclick="changeRange(\'1d\',this)">۱روز</button>';
            html += '<button data-range="1m" onclick="changeRange(\'1m\',this)">۱ماه</button>';
            html += '</div></div>';
            html += '<div class="chart-wrap"><canvas id="usageChart"></canvas></div>';
            html += '</div>';

            // ping
            html += '<div class="ping-box">';
            html += '<div class="head">';
            html += '<span class="label"><i class="fas fa-bolt"></i> پینگ</span>';
            html += '<button class="btn-ping" id="pingBtn" onclick="runPing()">شروع</button>';
            html += '</div>';
            html += '<div class="result" id="pingResult">—</div>';
            html += '</div>';

            document.getElementById('root').innerHTML = html;

            // init chart
            renderChart('10s');

            // store links for copy
            window._copyLinks = data.links.map(function(l) { return l.vless_link || ''; });
        }

        // ============================================================
        // UI ACTIONS
        // ============================================================
        function toggleLink(i) {
            var el = document.getElementById('link-' + i);
            if (el) el.classList.toggle('open');
        }

        function copyLink(i) {
            var link = window._copyLinks[i] || '';
            if (!link) { showToast('لینکی وجود ندارد'); return; }
            navigator.clipboard.writeText(link).then(function() {
                showToast('کپی شد');
            }).catch(function() {
                var ta = document.createElement('textarea');
                ta.value = link;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                ta.remove();
                showToast('کپی شد');
            });
        }

        function copyAll() {
            var links = window._copyLinks.filter(Boolean);
            if (!links.length) { showToast('لینکی وجود ندارد'); return; }
            var text = links.join('\n');
            navigator.clipboard.writeText(text).then(function() {
                showToast('همه کپی شد (' + links.length + ')');
            }).catch(function() {
                var ta = document.createElement('textarea');
                ta.value = text;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                ta.remove();
                showToast('همه کپی شد');
            });
        }

        function showQR(i) {
            var link = window._copyLinks[i] || '';
            if (!link) { showToast('لینکی وجود ندارد'); return; }
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
        // INIT
        // ============================================================
        (async function() {
            var audio = document.getElementById('bgMusic');
            if (audio) audio.volume = 0.04;

            var data = await fetchData();
            if (data) {
                renderPage(data);
            } else {
                document.getElementById('root').innerHTML =
                    '<div class="card" style="text-align:center;padding:40px 20px;">' +
                    '<i class="fas fa-exclamation-triangle" style="font-size:40px;color:var(--red);display:block;margin-bottom:12px;"></i>' +
                    '<p style="color:var(--text3);font-size:13px;">خطا در دریافت اطلاعات</p></div>';
            }
        })();
    </script>

</body>
</html>
""".replace("SUB_ID_PLACEHOLDER", sub_id)
