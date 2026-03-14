from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

METADATA_URL = "http://metadata.google.internal/computeMetadata/v1"
HEADERS = {"Metadata-Flavor": "Google"}

def get_metadata(path):
    return requests.get(f"{METADATA_URL}/{path}", headers=HEADERS).text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metadata")
def metadata():
    data = {
        "instance_name": get_metadata("instance/name"),
        "zone": get_metadata("instance/zone").split("/")[-1],
        "private_ip": get_metadata("instance/network-interfaces/0/ip"),
        "project_id": get_metadata("project/project-id"),
        "network": get_metadata("instance/network-interfaces/0/network").split("/")[-1],
    }

    return render_template("metadata.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
