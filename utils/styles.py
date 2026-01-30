import streamlit as st

def load_css():
    """
    Hàm này chỉ chịu trách nhiệm tiêm mã CSS vào trang web.
    Tách biệt hoàn toàn với logic hiển thị.
    """
    st.markdown("""
        <style>
        /* 1. Nhập Font chữ Orbitron & Be Vietnam Pro */
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;600;700&family=Orbitron:wght@500;700;900&display=swap');

        /* 2. Thiết lập nền đen vũ trụ */
        .stApp {
            background-color: #050505;
            background-image: radial-gradient(circle at center, #1a1a1a 0%, #000000 100%);
            color: #e2e8f0;
        }

        /* 3. Tiêu đề hệ thống */
        .titan-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.5rem;
            font-weight: 900;
            text-align: center;
            background: -webkit-linear-gradient(45deg, #3b82f6, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(59, 130, 246, 0.5);
            margin-bottom: 10px;
            letter-spacing: 4px;
        }
        .titan-subtitle {
            font-family: 'Be Vietnam Pro', sans-serif;
            text-align: center;
            color: #64748b;
            font-size: 0.9rem;
            letter-spacing: 3px;
            margin-bottom: 50px;
            text-transform: uppercase;
        }

        /* 4. Tùy biến các nút bấm thành Portal Tiles */
        div.stButton > button {
            width: 100%;
            height: 180px; 
            background: rgba(30, 41, 59, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            color: #94a3b8;
            font-family: 'Orbitron', sans-serif;
            font-size: 1.1rem;
            transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
            backdrop-filter: blur(10px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        /* Hiệu ứng Hover phát sáng */
        div.stButton > button:hover {
            transform: translateY(-10px);
            color: #ffffff;
            background: rgba(30, 41, 59, 0.8);
            border-color: #3b82f6;
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.4);
        }
        
        /* 5. Ẩn các thành phần thừa của Streamlit */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
