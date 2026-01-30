import streamlit as st
from utils.constants import MODULES

def render_main_menu():
    """
    Vẽ lưới 3x3 dựa trên danh sách MODULES từ constants.py.
    Code thông minh: Tự động tính toán dòng cột, không cần if-else thủ công.
    """
    
    # Duyệt qua danh sách module và vẽ lưới 3 cột
    # Logic: Cắt list thành các chunk 3 phần tử
    for i in range(0, len(MODULES), 3):
        cols = st.columns(3)
        chunk = MODULES[i:i+3]
        
        for j, mod in enumerate(chunk):
            with cols[j]:
                # Tạo nút bấm
                if st.button(f"{mod['icon']}\n\n{mod['name']}", key=f"btn_{mod['id']}"):
                    st.session_state.active_tab = mod['id']
                    st.rerun()
        
        # Tạo khoảng cách giữa các hàng
        st.write("")
