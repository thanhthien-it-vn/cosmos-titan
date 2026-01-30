import streamlit as st

def load_cosmos_theme():
    """
    Tiêm toàn bộ linh hồn Cyberpun k từ bản Prototype vào hệ thống.
    Bao gồm: Hiệu ứng Stars Warp, Neon Glow, và Portal Tiles.
    """
    st.markdown("""
        <style>
        /* 1. NẠP FONT CHỮ CHUẨN TITAN */
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;600;700&family=Orbitron:wght@500;700;900&display=swap');

        /* 2. THIẾT LẬP NỀN VŨ TRỤ (BACKGROUND) */
        .stApp {
            background-color: #000000;
            color: #e2e8f0;
        }

        /* Hiệu ứng Stars Warp Canvas nằm dưới cùng */
        #warp-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            pointer-events: none;
        }

        /* 3. ĐỊNH NGHĨA PORTAL TILES (Cấu trúc ô gạch) */
        div.stButton > button {
            background: rgba(15, 23, 42, 0.3) !important;
            backdrop-filter: blur(10px) !important;
            border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-left: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-bottom-width: 6px !important;
            border-bottom-style: solid !important;
            border-radius: 16px !important;
            height: 200px !important;
            width: 100% !important;
            transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
            font-family: 'Orbitron', sans-serif !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            font-size: 0.9rem !important;
            color: #94a3b8 !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
        }

        /* Hiệu ứng hover cho từng loại màu (Glow) */
        div.stButton > button:hover {
            transform: translateY(-15px) !important;
            color: #ffffff !important;
            background: rgba(30, 41, 59, 0.5) !important;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7) !important;
        }

        /* 4. MÀU SẮC NEON CHO TỪNG MODULE (Dựa trên ID nút bấm) */
        /* Overview - Blue */
        button[key*="btn_1"] { border-bottom-color: #3b82f6 !important; }
        button[key*="btn_1"]:hover { box-shadow: 0 0 30px rgba(59, 130, 246, 0.6) !important; border-bottom-color: #60a5fa !important; }
        
        /* Salary - Amber */
        button[key*="btn_2"] { border-bottom-color: #f59e0b !important; }
        button[key*="btn_2"]:hover { box-shadow: 0 0 30px rgba(245, 158, 11, 0.6) !important; border-bottom-color: #fbbf24 !important; }
        
        /* KPI - Rose */
        button[key*="btn_3"] { border-bottom-color: #f43f5e !important; }
        button[key*="btn_3"]:hover { box-shadow: 0 0 30px rgba(244, 63, 94, 0.6) !important; border-bottom-color: #fb7185 !important; }
        
        /* HR - Emerald */
        button[key*="btn_4"] { border-bottom-color: #10b981 !important; }
        button[key*="btn_4"]:hover { box-shadow: 0 0 30px rgba(16, 185, 129, 0.6) !important; border-bottom-color: #34d399 !important; }
        
        /* Insurance - Cyan */
        button[key*="btn_5"] { border-bottom-color: #06b6d4 !important; }
        button[key*="btn_5"]:hover { box-shadow: 0 0 30px rgba(6, 182, 212, 0.6) !important; border-bottom-color: #22d3ee !important; }
        
        /* Admin - Slate */
        button[key*="btn_6"] { border-bottom-color: #64748b !important; }
        button[key*="btn_6"]:hover { box-shadow: 0 0 30px rgba(100, 116, 139, 0.6) !important; border-bottom-color: #94a3b8 !important; }

        /* 5. TIÊU ĐỀ HỆ THỐNG */
        .titan-title-main {
            font-family: 'Orbitron', sans-serif;
            font-size: 4rem;
            font-weight: 900;
            text-align: center;
            background: linear-gradient(to bottom, #ffffff 0%, #334155 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 0.5em;
            text-shadow: 0 0 30px rgba(59, 130, 246, 0.3);
            margin-bottom: 0;
            padding-top: 50px;
        }
        .titan-subtitle-main {
            font-family: 'Be Vietnam Pro', sans-serif;
            text-align: center;
            color: #475569;
            font-size: 0.7rem;
            letter-spacing: 0.4em;
            margin-bottom: 80px;
            text-transform: uppercase;
        }

        /* Ẩn các thành phần mặc định của Streamlit để tăng độ thẩm mỹ */
        header, footer {visibility: hidden;}
        .stDeployButton {display:none;}
        </style>

        <!-- CANVAS CHẠY HIỆU ỨNG SAO SAU LƯNG -->
        <canvas id="warp-canvas"></canvas>
        <script>
            const canvas = document.getElementById('warp-canvas');
            const ctx = canvas.getContext('2d');
            let width, height, stars = [];
            const numStars = 200, speed = 0.5;

            function resize() {
                width = window.innerWidth;
                height = window.innerHeight;
                canvas.width = width;
                canvas.height = height;
            }

            class Star {
                constructor() { this.reset(); }
                reset() {
                    this.x = (Math.random() - 0.5) * width * 3;
                    this.y = (Math.random() - 0.5) * height * 3;
                    this.z = Math.random() * width;
                    this.size = Math.random() * 2;
                }
                update() {
                    this.z -= speed;
                    if (this.z <= 0) { this.reset(); this.z = width; }
                }
                draw() {
                    const x = (this.x / this.z) * 100 + width / 2;
                    const y = (this.y / this.z) * 100 + height / 2;
                    const opacity = 1 - this.z / width;
                    ctx.beginPath();
                    ctx.arc(x, y, this.size * (opacity + 0.5), 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(200, 230, 255, ${opacity})`;
                    ctx.fill();
                }
            }

            function init() {
                resize();
                stars = Array.from({length: numStars}, () => new Star());
                animate();
            }

            function animate() {
                ctx.fillStyle = '#000';
                ctx.fillRect(0, 0, width, height);
                stars.forEach(s => { s.update(); s.draw(); });
                requestAnimationFrame(animate);
            }

            window.addEventListener('resize', resize);
            init();
        </script>
    """, unsafe_allow_html=True)
