from email.mime import image
from flask import Flask, Response, jsonify
import gan
import torch
import cms
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import random

from flask import request

app = Flask(__name__)

device = torch.device('cpu')

models_info = {}
loaded_models = {}


# Check CMS each 5 min for new models
def load():
    cms.fetch_models(models_info)
    gan.load_models(models_info, loaded_models, device)


scheduler = BackgroundScheduler()
scheduler.add_job(func=load, trigger="interval", seconds=300)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

load()


@app.route("/", methods=["GET"])
def warmup():
    return "Kunstig is up and running!"


@app.route("/models", methods=["GET"])
def models():

    models = []

    for key, value in models_info.items():
        models.append({
            "name": key,
            "displayName": value["displayName"],
            "description": value.get("description") or ""
        })

    response = jsonify({"models": models})

    return response


@app.route("/model", methods=["POST"])
def model():
    json_data = request.json

    if not json_data or not "model" in json_data:
        return Response("Missing payload", status=400)

    model_name = json_data.get("model")

    if not model_name or not model_name in models_info:
        return Response("Provided model name not found", status=400)

    return jsonify({
        "displayName":
        models_info[model_name].get("displayName"),
        "images":
        models_info[model_name].get("images") or [],
        "description":
        models_info[model_name].get("description") or '',
    })


@app.route("/images", methods=["GET"])
def images():
    images = []

    for key, value in models_info.items():
        images.extend(value.get("images" or []))

    random.shuffle(images)

    response = jsonify({"images": images})

    return response


@app.route("/generate", methods=["POST"])
def generate():
    json_data = request.json

    if not json_data or not "model" in json_data:
        return Response("Missing payload", status=400)

    model_name = json_data.get("model")

    if not model_name or not model_name in models_info:
        return Response("Provided model name not found", status=400)

    input_string = None

    if "inputString" in json_data:
        input_string = json_data.get("inputString")

    img = gan.generate_images(loaded_models.get(model_name), device,
                              input_string)

    return Response(img, status=200, mimetype="image/png")
