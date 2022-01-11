from flask import Flask, Response
from generate import generate_images, load_model
import torch
from flask import request

app = Flask(__name__)

device = torch.device('cpu')

munch_model = load_model(
    'https://glupaisa.blob.core.windows.net/glup/munch.pkl', device)

portrait_model = load_model(
    'https://glupaisa.blob.core.windows.net/glup/portraits18.pkl', device)


@app.route("/", methods=["GET"])
def warmup():
    generate_images(munch, device)
    return "Kunstig is up and running!"


@app.route("/munch", methods=["POST"])
def munch():
    json_data = request.json
    input_string = None

    if json_data:
        input_string = json_data["inputString"]

    img = generate_images(munch_model, device, input_string)
    return Response(img, status=200, mimetype="image/png")


@app.route("/portrait", methods=["POST"])
def portrait():
    json_data = request.json
    input_string = None

    if json_data:
        input_string = json_data["inputString"]

    img = generate_images(portrait_model, device, input_string)
    return Response(img, status=200, mimetype="image/png")