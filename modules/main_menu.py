import streamlit as st
from utils.constants import MODULES

def render_main_menu():
    """
    Vẽ lưới Portal Grid.
    Lưu ý: CSS ở utils/styles.py sẽ tự động biến các nút này thành hình ô gạch 3D.
    """
    
    # Tạo khoảng cách đệm phía trên
    st.write("<div style='height: 50px'></div>", unsafe_allow_html=True)

    # Container giới hạn chiều rộng để giống bản gốc (max-width: 6xl)
    with st.container():
        # Duyệt qua danh sách module
        for i in range(0, len(MODULES), 3):
            cols = st.columns(3)
            chunk = MODULES[i:i+3]
            
            for j, mod in enumerate(chunk):
                with cols[j]:
                    # Nút bấm chỉ chứa Tên, icon sẽ được CSS xử lý hoặc thêm vào sau nếu cần
                    # Để giống bản gốc, ta để icon và text tách dòng
                    label = f"{mod['name']}\n\n." 
                    # Dấu chấm ở dưới là mẹo để nút có đủ chiều cao cho CSS can thiệp, CSS sẽ ẩn nó đi hoặc làm mờ
                    
                    if st.button(mod['name'], key=f"btn_{mod['id']}"):
                        st.session_state.active_tab = mod['id']
                        st.rerun()
            
            st.write("") # Spacer
