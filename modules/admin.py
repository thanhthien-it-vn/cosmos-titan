import streamlit as st
from utils.database import get_config_all

def render_admin_zone(module_info):
    """Nghiệp vụ chi tiết của Tab 6: Cấu hình hệ thống"""
    st.markdown(f"<h2 style='color:#3b82f6; font-family:Orbitron'>{module_info['name']}</h2>", unsafe_allow_html=True)
    
    st.info("📊 Hệ thống đang truy xuất tham số thực tế từ Singapore...")
    
    # Logic nghiệp vụ nằm gọn tại đây
    configs = get_config_all()
    if configs:
        st.write("### DANH SÁCH THAM SỐ MỀM (CONFIG)")
        st.dataframe(configs, use_container_width=True)
    else:
        st.error("Không thể kết nối dữ liệu. Vui lòng kiểm tra Secrets.")
