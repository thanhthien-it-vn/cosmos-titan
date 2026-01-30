import streamlit as st
from utils.database import get_config_all
from utils.ui_core import apply_cosmos_style, header_component, footer_component
from modules.main_menu import render_main_menu

# --- CẤU HÌNH HỆ THỐNG ---
st.set_page_config(
    page_title="COSMOS-TITAN SYSTEM",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ÁP DỤNG GIAO DIỆN (Lấy từ utils/ui_core.py) ---
apply_cosmos_style()

def main():
    # 1. Hiển thị Header
    header_component()

    # 2. Khởi tạo trạng thái phiên làm việc
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = None

    # 3. ĐIỀU HƯỚNG (ROUTER)
    # Nếu chưa chọn tab nào -> Gọi module Menu để vẽ lưới
    if st.session_state.active_tab is None:
        render_main_menu()
        footer_component()

    # Nếu đã chọn Tab -> Điều hướng vào trong
    else:
        # Nút Quay lại (Dùng chung)
        if st.button("⬅️ TRỞ VỀ TRẠM CHỈ HUY (MENU)"):
            st.session_state.active_tab = None
            st.rerun()
            
        # Lấy ID của Tab đang chọn
        tab_id = st.session_state.active_tab
        
        # --- ROUTER ĐẾN CÁC MODULE CON ---
        if tab_id == 6:
            # Ví dụ: Gọi Module Admin (Sau này sẽ tách file riêng nữa)
            st.markdown("<h2 style='color:#3b82f6; font-family:Orbitron'>6. CẤU HÌNH HỆ THỐNG</h2>", unsafe_allow_html=True)
            st.info("Đang kết nối tới Supabase Singapore...")
            configs = get_config_all()
            if configs:
                st.dataframe(configs, use_container_width=True)
            else:
                st.warning("Chưa có dữ liệu cấu hình.")
                
        elif tab_id == 9:
            st.markdown("<h2 style='color:#a855f7; font-family:Orbitron'>9. TITAN AI INTELLIGENCE</h2>", unsafe_allow_html=True)
            st.write("Xin chào, tôi là AI Toàn năng của hệ thống COSMOS-TITAN.")
            
        else:
            # Các module đang xây dựng
            st.warning(f"🚧 Module {tab_id} đang được Nghệ nhân xây dựng (Frozen UI Mode).")

if __name__ == "__main__":
    main()
