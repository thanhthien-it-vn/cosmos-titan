import streamlit as st

def load_cosmos_theme():
    """
    Nạp toàn bộ CSS từ bản thiết kế TITAN HRM Prototype v1.9 HTML.
    """
    st.markdown("""
        <style>
        /* --- 1. FONTS --- */
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;600;700;800;900&family=Orbitron:wght@500;700;900&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

        /* --- 2. GLOBAL RESET --- */
        :root {
            --bg-color: #000000;
            --panel-bg: rgba(15, 23, 42, 0.6); 
            --text-color: #e2e8f0;
        }
        
        /* Ép nền đen tuyệt đối cho toàn bộ ứng dụng */
        .stApp {
            background-color: var(--bg-color);
            background-image: radial-gradient(circle at center, #1a1a1a 0%, #000000 100%);
            color: var(--text-color);
            font-family: 'Be Vietnam Pro', sans-serif;
        }

        /* Ẩn các thành phần thừa của Streamlit */
        header, footer, .stDeployButton {display: none !important;}
        #MainMenu {visibility: hidden;}

        /* --- 3. HIỆU ỨNG NEBULA (VÒNG XOAY LOGO) --- */
        .titan-nebula { position: relative; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
        .nebula-core { width: 12px; height: 12px; background: #3b82f6; border-radius: 50%; box-shadow: 0 0 20px #3b82f6, 0 0 40px #2563eb; animation: core-pulse 4s infinite ease-in-out; z-index: 2; }
        .nebula-ring-1 { position: absolute; width: 100%; height: 100%; border-radius: 50%; border: 2px solid transparent; border-top-color: rgba(96, 165, 250, 0.8); border-right-color: rgba(96, 165, 250, 0.2); animation: spin 8s linear infinite; }
        .nebula-ring-2 { position: absolute; width: 70%; height: 70%; border-radius: 50%; border: 2px solid transparent; border-bottom-color: rgba(147, 197, 253, 0.8); border-left-color: rgba(147, 197, 253, 0.2); animation: spin-reverse 10s linear infinite; }

        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
        @keyframes core-pulse { 0%, 100% { transform: scale(0.9); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } }

        /* --- 4. BIẾN NÚT BẤM THÀNH PORTAL TILE (GIỐNG HTML) --- */
        div.stButton > button {
            background: rgba(15, 23, 42, 0.3) !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-bottom: 4px solid rgba(255, 255, 255, 0.1) !important; /* Viền dưới dày */
            border-radius: 16px !important;
            height: 180px !important;
            width: 100% !important;
            transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
            
            /* Typography */
            font-family: 'Orbitron', sans-serif !important;
            text-transform: uppercase !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            color: #94a3b8 !important;
            
            /* Layout */
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 10px !important;
        }

        div.stButton > button:hover {
            transform: translateY(-10px) !important;
            background: rgba(30, 41, 59, 0.6) !important;
            color: #ffffff !important;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5) !important;
        }

        /* --- 5. MÀU SẮC RIÊNG CHO TỪNG MODULE (CSS Selector nâng cao) --- */
        /* Tổng quan - Blue */
        div.stButton > button:has(div:contains("TỔNG QUAN")) { border-bottom-color: #3b82f6 !important; }
        div.stButton > button:has(div:contains("TỔNG QUAN")):hover { border-color: #3b82f6 !important; box-shadow: 0 0 30px rgba(59, 130, 246, 0.4) !important; }

        /* Tiền lương - Amber */
        div.stButton > button:has(div:contains("TIỀN LƯƠNG")) { border-bottom-color: #f59e0b !important; }
        div.stButton > button:has(div:contains("TIỀN LƯƠNG")):hover { border-color: #f59e0b !important; box-shadow: 0 0 30px rgba(245, 158, 11, 0.4) !important; }
        
        /* KPI - Rose */
        div.stButton > button:has(div:contains("KPI")) { border-bottom-color: #f43f5e !important; }
        div.stButton > button:has(div:contains("KPI")):hover { border-color: #f43f5e !important; box-shadow: 0 0 30px rgba(244, 63, 94, 0.4) !important; }

        /* Nhân sự - Rose (Theo ảnh mẫu) hoặc Emerald */
        div.stButton > button:has(div:contains("NHÂN SỰ")) { border-bottom-color: #8b5cf6 !important; }
        div.stButton > button:has(div:contains("NHÂN SỰ")):hover { border-color: #8b5cf6 !important; box-shadow: 0 0 30px rgba(139, 92, 246, 0.4) !important; }

        /* Chấm công - Emerald */
        div.stButton > button:has(div:contains("CHẤM CÔNG")) { border-bottom-color: #10b981 !important; }
        div.stButton > button:has(div:contains("CHẤM CÔNG")):hover { border-color: #10b981 !important; box-shadow: 0 0 30px rgba(16, 185, 129, 0.4) !important; }

        /* Admin - Slate */
        div.stButton > button:has(div:contains("ADMIN")) { border-bottom-color: #64748b !important; }
        div.stButton > button:has(div:contains("ADMIN")):hover { border-color: #64748b !important; box-shadow: 0 0 30px rgba(100, 116, 139, 0.4) !important; }

        /* AI - Violet */
        div.stButton > button:has(div:contains("TITAN AI")) { border-bottom-color: #d946ef !important; }
        div.stButton > button:has(div:contains("TITAN AI")):hover { border-color: #d946ef !important; box-shadow: 0 0 30px rgba(217, 70, 239, 0.4) !important; }

        </style>
    """, unsafe_allow_html=True)
