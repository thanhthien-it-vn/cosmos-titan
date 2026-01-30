import streamlit as st

def render_main_menu():
    """
    Hàm này chịu trách nhiệm vẽ lưới 3x3 (Portal Grid).
    Tách ra để app.py không bị rối.
    """
    
    # Hàng 1
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📊 1. TỔNG QUAN"): st.session_state.active_tab = 1; st.rerun()
    with c2:
        if st.button("💰 2. TIỀN LƯƠNG"): st.session_state.active_tab = 2; st.rerun()
    with c3:
        if st.button("🎯 3. ĐÁNH GIÁ KPI"): st.session_state.active_tab = 3; st.rerun()

    # Hàng 2
    st.write("") # Spacer tạo khoảng cách
    c4, c5, c6 = st.columns(3)
    with c4:
        if st.button("👥 4. NHÂN SỰ"): st.session_state.active_tab = 4; st.rerun()
    with c5:
        if st.button("📜 5. BẢO HIỂM & THUẾ"): st.session_state.active_tab = 5; st.rerun()
    with c6:
        if st.button("⚙️ 6. CẤU HÌNH ADMIN"): st.session_state.active_tab = 6; st.rerun()

    # Hàng 3
    st.write("") # Spacer tạo khoảng cách
    c7, c8, c9 = st.columns(3)
    with c7:
        if st.button("📅 7. CHẤM CÔNG"): st.session_state.active_tab = 7; st.rerun()
    with c8:
        if st.button("🚚 8. HẬU CẦN"): st.session_state.active_tab = 8; st.rerun()
    with c9:
        if st.button("🧠 9. TITAN AI"): st.session_state.active_tab = 9; st.rerun()
