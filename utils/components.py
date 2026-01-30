import streamlit as st

def render_header():
    """Hiển thị Header chuẩn TITAN SYSTEM từ Prototype"""
    st.markdown("""
        <div class="titan-title-main">TITAN</div>
        <div class="titan-subtitle-main">THE NEXT GEN HRM v1.9 (FINAL PROTOTYPE)</div>
    """, unsafe_allow_html=True)

def render_footer():
    """Hiển thị Footer bản quyền thiết kế"""
    st.markdown("""
        <div style="text-align: center; margin-top: 100px; padding-bottom: 50px;">
            <p style="text-transform: uppercase; letter-spacing: 0.2em; font-size: 0.6rem; color: #475569; margin-bottom: 4px;">Designed & Built by</p>
            <h2 style="font-family: 'Orbitron', sans-serif; font-size: 1.2rem; font-weight: 700; color: #94a3b8; letter-spacing: 2px;">NGUYỄN THANH THIỆN</h2>
            <div style="color: #475569; font-size: 0.6rem; margin-top: 5px;">
                <span>Vina: 0918 283 825</span> | <span>Vietnam</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
