import streamlit as st

def render_header():
    """
    Header chuẩn 100% giống file HTML: Có hiệu ứng Nebula xoay bên cạnh chữ TITAN.
    """
    st.markdown("""
        <!-- Canvas nền -->
        <canvas id="warp-canvas"></canvas>
        
        <!-- Header Container -->
        <div style="display: flex; flex-direction: column; align-items: flex-start; padding: 2rem; padding-left: 10%; z-index: 20; position: relative;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <!-- TITAN NEBULA ANIMATION -->
                <div class="titan-nebula">
                    <div class="nebula-ring-1"></div>
                    <div class="nebula-ring-2"></div>
                    <div class="nebula-core"></div>
                </div>
                
                <!-- LOGO TEXT -->
                <h1 style="
                    font-family: 'Orbitron', sans-serif;
                    font-size: 3rem;
                    font-weight: 900;
                    letter-spacing: 0.2em;
                    color: white;
                    text-shadow: 0 0 30px rgba(59, 130, 246, 0.3);
                    margin: 0;
                ">
                    TITAN <span style="font-family: 'Be Vietnam Pro', sans-serif; font-weight: 300; font-size: 1.5rem; color: #475569;">SYSTEM</span>
                </h1>
            </div>
            
            <!-- SUBTITLE -->
            <p style="
                font-family: 'Be Vietnam Pro', sans-serif;
                font-size: 0.7rem;
                color: rgba(59, 130, 246, 0.8);
                margin-top: 0.5rem;
                margin-left: 4rem; /* Căn thẳng với chữ TITAN */
                text-transform: uppercase;
                letter-spacing: 0.3em;
                font-weight: 700;
            ">
                The Next Gen HRM v1.9 (Final Prototype)
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div style='text-align: center; color: #475569; margin-top: 100px; font-size: 0.7rem; font-family: "Be Vietnam Pro"; letter-spacing: 2px;'>
            DESIGNED & BUILT BY NGUYỄN THANH THIỆN
        </div>
    """, unsafe_allow_html=True)
