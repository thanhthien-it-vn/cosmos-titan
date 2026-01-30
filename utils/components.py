import streamlit as st

def render_header():
    """
    Hiển thị Header với Logo TITAN xoay (Nebula Animation).
    Sử dụng các class CSS đã định nghĩa trong styles.py
    """
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 50px; padding-bottom: 50px;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div class="titan-nebula">
                    <div class="nebula-ring-1"></div>
                    <div class="nebula-ring-2"></div>
                    <div class="nebula-core"></div>
                </div>
                <h1 style="font-family: 'Orbitron'; font-size: 3.5rem; font-weight: 900; color: white; margin: 0; text-shadow: 0 0 30px rgba(59, 130, 246, 0.5); line-height: 1;">
                    TITAN <span style="font-family: 'Be Vietnam Pro'; font-weight: 300; font-size: 1.5rem; color: #64748b;">SYSTEM</span>
                </h1>
            </div>
            <p style="font-family: 'Be Vietnam Pro'; font-size: 0.8rem; color: #475569; letter-spacing: 0.4em; margin-top: 10px; text-transform: uppercase;">
                The Next Gen HRM x AI System
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div style='text-align: center; color: #475569; margin-top: 80px; font-size: 0.7rem; font-family: "Be Vietnam Pro"; letter-spacing: 2px;'>
            DESIGNED & BUILT BY NGUYỄN THANH THIỆN
        </div>
    """, unsafe_allow_html=True)
