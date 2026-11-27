from flask import Flask
import socket
import os

THIS_IS_BROKEN_CODE

app = Flask(__name__)

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
