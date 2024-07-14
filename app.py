import streamlit as st
import requests
from dotenv import load_dotenv
import os
import base64

st.set_page_config(page_title="Deepfake Detection")

# Load environment variables from .env file
load_dotenv('config/config.env')

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Set background image
def set_bg_login(image_url):
    st.markdown(
        f"""
        <style>
        .st-emotion-cache-12fmjuu {{
            top: -110px;
        }}
        .stDeployButton {{
            visibility: hidden;
        }}
        .stApp {{
            background-image: url("data:image/png;base64,{image_url}");
            background-size: cover;
        }}
        .st-emotion-cache-1n76uvr{{
            left: -475px;
            bottom: -300px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Set background image
def set_bg(image_url):
    st.markdown(
        f"""
        <style>
        .st-emotion-cache-12fmjuu {{
            top: -110px;
        }}
        .stDeployButton {{
            visibility: hidden;
        }}
        .stApp {{
            background-image: url("data:image/png;base64,{image_url}");
            background-size: cover;
        }}
        .st-emotion-cache-1n76uvr{{
            left: -550px;
            bottom: -100px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Render the login page
def render_login_page():
    img = get_img_as_base64("static/images/Login_final.jpg")
    set_bg_login(img)
    #st.markdown(f"<p style='font-size:50px; color:white;'>Login</p>",unsafe_allow_html=True)
    username = st.text_input("", placeholder="Enter your username")
    password = st.text_input("", type="password", placeholder="Enter your password")
    # Custom CSS to style the button
    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: #ad9c00; /* Change this to your desired color */
            color: white;
            padding: 10px 24px; /* Adjust padding for desired width */
            font-size: 16px;
            border: none;
            border-radius: 4px;
            width: 100%; /* Set width to 100% for full width button */
            cursor: pointer; /* Change cursor to pointer on hover */
        }
        .stButton > button:hover {
            background-color: #45a049; /* Darker green background on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    login_button = st.button("Login")
    return username, password, login_button


# Authenticate user
def authenticate(username, password):
    stored_username = os.getenv('STREAMLIT_USERNAME')
    stored_password = os.getenv('STREAMLIT_PASSWORD')

    print(username, password)
    print(stored_username, stored_password)

    if username == stored_username and password == stored_password:
        st.session_state.logged_in = True
        return True
    else:
        return False


# Render the upload page
def render_upload_page():
    img = get_img_as_base64("static/images/action_final.jpg")
    set_bg(img)

    # Custom CSS to style the button
    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: #ad9c00; /* Change this to your desired color */
            color: white;
            padding: 10px 24px; /* Adjust padding for desired width */
            font-size: 16px;
            border: none;
            border-radius: 4px;
            width: 100%; /* Set width to 100% for full width button */
            cursor: pointer; /* Change cursor to pointer on hover */
        }
        .stButton > button:hover {
            background-color: #45a049; /* Darker green background on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    #st.markdown(f"<p style='font-size:20px; color:white;'>Choose what you want to upload</p>",unsafe_allow_html=True)
    upload_choice = st.selectbox("", ["Image", "Video"], key="custom-selectbox")
    if upload_choice == "Image":
        #st.markdown(f"<p style='font-size:20px; color:white;'>Upload an image</p>",unsafe_allow_html=True)
        image_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
        if image_file:
            if st.button("Upload Image"):
                data = {
                    "name": image_file.name
                }
                files = {"file": image_file.getvalue()}
                response = requests.post("http://127.0.0.1:8000/upload/image/", files=files, data=data)
                if response.status_code == 200:
                    st.markdown(f"<p style='font-size:50px; color:green; font-weight: bold;'>{response.json()['message']}</p>",
                                unsafe_allow_html=True)
                    st.image(image_file)
                else:
                    st.error("Failed to upload image")
    elif upload_choice == "Video":
        video_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi", "gif"])
        if video_file:
            if st.button("Upload Video"):
                data = {
                    "name": video_file.name
                }
                files = {"file": video_file.getvalue()}
                response = requests.post("http://127.0.0.1:8000/upload/video/", files=files, data=data)
                if response.status_code == 200:
                    st.markdown(f"<p style='font-size:50px; color:green; font-weight: bold;'>{response.json()['message']}</p>",
                                unsafe_allow_html=True)
                    st.video(video_file)
                else:
                    st.error("Failed to upload video")


def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        username, password, login_button = render_login_page()
        if login_button:
            if authenticate(username, password):
                st.success("Login successful")
            else:
                st.error("Invalid username or password")
    else:
        render_upload_page()


if __name__ == "__main__":
    main()
