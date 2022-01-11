from flask import Flask, Response
from generate import generate_images, load_model
import torch

app = Flask(__name__)

device = torch.device('cpu')

munch = load_model('https://glupaisa.blob.core.windows.net/glup/munch.pkl',
                   device)
portrait = load_model(
    'https://glupaisa.blob.core.windows.net/glup/portraits18.pkl', device)


@app.route("/", methods=["GET"])
def warmup():
    generate_images(munch, device)
    return "Kunstig is up and running!"


@app.route("/munch", methods=["GET"])
def main():
    img = generate_images(munch, device)
    return Response(img, status=200, mimetype="image/png")


@app.route("/portrait", methods=["GET"])
def portrait():
    img = generate_images(portrait, device)
    return Response(img, status=200, mimetype="image/png")