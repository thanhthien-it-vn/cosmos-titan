import streamlit as st

def render_header():
    """Hiển thị Header chuẩn của COSMOS-TITAN"""
    st.markdown("<div class='titan-title'>COSMOS TITAN</div>", unsafe_allow_html=True)
    st.markdown("<div class='titan-subtitle'>THE NEXT GEN HRM x AI SYSTEM</div>", unsafe_allow_html=True)

def render_footer():
    """Hiển thị Footer bản quyền"""
    st.markdown("""
        <div style='text-align: center; color: #475569; margin-top: 50px; font-size: 0.8rem;'>
            DESIGNED & BUILT BY NGUYỄN THANH THIỆN<br>
            POWERED BY SUPABASE SINGAPORE & STREAMLIT
        </div>
    """, unsafe_allow_html=True)
