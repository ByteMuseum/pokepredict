from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import os
import time
import random

IMG_HEIGHT = 80
IMG_WIDTH = 128
API_TOKENS = [
    "dfe45447ce53c9c1b632c3d20cc1883028bf162413114962f7b05f81cf0f4c84",
    "c5113cc8b5e4c5aa7f9cc36e1d9ae2c6f38a65657a64b0db4823424e3f2512c9",
    "def99c0071be80980c422822205aac3fbfa20580ef60dfe2a29ca787e7038921",
]


def get_prediction(img):
    img = tf.keras.utils.load_img(img, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    prediction = class_names[np.argmax(score)]
    return jsonify({"prediction": prediction})


model = tf.keras.models.load_model("pokemon.keras")
class_names = np.load("classnames.npy")
app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to PokePredict"})


@app.route("/predict", methods=["POST"])
def predict():
    if request.headers.get("auth") in API_TOKENS:
        if request.files:
            img = request.files["image"]
            if not img:
                return jsonify({"error": "No image provided"})
            filename = f"temp_{time.time()}{random.randint(0, 1000)}.jpg"
            img.save(filename)
            pred = get_prediction(filename)
            os.remove(filename)
            return pred
        else:
            return jsonify({"error": "No image provided"})
    else:
        return jsonify({"error": "Invalid API Token"})


if __name__ == "__main__":
    app.run(port=5443, host="0.0.0.0")
