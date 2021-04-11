from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

## This will run the file locally when executed directly.
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
