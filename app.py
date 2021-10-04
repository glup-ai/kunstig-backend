from flask import Flask, Response
from generate import generate_images

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def warmup():
    return "Kunstig is up and running!"

@app.route("/munch", methods = ["GET"])
def main():
    trained_model = 'https://glupaisa.blob.core.windows.net/glup/munch.pkl'
    img = generate_images(network_pkl=trained_model)
    return Response(img, status=200, mimetype="image/png")