import streamlit as st

def load_cosmos_theme():
    """
    Kỹ thuật Pixel-Perfect: Ép giao diện Streamlit giống hệt bản Prototype HTML v1.9.
    """
    st.markdown("""
        <style>
        /* --- 1. IMPORT FONTS TỪ BẢN GỐC --- */
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;600;700;800;900&family=Orbitron:wght@500;700;900&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

        /* --- 2. BIẾN MÀU SẮC (ROOT VARIABLES) --- */
        :root {
            --bg-color: #000;
            --panel-bg: rgba(15, 23, 42, 0.3);
            --border-color: rgba(255, 255, 255, 0.1);
        }

        /* --- 3. CẤU HÌNH NỀN & CANVAS --- */
        .stApp {
            background-color: var(--bg-color);
            font-family: 'Be Vietnam Pro', sans-serif;
        }
        
        /* Ẩn Header mặc định của Streamlit */
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}

        /* Canvas Sao bay nằm dưới cùng */
        #warp-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 0; /* Nằm dưới nội dung */
            pointer-events: none;
        }

        /* --- 4. BIẾN HÓA NÚT BẤM THÀNH "PORTAL TILE" --- */
        /* Đây là đoạn quan trọng nhất để giống bản gốc */
        div.stButton > button {
            background: var(--panel-bg) !important;
            backdrop-filter: blur(10px) !important;
            border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-left: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-bottom-width: 8px !important; /* Giống bản gốc */
            border-bottom-style: solid !important;
            border-radius: 16px !important;
            
            height: 220px !important; /* Chiều cao chuẩn */
            width: 100% !important;
            
            /* Typography */
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            font-size: 1rem !important;
            color: #94a3b8 !important;
            
            /* Layout bên trong nút */
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 15px !important;
            
            transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), background 0.3s !important;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7) !important;
            position: relative !important;
            overflow: hidden !important;
            z-index: 10 !important;
        }

        /* Hiệu ứng Hover: Nổi lên và sáng */
        div.stButton > button:hover {
            transform: translateY(-15px) !important;
            background: rgba(30, 41, 59, 0.5) !important;
            color: #ffffff !important;
        }

        /* --- 5. MÀU SẮC RIÊNG CHO TỪNG LOẠI TILE (Mapping ID) --- */
        /* Sử dụng CSS Selector thông minh để bắt màu dựa trên tên nút */
        
        /* Tổng quan (Blue) */
        div.stButton > button:has(div:contains("1.")) { border-bottom-color: #3b82f6 !important; color: #60a5fa !important; }
        div.stButton > button:has(div:contains("1.")):hover { box-shadow: 0 0 40px rgba(59, 130, 246, 0.6) !important; border-bottom-color: #60a5fa !important; }

        /* Tiền lương (Amber) */
        div.stButton > button:has(div:contains("2.")) { border-bottom-color: #f59e0b !important; color: #fbbf24 !important; }
        div.stButton > button:has(div:contains("2.")):hover { box-shadow: 0 0 40px rgba(245, 158, 11, 0.6) !important; border-bottom-color: #fbbf24 !important; }

        /* KPI (Rose) */
        div.stButton > button:has(div:contains("3.")) { border-bottom-color: #f43f5e !important; color: #fb7185 !important; }
        div.stButton > button:has(div:contains("3.")):hover { box-shadow: 0 0 40px rgba(244, 63, 94, 0.6) !important; border-bottom-color: #fb7185 !important; }

        /* Nhân sự (Emerald) */
        div.stButton > button:has(div:contains("4.")) { border-bottom-color: #10b981 !important; color: #34d399 !important; }
        div.stButton > button:has(div:contains("4.")):hover { box-shadow: 0 0 40px rgba(16, 185, 129, 0.6) !important; border-bottom-color: #34d399 !important; }

        /* Bảo hiểm (Cyan) */
        div.stButton > button:has(div:contains("5.")) { border-bottom-color: #06b6d4 !important; color: #22d3ee !important; }
        div.stButton > button:has(div:contains("5.")):hover { box-shadow: 0 0 40px rgba(6, 182, 212, 0.6) !important; border-bottom-color: #22d3ee !important; }
        
        /* Admin (Slate) */
        div.stButton > button:has(div:contains("6.")) { border-bottom-color: #64748b !important; color: #94a3b8 !important; }
        div.stButton > button:has(div:contains("6.")):hover { box-shadow: 0 0 40px rgba(148, 163, 184, 0.6) !important; border-bottom-color: #cbd5e1 !important; }

        /* Chấm công (Emerald/Blue mix) */
        div.stButton > button:has(div:contains("7.")) { border-bottom-color: #10b981 !important; color: #34d399 !important; }
        div.stButton > button:has(div:contains("7.")):hover { box-shadow: 0 0 40px rgba(16, 185, 129, 0.6) !important; border-bottom-color: #34d399 !important; }

        /* Hậu cần (Orange) */
        div.stButton > button:has(div:contains("8.")) { border-bottom-color: #f97316 !important; color: #fdba74 !important; }
        div.stButton > button:has(div:contains("8.")):hover { box-shadow: 0 0 40px rgba(249, 115, 22, 0.6) !important; border-bottom-color: #fdba74 !important; }

        /* AI (Violet) */
        div.stButton > button:has(div:contains("9.")) { border-bottom-color: #8b5cf6 !important; color: #a78bfa !important; }
        div.stButton > button:has(div:contains("9.")):hover { box-shadow: 0 0 40px rgba(139, 92, 246, 0.6) !important; border-bottom-color: #c4b5fd !important; }


        /* --- 6. ANIMATION KEYFRAMES (Copy từ HTML) --- */
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
        @keyframes core-pulse { 0%, 100% { transform: scale(0.9); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } }

        /* Nebula Classes cho Header */
        .titan-nebula { position: relative; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
        .nebula-core { width: 12px; height: 12px; background: #3b82f6; border-radius: 50%; box-shadow: 0 0 20px #3b82f6, 0 0 40px #2563eb; animation: core-pulse 4s infinite ease-in-out; z-index: 2; }
        .nebula-ring-1 { position: absolute; width: 100%; height: 100%; border-radius: 50%; border: 2px solid transparent; border-top-color: rgba(96, 165, 250, 0.8); border-right-color: rgba(96, 165, 250, 0.2); animation: spin 8s linear infinite; }
        .nebula-ring-2 { position: absolute; width: 70%; height: 70%; border-radius: 50%; border: 2px solid transparent; border-bottom-color: rgba(147, 197, 253, 0.8); border-left-color: rgba(147, 197, 253, 0.2); animation: spin-reverse 10s linear infinite; }

        </style>

        <!-- SCRIPT CANVAS SAO BAY (Javascript chạy nền) -->
        <script>
            // Tự động tìm và tạo canvas nếu chưa có
            let canvas = document.getElementById('warp-canvas');
            if(!canvas) {
                // Nếu chưa có (Streamlit chưa render kịp), script này sẽ đợi
            } else {
                const ctx = canvas.getContext('2d');
                let width, height, stars = [];
                const numStars = 200, speed = 0.2; // Tốc độ giống bản gốc

                function resize() {
                    width = window.innerWidth;
                    height = window.innerHeight;
                    canvas.width = width;
                    canvas.height = height;
                    ctx.translate(width/2, height/2); // Tâm ở giữa như bản gốc
                }

                class Star {
                    constructor() { this.reset(); }
                    reset() {
                        this.x = (Math.random() - 0.5) * width * 3;
                        this.y = (Math.random() - 0.5) * height * 3;
                        this.z = Math.random() * width;
                        this.size = Math.random() * 2;
                        this.pz = this.z;
                    }
                    update() {
                        this.z -= speed;
                        if (this.z <= 0) { this.reset(); this.z = width; this.pz = this.z; }
                    }
                    draw() {
                        const x = this.x / this.z * 100;
                        const y = this.y / this.z * 100;
                        const op = 1 - this.z / width;
                        
                        ctx.beginPath();
                        ctx.arc(x, y, this.size * (op + 0.5), 0, Math.PI * 2);
                        ctx.fillStyle = `rgba(200, 230, 255, ${op * 0.8})`;
                        ctx.fill();
                        this.pz = this.z;
                    }
                }

                function init() {
                    resize();
                    stars = [];
                    for(let i=0; i<numStars; i++) stars.push(new Star());
                    animate();
                }

                function animate() {
                    ctx.clearRect(-width/2, -height/2, width, height); // Xóa frame cũ
                    stars.forEach(s => { s.update(); s.draw(); });
                    requestAnimationFrame(animate);
                }

                window.addEventListener('resize', () => { resize(); init(); });
                init();
            }
        </script>
    """, unsafe_allow_html=True)
