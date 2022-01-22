from email.mime import image
from pyexpat import model
from flask import Flask, Response, jsonify
from flask_cors import CORS, cross_origin
from generate import generate_images, load_model, load_models
import torch
import cms
import threading

from flask import request

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

device = torch.device('cpu')

models_dict = cms.get_models()


# Check CMS each 5 min for new models
def load():
    load_models(models_dict, device)
    threading.Timer(300, load).start()


load()


@app.route("/", methods=["GET"])
def warmup():
    return "Kunstig is up and running!"


@app.route("/models", methods=["GET"])
def models():

    models = []

    for key, value in models_dict.items():
        models.append({"name": key, "displayName": value["displayName"]})

    response = jsonify({"models": models})

    return response


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
