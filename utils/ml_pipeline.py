# utils/ml_pipeline.py
# Fixed version - March 2026

import os
import numpy as np
import logging
from PIL import Image
import io

logger = logging.getLogger(__name__)

# ── Constants ─────────────────────────────────────────────────────────────────
IMAGE_SIZE = (224, 224)

# Crop classifier output → disease model file mapping
CROP_MODEL_MAP = {
    "potato":     "potato.keras",
    "tomato":     "tomato.keras",
    "strawberry": "strawberry.keras",
    "grapes":     "grapes.keras",
    "banana":     "banana.keras",
    "mango":      "mango.keras",
}

# Normalize crop name from classifier output to display name
CROP_NORMALIZE = {
    "banana":     "Banana",
    "grapes":     "Grape",
    "mango":      "Mango",
    "potato":     "Potato",
    "strawberry": "Strawberry",
    "tomato":     "Tomato",
}

SUPPORTED_CROPS = set(CROP_MODEL_MAP.keys())


# ── Model Cache ───────────────────────────────────────────────────────────────
_crop_classifier = None
_disease_models  = {}
_class_names     = {}


def get_models_dir():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")


def load_all_models():
    global _crop_classifier, _disease_models, _class_names

    try:
        import tensorflow as tf
        models_dir = get_models_dir()

        # ── Crop Classifier ──────────────────────────────────────────────────
        crop_model_path = os.path.join(models_dir, "crop_classification.keras")
        if os.path.exists(crop_model_path):
            logger.info(f"Loading crop classifier: {crop_model_path}")
            _crop_classifier = tf.keras.models.load_model(crop_model_path)
            crop_json = os.path.join(models_dir, "crop_classification_classes.json")

            if not os.path.exists(crop_json):
                raise FileNotFoundError("Missing crop_classes.json")

            import json
            with open(crop_json, "r") as f:
                _class_names["crop"] = json.load(f)
            logger.info(f"✅ Crop classifier loaded. Classes: {_class_names['crop']}")
        else:
            logger.warning(f"⚠️ Crop classifier NOT found at {crop_model_path}")

        # ── Disease Models ───────────────────────────────────────────────────
        
        

        for crop, model_file in CROP_MODEL_MAP.items():
            model_path = os.path.join(models_dir, model_file)
            json_path  = os.path.join(models_dir, f"{crop}_classes.json")

            if os.path.exists(model_path):
                logger.info(f"Loading disease model: {model_path}")
                _disease_models[crop] = tf.keras.models.load_model(model_path)

                # Load class names from JSON
                if not os.path.exists(json_path):
                    raise FileNotFoundError(f"Missing class file: {json_path}")

                import json
                with open(json_path, "r") as f:
                    _class_names[crop] = json.load(f)

                logger.info(f"✅ {crop} model loaded. Classes: {_class_names[crop]}")
            else:
                logger.warning(f"⚠️ Disease model NOT found: {model_path}")

    except ImportError:
        logger.error("TensorFlow is not installed. Run: pip install tensorflow")
    except Exception as e:
        logger.error(f"Fatal error loading models: {e}", exc_info=True)


def preprocess_image(image_bytes):
    """Important: Do NOT divide by 255 because Rescaling layer is inside the model"""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMAGE_SIZE, Image.LANCZOS)
    arr = np.array(img, dtype=np.float32)          # No /255 here
    return np.expand_dims(arr, axis=0)


def predict_crop(image_bytes):
    if _crop_classifier is None:
        raise RuntimeError("Crop classifier model not loaded.")

    img_array = preprocess_image(image_bytes)
    preds = _crop_classifier.predict(img_array, verbose=0)[0]

    # Optional debug (you can comment this later)
    print("\n=== CROP PREDICTION DEBUG ===")
    class_list = _class_names["crop"]
    for i, name in enumerate(class_list):
        print(f"{name:12} : {preds[i]:.4f} ({preds[i]*100:6.2f}%)")
    print(f"Predicted: {class_list[np.argmax(preds)]} with {max(preds)*100:.2f}% confidence\n")

    idx = int(np.argmax(preds))
    confidence = float(preds[idx])
    crop = class_list[idx]

    logger.info(f"Crop prediction: {crop} ({confidence:.2%})")
    return crop, confidence


def predict_disease(crop, image_bytes):
    if crop not in SUPPORTED_CROPS:
        raise ValueError(f"Crop '{crop}' is not supported.")

    if crop not in _disease_models:
        raise RuntimeError(f"Disease model for '{crop}' not loaded.")
    img_array = preprocess_image(image_bytes)
    model = _disease_models[crop]
    
    preds = model.predict(img_array, verbose=0)[0]   # This should now return 9 values for tomato

    if len(preds) != len(_class_names[crop]):
        raise ValueError(
            f"Mismatch: model outputs {len(preds)} but class_names has {len(_class_names[crop])}"
        )
    idx = int(np.argmax(preds))
    confidence = float(preds[idx])
    raw_class = _class_names[crop][idx]

    normalized = (
        raw_class.strip()
        .replace(" ", "_")
        .replace("-", "_")
    )

    if "___" in normalized:
        disease = normalized
    else:
        disease = f"{crop.capitalize()}___{normalized}"
    # Safe logging
    scores = { _class_names[crop][i]: round(float(preds[i]), 3) 
              for i in range(len(preds)) }

    logger.info(f"Disease prediction for {crop}: {disease} ({confidence:.2%}) | scores: {scores}")
    
    return disease, confidence


def run_full_pipeline(image_bytes):
    from utils.disease_data import DISEASE_INFO

    crop, crop_conf = predict_crop(image_bytes)

    if crop not in SUPPORTED_CROPS:
        return {
            "supported": False,
            "crop": crop,
            "crop_confidence": round(crop_conf * 100, 1),
            "disease": None,
            "disease_confidence": None,
            "display_name": None,
            "symptoms": None,
            "causes": None,
            "recommendation": None,
            "severity": None,
        }

    disease, disease_conf = predict_disease(crop, image_bytes)

    info = DISEASE_INFO.get(disease, {
        "display_name": disease.replace("___", " — ").replace("_", " "),
        "display_name_hi": disease.replace("___", " — ").replace("_", " "),

        "symptoms": "Information not available.",
        "symptoms_hi": "जानकारी उपलब्ध नहीं है।",

        "causes": "Information not available.",
        "causes_hi": "जानकारी उपलब्ध नहीं है।",

        "recommendation": "Consult a local agricultural extension office.",
        "recommendation_hi": "कृपया कृषि विशेषज्ञ से सलाह लें।",

        "severity": "unknown"
    })

    display_crop = CROP_NORMALIZE.get(crop, crop.capitalize())

    return {
        "supported": True,
        "crop": display_crop,
        "crop_confidence": round(crop_conf * 100, 1),
        "disease": disease,
        "disease_confidence": round(disease_conf * 100, 1),

        # EN
        "display_name": info["display_name"],
        "symptoms": info["symptoms"],
        "causes": info["causes"],
        "recommendation": info["recommendation"],

        # (HI)
        "display_name_hi": info.get("display_name_hi"),
        "symptoms_hi": info.get("symptoms_hi"),
        "causes_hi": info.get("causes_hi"),
        "recommendation_hi": info.get("recommendation_hi"),

        "severity": info.get("severity", "unknown"),
    }