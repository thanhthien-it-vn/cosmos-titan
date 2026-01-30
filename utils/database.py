import streamlit as st
from supabase import create_client, Client
from decimal import Decimal, getcontext

# Thiết lập độ chính xác cho tính toán tài chính (28 chữ số thập phân là chuẩn kế toán)
getcontext().prec = 28

@st.cache_resource
def init_connection() -> Client:
    """Khởi tạo kết nối duy nhất tới Supabase Singapore"""
    try:
        # Hút chìa khóa từ két sắt bảo mật GitHub Secrets hoặc Streamlit Secrets
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"⚠️ Lỗi kết nối Database: {e}")
        return None

def get_config_all():
    """Lấy toàn bộ tham số 'mềm', chuyển đổi sang Decimal để đảm bảo chính xác tuyệt đối"""
    supabase = init_connection()
    if supabase:
        response = supabase.table("sys_config").select("*").execute()
        data = response.data
        # Ép kiểu giá trị số sang Decimal ngay tại nguồn để tránh sai số lũy kế
        for item in data:
            if item['config_value'] is not None:
                item['config_value'] = Decimal(str(item['config_value']))
        return data
    return []

def get_config_value(key_name: str):
    """Lấy một giá trị cụ thể và trả về định dạng Decimal chuyên dụng cho kế toán"""
    supabase = init_connection()
    if supabase:
        response = supabase.table("sys_config").select("config_value").eq("config_key", key_name).execute()
        if response.data:
            val = response.data[0]['config_value']
            # Chuyển sang chuỗi trước khi sang Decimal để loại bỏ hoàn toàn sai số nhị phân
            return Decimal(str(val)) if val is not None else Decimal('0')
    return Decimal('0')
