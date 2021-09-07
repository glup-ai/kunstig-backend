from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def main():
    name = request.args.get("name")
    if not name:
        return Response("Please input your name.", status=400)
    return Response(f"Hello, {name}. This Flask application executed successfully!", status=200)