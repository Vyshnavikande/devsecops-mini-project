from flask import Flask
import os

app = Flask(__name__)

DB_PASSWORD = os.environ.get("DB_PASSWORD", "not_configured")

@app.route("/")
def home():
    return "DevSecOps Mini Project Application is running securely!"

@app.route("/health")
def health():
    return {"status": "UP", "message": "Service is healthy"}

@app.route("/secret-check")
def secret_check():
    if DB_PASSWORD == "not_configured":
        return {"status": "warning", "message": "Secret is not configured"}
    return {"status": "success", "message": "Secret loaded from environment variable"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)