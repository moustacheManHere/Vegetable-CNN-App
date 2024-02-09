import numpy as np
from PIL import Image
import requests
import json 
from application import app
import os

def preprocess(image_path,size):
    try:
        image_path = os.path.join("application/static/uploads", image_path)
        image = Image.open(image_path).convert("RGB")
        image = image.convert("L")
        image = image.resize((size, size))  
        image_array = np.array(image)[:, :, np.newaxis] / 255.0  # Normalize pixel values to [0, 1]
        return [image_array.tolist()]
    except Exception as e:
        print("Error during preprocessing:", e)
        return None


def get_response(url, img_array):
    headers = {"Content-Type": "application/json"}
    input_data = {"instances": img_array}
    json_data = json.dumps(input_data)
    try:
        response = requests.post(url, data=json_data, headers=headers)
        prediction_results = response.json()
        if "error" in prediction_results.keys():
            return None
        predictions = np.array(prediction_results["predictions"])
        predicted_label = np.argmax(predictions)
        predicted_probs = predictions.tolist()[0][predicted_label]
        return (predicted_label, predicted_probs*100)
    except Exception as e:
        print(e)
        return None
    
def get_prediction(image_path, size):
    if size not in [31, 128]:
        size = 31
    img_array = preprocess(image_path, size)
    if img_array is None:
        return None
    if size == 31:
        url = app.config["DL_URL_SMALL"]
    else:
        url = app.config["DL_URL_LARGE"]
    response = get_response(url + ":predict", img_array)
    return response