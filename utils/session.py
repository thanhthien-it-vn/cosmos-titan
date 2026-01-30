import streamlit as st

def init_session_state():
    """
    Khởi tạo toàn bộ các biến Session State cần thiết cho ứng dụng.
    Giúp app.py gọn gàng hơn.
    """
    # Biến lưu Tab đang hoạt động
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = None
    
    # Biến lưu thông tin User (Chuẩn bị cho sau này)
    if 'user_role' not in st.session_state:
        st.session_state.user_role = 'guest'
