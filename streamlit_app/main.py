import streamlit as st
import requests
import os

# Define FastAPI backend URL
FASTAPI_URL = os.getenv("FASTAPI_URL", "http://127.0.0.1:8000")

# Page title and background styling with solid color
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
            color: #333333;
            padding: 2rem;
        }
        .stButton>button {
            background-color: #fca311;
            color: #ffffff;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: #000000;
        }
        .reportview-container .main .block-container {
            padding: 1rem;
        }
        .title-class {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 1rem;
            border-radius: 10px;
        }
        .header-class {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="title-class">Image Manager</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="header-class">Manage your images effortlessly!</h2>', unsafe_allow_html=True)

# Upload section
st.subheader("Upload Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    response = requests.post(f"{FASTAPI_URL}/upload/", files=files)
    if response.status_code == 200:
        st.success("Image uploaded successfully!")
    else:
        st.error("Failed to upload image. Please try again.")

# Retrieve section
st.subheader("Retrieve Image")
image_id = st.number_input("Enter Image ID to retrieve", min_value=1, step=1)
if st.button("Retrieve Image"):
    if image_id:
        response = requests.get(f"{FASTAPI_URL}/images/{image_id}")
        if response.status_code == 200:
            image_data = response.json()
            st.image(image_data["url"], caption=f"ID: {image_data['id']}, Filename: {image_data['filename']}", use_column_width=True)
        else:
            st.error(f"Failed to retrieve image with ID {image_id}. Image not found.")

# Delete section
st.subheader("Delete Image")
delete_image_id = st.number_input("Enter Image ID to delete", min_value=1, step=1)
if st.button("Delete Image"):
    if delete_image_id:
        delete_response = requests.delete(f"{FASTAPI_URL}/delete/{delete_image_id}")
        if delete_response.status_code == 200:
            st.success(f"Image with ID {delete_image_id} deleted successfully!")
        else:
            st.error(f"Failed to delete image with ID {delete_image_id}. Please try again.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Rhythm Gajera")

# Additional features or sections can be added as per your application's needs
