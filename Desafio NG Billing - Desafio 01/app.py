from flask import Flask, jsonify
import os

app = Flask(__name__)
DIRECTORY = "/data"

@app.route("/files", methods=["GET"])
def list_files():
    try:
        files = os.listdir(DIRECTORY)
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)