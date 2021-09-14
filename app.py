from flask import Flask, send_file
import os, random

app = Flask(__name__)

@app.route("/generate", methods = ["GET"])
def main():
    seed = random.randint(1, 1000)
    trained_model = './trained_models/network-snapshot-010200.pkl'
    os.system(f'python generate.py --outdir=out/{seed} --trunc=1 --seeds={seed} \
    --network={trained_model}')
    image = random.choice(os.listdir(f'./out/{seed}'))
    return send_file(f'./out/{seed}/{image}', mimetype='image/png')