import tensorflow as tf
import os
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained model
#image_model = tf.keras.models.load_model('model/cnn_deepfake_image.h5')
def load_model():
    # Load JSON model architecture
    with open('model/model.json', 'r') as json_file:
        loaded_model_json = json_file.read()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)

    # Load weights into the model
    loaded_model.load_weights("model/model.weights.h5")
    return loaded_model

image_model=load_model()

# Configure upload folder and allowed file extensions
IMAGE_UPLOAD_FOLDER = 'uploads/images'
IMAGE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(IMAGE_UPLOAD_FOLDER, exist_ok=True)


def image_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGE_ALLOWED_EXTENSIONS


def predict_image(filepath):
    img = image.load_img(filepath)

    img_tensor = image.img_to_array(img)
    img_tensor = tf.image.resize(img_tensor, (224, 224))
    img_tensor = tf.expand_dims(img_tensor, axis=0)

    # Indicate classifying before prediction
    predicted = image_model.predict(img_tensor)

    predicted_class = "Fake" if predicted[0, 0] > 0.50 else "Real"

    score = round(predicted[0, 0]*100)

    if predicted_class == 'Real':
        score = 100 - score

    return f'{predicted_class} with Confidence {score}%'
