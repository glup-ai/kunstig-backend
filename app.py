from flask import Flask, send_file
import os, random

app = Flask(__name__)

@app.route("/munch", methods = ["GET"])
def main():
    seed = random.randint(1, 1000)
    # TODO: Find a way to do this less costly
    trained_model = './trained_models/munch.pkl'
    os.system(f'python generate.py --outdir=out/{seed} --trunc=1 --seeds={seed} \
    --network={trained_model}')
    # TODO: Return image directly, don't store it
    image = random.choice(os.listdir(f'./out/{seed}'))
    return send_file(f'./out/{seed}/{image}', mimetype='image/png')