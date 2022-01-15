from email.mime import image
from pyexpat import model
from flask import Flask, Response, jsonify
from generate import generate_images, load_model
import torch
from flask import request

app = Flask(__name__)

device = torch.device('cpu')

models_dict = {
    "munch": {
        "displayName": "Munch",
        "url": "https://glupaisa.blob.core.windows.net/glup/munch.pkl",
        "model": None,
        "images": ["test/test_image1.jpg", "test/test_image2.jpg"]
    },
    "portrait": {
        "displayName": "Portrait",
        "url": "https://glupaisa.blob.core.windows.net/glup/portraits18.pkl",
        "model": None,
        "images": ["test/test_image1.jpg", "test/test_image2.jpg"]
    },
}

for key in models_dict:
    models_dict[key]["model"] = load_model(models_dict[key]["url"], device)


@app.route("/", methods=["GET"])
def warmup():
    return "Kunstig is up and running!"


@app.route("/models", methods=["GET"])
def models():

    models = []

    for key, value in models_dict.items():
        models.append({"name": key, "displayName": value["displayName"]})

    return jsonify({"models": models})


@app.route("/model", methods=["POST"])
def model():
    json_data = request.json

    if not json_data or not "model" in json_data:
        return Response("Missing payload", status=400)

    model_name = json_data["model"]

    if not model_name or not model_name in models_dict:
        return Response("Provided model name not found", status=400)

    return jsonify({
        "displayName": models_dict[model_name]["displayName"],
        "images": models_dict[model_name]["images"]
    })


@app.route("/generate", methods=["POST"])
def generate():
    json_data = request.json

    if not json_data or not "model" in json_data:
        return Response("Missing payload", status=400)

    model_name = json_data["model"]

    if not model_name or not model_name in models_dict:
        return Response("Provided model name not found", status=400)

    input_string = None

    if "inputString" in json_data:
        input_string = json_data["inputString"]

    img = generate_images(models_dict[model_name]["model"], device,
                          input_string)

    return Response(img, status=200, mimetype="image/png")
