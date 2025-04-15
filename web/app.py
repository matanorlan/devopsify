from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("http://gateway:5001/api")
    data = response.json()
    return f"<h1>Web says:</h1><p>{data['message']}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
