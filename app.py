from flask import Flask, Response
from generate import generate_images2

app = Flask(__name__)

@app.route("/munch", methods = ["GET"])
def main():
    trained_model = './trained_models/munch.pkl'
    img = generate_images2(network_pkl=trained_model)
    return Response(img, status=200, mimetype="image/png")

@app.route("/portrait", methods = ["GET"])
def portrait():
    trained_model = './trained_models/portraits18.pkl'
    img = generate_images2(network_pkl=trained_model)
    return Response(img, status=200, mimetype="image/png")