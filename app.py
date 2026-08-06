import os
from flask import Flask, jsonify, request, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder=".", static_url_path="")

@app.get("/")
def home():
    return send_from_directory(".", "index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message:
        return jsonify({"error": "Message is required."}), 400

    # Safe starter mode: no secret is exposed to the browser.
    # Add your preferred AI provider here using server-side environment variables.
    return jsonify({
        "answer": (
            "Alpha AI received your message. Real model inference is not enabled yet. "
            "Connect a server-side AI provider in app.py using environment variables; "
            "never place an API key in index.html."
        ),
        "mode": "starter"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
