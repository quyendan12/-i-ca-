import streamlit as st
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cấu hình Cloudinary của bạn
cloudinary.config(
    cloud_name = "dn6rqvvvd",
    api_key = "251922673532191",
    api_secret = "QgjA7S16EqiVazn8qpHxu5cAYQ0",
    secure = True
)

st.set_page_config(page_title="Photo Share", page_icon="📸")
st.title("📸 Web Chia Sẻ Ảnh Đám Mây")

# Giao diện tải ảnh
with st.sidebar:
    st.header("Tải ảnh mới")
    uploaded_file = st.file_uploader("Chọn ảnh từ máy...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        with st.spinner("Đang tải lên..."):
            cloudinary.uploader.upload(uploaded_file)
            st.success("Tải lên thành công!")
            st.rerun()

st.write("---")

# Hiển thị ảnh
try:
    res = cloudinary.api.resources(type="upload", max_results=12)
    images = res.get("resources", [])
    if images:
        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img['secure_url'], use_container_width=True)
    else:
        st.info("Chưa có ảnh nào được chia sẻ.")
except Exception as e:
    st.error(f"Lỗi kết nối Cloudinary: {e}")