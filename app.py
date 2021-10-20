from flask import Flask, Response
from generate import generate_images

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def warmup():
    #generate_images(network_pkl='https://glupaisa.blob.core.windows.net/glup/munch.pkl')
    generate_images(network_pkl='https://glupaisa.blob.core.windows.net/glup/portraits18.pkl')
    return "Kunstig is up and running!"

@app.route("/munch", methods = ["GET"])
def main():
    trained_model = 'https://glupaisa.blob.core.windows.net/glup/munch.pkl'
    img = generate_images(network_pkl=trained_model)
    return Response(img, status=200, mimetype="image/png")

@app.route("/portrait", methods = ["GET"])
def portrait():
    trained_model = 'https://glupaisa.blob.core.windows.net/glup/portraits18.pkl'
    img = generate_images(network_pkl=trained_model)
    return Response(img, status=200, mimetype="image/png")