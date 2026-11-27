from flask import Flask
import socket
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

VERSION = "8"

@app.route("/")
def home():
    hostname = socket.gethostname()

    current_release = os.path.realpath(
        os.path.dirname(__file__)
    )

    return (
        f"Employee Portal "
        f"Version {VERSION} "
        f"| Host: {hostname} "
        f"| Release: {current_release}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
