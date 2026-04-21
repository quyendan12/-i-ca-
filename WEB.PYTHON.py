import streamlit as st
import cloudinary
import cloudinary.uploader
import cloudinary.api

# C?u hình Cloudinary c?a b?n
cloudinary.config(
    cloud_name = "dn6rqvvvd",
    api_key = "251922673532191",
    api_secret = "QgjA7S16EqiVazn8qpHxu5cAYQ0",
    secure = True
)

st.set_page_config(page_title="Photo Share", page_icon="??")
st.title("?? Web Chia S? ?nh ?ám Mây")

# Giao di?n t?i ?nh
with st.sidebar:
    st.header("T?i ?nh m?i")
    uploaded_file = st.file_uploader("Ch?n ?nh t? máy...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        with st.spinner("?ang t?i lên..."):
            cloudinary.uploader.upload(uploaded_file)
            st.success("T?i lên thành công!")
            st.rerun()

st.write("---")

# Hi?n th? ?nh
try:
    res = cloudinary.api.resources(type="upload", max_results=12)
    images = res.get("resources", [])
    if images:
        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img['secure_url'], use_container_width=True)
    else:
        st.info("Ch?a có ?nh nào ???c chia s?.")
except Exception as e:
    st.error(f"L?i k?t n?i Cloudinary: {e}")