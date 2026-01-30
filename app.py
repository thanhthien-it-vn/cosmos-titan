import streamlit as st
from utils.database import get_config_all
from utils.styles import load_css
from utils.components import render_header, render_footer
from utils.session import init_session_state
from utils.constants import PAGE_CONFIG, MODULES
from modules.main_menu import render_main_menu

# 1. CẤU HÌNH HỆ THỐNG (Lấy từ constants.py)
st.set_page_config(**PAGE_CONFIG)

# 2. KHỞI TẠO (Giao diện & Session)
load_css()
init_session_state()

def main():
    header_component()

    # 3. ĐIỀU HƯỚNG (ROUTER)
    if st.session_state.active_tab is None:
        render_main_menu()
        render_footer()

    else:
        # Nút Quay lại
        if st.button("⬅️ TRỞ VỀ TRẠM CHỈ HUY (MENU)"):
            st.session_state.active_tab = None
            st.rerun()
            
        tab_id = st.session_state.active_tab
        
        # Lấy tên module hiện tại để hiển thị (Lấy từ constants)
        current_module = next((m for m in MODULES if m['id'] == tab_id), None)
        
        # --- ROUTER MODULE ---
        if tab_id == 6:
            st.markdown(f"<h2 style='color:#3b82f6; font-family:Orbitron'>{current_module['name']}</h2>", unsafe_allow_html=True)
            st.info("Đang kết nối tới Supabase Singapore...")
            configs = get_config_all()
            if configs:
                st.dataframe(configs, use_container_width=True)
            else:
                st.warning("Chưa có dữ liệu cấu hình.")
                
        elif tab_id == 9:
            st.markdown(f"<h2 style='color:#a855f7; font-family:Orbitron'>{current_module['name']}</h2>", unsafe_allow_html=True)
            st.write("Xin chào, tôi là AI Toàn năng của hệ thống COSMOS-TITAN.")
            
        else:
            if current_module:
                st.warning(f"🚧 Module {current_module['name']} đang được Nghệ nhân xây dựng (Frozen UI Mode).")

if __name__ == "__main__":
    main()
