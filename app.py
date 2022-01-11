from flask import Flask, Response
from generate import generate_images, load_model
import torch

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


@app.route("/munch", methods=["GET"])
def munch():
    img = generate_images(munch_model, device)
    return Response(img, status=200, mimetype="image/png")


@app.route("/portrait", methods=["GET"])
def portrait():
    img = generate_images(portrait_model, device)
    return Response(img, status=200, mimetype="image/png")