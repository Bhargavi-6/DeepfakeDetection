import numpy as np
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import model.video_inference as videoinference
import model.image_inference as imageinference
import os

app = FastAPI()

# Create directories for images and videos
os.makedirs('uploads/images', exist_ok=True)
os.makedirs('uploads/videos', exist_ok=True)


@app.post("/upload/image/")
async def upload_image(file: UploadFile = File(...), name: str = Form(...)):
    file_location = f"uploads/images/{name}"
    print(file_location)
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    # Predict the uploaded image
    message = imageinference.predict_image(file_location)

    return JSONResponse(content={"message": message})


@app.post("/upload/video/")
async def upload_video(file: UploadFile = File(...), name: str = Form(...)):
    file_location = f"uploads/videos/{name}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    print(file_location)
    # Perform prediction
    prediction = videoinference.sequence_prediction(file_location)

    score = np.round_(prediction[0]*100)

    predicted_class = 'Fake' if prediction[0] <= 0.50 else 'Real'

    return JSONResponse(content={"message": f'{predicted_class} with Confidence {score}%'})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
