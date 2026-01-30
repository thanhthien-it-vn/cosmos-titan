import streamlit as st
from utils.constants import PAGE_CONFIG, MODULES
from utils.styles import load_css
from utils.components import render_header, render_footer
from utils.session import init_session_state
from modules.main_menu import render_main_menu

# 1. CẤU HÌNH HỆ THỐNG
st.set_page_config(**PAGE_CONFIG)

# 2. KHỞI TẠO HẠ TẦNG
load_css()
init_session_state()

def main():
    # Luôn hiển thị Header
    render_header()

    # 3. ĐIỀU HƯỚNG (ROUTER) TRUNG TÂM
    if st.session_state.active_tab is None:
        render_main_menu()
        render_footer()
    else:
        # Nút Quay lại (Dùng chung cho mọi Module)
        if st.button("⬅️ TRỞ VỀ TRẠM CHỈ HUY (MENU)"):
            st.session_state.active_tab = None
            st.rerun()
            
        tab_id = st.session_state.active_tab
        current_mod = next((m for m in MODULES if m['id'] == tab_id), None)

        # GỌI MODULE TƯƠNG ỨNG (Dynamic Import Pattern)
        # Cách tách này giúp app.py không bao giờ bị phình to
        if tab_id == 6:
            from modules.admin import render_admin_zone
            render_admin_zone(current_mod)
        elif tab_id == 9:
            from modules.ai_titan import render_ai_zone
            render_ai_zone(current_mod)
        else:
            st.warning(f"🚧 Module {current_mod['name']} đang được xây dựng (Frozen UI).")

if __name__ == "__main__":
    main()
