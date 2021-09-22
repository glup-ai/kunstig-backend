from flask import Flask, Response
from generate import generate_images

app = Flask(__name__)

@app.route("/munch", methods = ["GET"])
def main():
    trained_model = './trained_models/munch.pkl'
    img = generate_images(network_pkl=trained_model)
    return Response(img, status=200, mimetype="image/png")