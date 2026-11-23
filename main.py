
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Tarunya running this application from docker file.!"

if __name__ == "__main__":
    # 0.0.0.0 is required so the app is accessible outside the container
    app.run(host="0.0.0.0", port=5000)

