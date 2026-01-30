import streamlit as st
from utils.database import get_config_all, get_config_value

# Cấu hình trang với phong cách chuyên nghiệp
st.set_page_config(
    page_title="COSMOS-TITAN | Next-Gen HRM",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- PHONG CÁCH GIAO DIỆN (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button {
        width: 100%;
        height: 150px;
        border-radius: 15px;
        border: 1px solid #30363d;
        background-color: #161b22;
        color: #c9d1d9;
        font-size: 1.2rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        border-color: #58a6ff;
        color: #58a6ff;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .title-text {
        text-align: center;
        color: #58a6ff;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 5px;
        margin-bottom: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.markdown("<h1 class='title-text'>COSMOS-TITAN SYSTEM</h1>", unsafe_allow_html=True)

    # Khởi tạo 9 Tab theo sơ đồ 3x3 đã chốt
    # Hàng 1: Tổng Quan (1), Lương (2), KPI (3)
    # Hàng 2: Nhân Sự (4), Bảo Hiểm (5), Cấu Hình (6)
    # Hàng 3: Chấm Công (7), Hậu Cần (8), AI (9)
    
    modules = [
        {"id": 1, "name": "1. TỔNG QUAN", "icon": "📊"},
        {"id": 2, "name": "2. TIỀN LƯƠNG", "icon": "💰"},
        {"id": 3, "name": "3. ĐÁNH GIÁ KPI", "icon": "🎯"},
        {"id": 4, "name": "4. NHÂN SỰ", "icon": "👥"},
        {"id": 5, "name": "5. THUẾ & BẢO HIỂM", "icon": "📜"},
        {"id": 6, "name": "6. CẤU HÌNH/ADMIN", "icon": "⚙️"},
        {"id": 7, "name": "7. CHẤM CÔNG", "icon": "📅"},
        {"id": 8, "name": "8. HẬU CẦN", "icon": "🚚"},
        {"id": 9, "name": "9. TITAN AI", "icon": "🧠"}
    ]

    # Hiển thị lưới 3x3
    for i in range(0, 9, 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(modules):
                with cols[j]:
                    if st.button(f"{modules[idx]['icon']}\n\n{modules[idx]['name']}", key=f"btn_{idx}"):
                        st.session_state.active_tab = modules[idx]['id']
                        st.rerun()

    # Xử lý khi nhấn vào Tab (Ví dụ demo cho Tab 6 Admin)
    if 'active_tab' in st.session_state:
        st.divider()
        tab_id = st.session_state.active_tab
        st.subheader(f"Đ đang mở: {next(m['name'] for m in modules if m['id'] == tab_id)}")
        
        if tab_id == 6:
            st.info("💡 Đây là trạm điều khiển các tham số 'mềm'.")
            configs = get_config_all()
            if configs:
                st.table(configs)
            else:
                st.warning("Chưa có dữ liệu cấu hình. Hãy nạp row đầu tiên trên Supabase.")
        
        if st.button("⬅️ Quay lại Menu chính"):
            del st.session_state.active_tab
            st.rerun()

if __name__ == "__main__":
    main()
