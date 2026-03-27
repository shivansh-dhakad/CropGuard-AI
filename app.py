# app.py  —  CropGuard AI Flask Application
# Phase 1–10 fully implemented

import os
import logging
import base64
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

# ── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s"
)
logger = logging.getLogger(__name__)

# ── Flask App ─────────────────────────────────────────────────────────────────
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024   # 16 MB max upload
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "cropguard-dev-key-change-in-prod")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Load Models Once at Startup ───────────────────────────────────────────────
from utils.ml_pipeline import load_all_models, run_full_pipeline
from utils.disease_data import TRANSLATIONS

logger.info("Starting CropGuard AI — loading models...")
load_all_models()
logger.info("Model initialization complete. Flask ready.")


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Home page — Phase 1"""
    return render_template("index.html")


@app.route("/translations")
def get_translations():
    """Serve translation strings — Phase 8"""
    return jsonify(TRANSLATIONS)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        image_bytes = None
        
        # ── Path A: File Upload ────────────────────────────────────────────
        if "image" in request.files:
            file = request.files["image"]
            if file.filename == "":
                return jsonify({"error": "No file selected"}), 400
            if not allowed_file(file.filename):
                return jsonify({"error": "File type not allowed. Use PNG, JPG, JPEG, WEBP."}), 400
            image_bytes = file.read()
            logger.info(f"Received uploaded file: {secure_filename(file.filename)}, size: {len(image_bytes)} bytes")

        # ── Path B: Base64 from Camera ─────────────────────────────────────
        elif request.is_json and "image_b64" in request.get_json():
            data = request.get_json()["image_b64"]
            # Strip data URL prefix if present
            if "," in data:
                data = data.split(",", 1)[1]
            image_bytes = base64.b64decode(data)
            logger.info(f"Received camera capture, size: {len(image_bytes)} bytes")

        else:
            return jsonify({"error": "No image provided. Send 'image' file or 'image_b64' JSON."}), 400

        # ── Validate image is non-empty ────────────────────────────────────
        if len(image_bytes) < 100:
            return jsonify({"error": "Image file appears to be empty or corrupt."}), 400

        # ── Run ML Pipeline ────────────────────────────────────────────────
        result = run_full_pipeline(image_bytes)
        logger.info(f"Prediction result: crop={result.get('crop')}, disease={result.get('disease')}")
        return jsonify(result)

    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500


@app.route("/health")
def health():
    """Health check endpoint for testing"""
    from utils.ml_pipeline import _crop_classifier, _disease_models
    return jsonify({
        "status": "ok",
        "crop_classifier": _crop_classifier is not None,
        "disease_models_loaded": list(_disease_models.keys()),
    })


# ── Error Handlers ─────────────────────────────────────────────────────────────
@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large. Maximum size is 16MB."}), 413

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error."}), 500


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
