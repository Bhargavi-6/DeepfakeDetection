# Deepfake Detection Project

## Introduction

This project aims to detect deepfake images and videos using advanced machine learning techniques. The application consists of two parts:
1. A FastAPI backend for processing image and video files.
2. A Streamlit frontend for user interaction and visualization.

## Features

- Upload and analyze image or video for deepfake detection.
- View results and confidence scores.
- Easy-to-use web interface.

## Requirements

- Python 3.9 or higher
- FastAPI
- Uvicorn
- Streamlit
- Other dependencies as listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Bhargavi-6/DeepfakeDetection.git
    cd deepfake-verification
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### Start the FastAPI Backend

1. Start the FastAPI server using Uvicorn:

    ```bash
    uvicorn main:app --reload --port 8000
    ```

### Start the Streamlit Frontend

1. Open a new terminal or command prompt and navigate to the project root directory.

2. Start the Streamlit application:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open your browser and go to `http://localhost:8501` to access the Streamlit interface.
2. Login the application. Enter the credentials and double click the login button.
3. Choose image or video to upload.
4. Upload a image or video file and click the "Upload" button.
5. View the results displayed on the screen.

![App Screenshot](https://raw.githubusercontent.com/Bhargavi-6/DeepfakeDetection/main/static/images/app_screen1.jpg)

![App Screenshot](https://raw.githubusercontent.com/Bhargavi-6/DeepfakeDetection/main/static/images/app_screen2.jpg)

![App Screenshot](https://raw.githubusercontent.com/Bhargavi-6/DeepfakeDetection/main/static/images/app_screen2.jpg)
