# 🌿 CropGuard AI — Plant Disease Detection System

A production-ready Flask web app for detecting crop diseases using a two-stage deep learning pipeline.

---

## Project Structure

```
project/
├── app.py                     # Flask app (Phases 1–5, API)
├── requirements.txt
├── models/                    # Place your .keras models here
│   ├── crop_classification.keras
│   ├── potato.keras
│   ├── tomato.keras
│   ├── strawberry.keras
│   ├── grapes.keras
│   ├── banana.keras
│   └── mango.keras
├── static/
│   ├── css/style.css          # Full production UI styles
│   └── js/app.js              # All client-side logic
├── templates/
│   └── index.html             # Single-page app template
└── utils/
    ├── __init__.py
    ├── ml_pipeline.py         # Model loading, caching, prediction
    └── disease_data.py        # Disease info DB + translations
```

---

## Setup & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Place model files

Copy all `.keras` model files into the `models/` directory:

```
models/crop_classification.keras   ← from crop_classification.ipynb output
models/potato.keras                ← from crop_disease_classification.py output
models/tomato.keras
models/strawberry.keras
models/grapes.keras
models/banana.keras
models/mango.keras
```

> **Note:** The app runs in **demo mode** if models are not present.
> It will still show the full UI with mock predictions.

### 3. Start the server

```bash
cd project/
python app.py
```

Open: http://localhost:5000

---

## API Reference

### POST /predict

**Input (multipart/form-data):**
```
image: <image file>  (PNG, JPG, JPEG, WEBP — max 16MB)
```

**Input (JSON — camera capture):**
```json
{ "image_b64": "data:image/jpeg;base64,..." }
```

**Output:**
```json
{
  "supported": true,
  "crop": "Tomato",
  "crop_confidence": 94.3,
  "disease": "Tomato___Early_blight",
  "disease_confidence": 87.1,
  "display_name": "Early Blight",
  "symptoms": "Concentric ring spots...",
  "causes": "Fungus Alternaria solani...",
  "recommendation": "Apply chlorothalonil...",
  "severity": "moderate"
}
```

**If unsupported crop:**
```json
{
  "supported": false,
  "crop": "wheat",
  "crop_confidence": 88.2,
  ...rest null
}
```

### GET /health

```json
{
  "status": "ok",
  "crop_classifier": true,
  "disease_models_loaded": ["potato", "tomato", "strawberry", "grapes", "banana", "mango"]
}
```

---

## Phase Testing Checklist

### ✅ Phase 1 — Project Setup & Basic Flask
```bash
python app.py
# Expected: Server starts on port 5000, no errors
curl http://localhost:5000/
# Expected: 200 OK, HTML response
```

### ✅ Phase 2 — Image Upload API
```bash
# Test with curl
curl -X POST http://localhost:5000/predict \
  -F "image=@/path/to/test_leaf.jpg"
# Expected: JSON with prediction or demo response
```

### ✅ Phase 3 — Crop Classifier
```bash
curl http://localhost:5000/health
# Expected: crop_classifier: true (if model file exists)
```

### ✅ Phase 4 — Multi-Model Routing
- Upload a tomato leaf → should load tomato disease model
- Upload unsupported crop → `"supported": false` in response

### ✅ Phase 5 — Disease Info Mapping
```bash
curl -X POST http://localhost:5000/predict -F "image=@tomato_leaf.jpg"
# Expected: Full JSON with symptoms, causes, recommendation, severity
```

### ✅ Phase 6 — Frontend UI
- Open http://localhost:5000
- Upload image → result shows crop, disease, all info cards

### ✅ Phase 7 — Camera Integration
- Click "Use Camera" → browser asks for permission
- Capture frame → preview shown → Analyze works

### ✅ Phase 8 — Language Toggle
- Click हिं button in header → all UI text switches to Hindi
- Click EN → switches back → no layout breaks

### ✅ Phase 9 — UX Enhancements
- Loading screen appears on startup (2 seconds)
- Back button returns to upload view
- Smooth transitions between views

### ✅ Phase 10 — Disclaimer
- Visible on every result page (amber warning box)

---

## Model Class Name Expectations

The ML pipeline uses these class name arrays (must match training order):

**Crop classifier:** `["banana", "grapes", "mango", "potato", "strawberry", "tomato"]`

**Disease models:**
- `potato`: `[Early_blight, Late_blight, healthy]`
- `tomato`: `[Bacterial_spot, Early_blight, Late_blight, Leaf_Mold, Septoria_leaf_spot, Spider_mites, Target_Spot, Yellow_Leaf_Curl_Virus, mosaic_virus, healthy]`
- `strawberry`: `[Leaf_scorch, healthy]`
- `grapes`: `[Black_rot, Esca, Leaf_blight, healthy]`
- `banana`: `[Cordana, Pestalotiopsis, Sigatoka, healthy]`
- `mango`: `[Anthracnose, Die_Back, Powdery_Mildew, Sooty_Mould, healthy]`

If your models have different class orders, update `_class_names` in `utils/ml_pipeline.py`.

---

## Key Architecture Decisions

| Concern | Solution |
|---|---|
| Model reload per request | `load_all_models()` called ONCE at startup, cached in module globals |
| Camera images | Sent as `multipart/form-data` blob (same as file upload) |
| Translation | JSON served via `/translations`, applied by `data-key` attributes |
| Error handling | Try/catch at every level, `demo mode` if models missing |
| Security | File extension validation, 16MB limit, no path traversal |
