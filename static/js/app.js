/* ═══════════════════════════════════════════════════════════
   CropGuard AI — app.js  (fixed)
   Fixes: duplicate capture listener, no error view, camera flow
═══════════════════════════════════════════════════════════ */

"use strict";

// ── State ─────────────────────────────────────────────────────────────────────
const state = {
  currentLang:    "en",
  translations:   {},
  selectedFile:   null,
  capturedBlob:   null,
  cameraStream:   null,
  capturedFrame:  null,
  captureReady:   false,   // moved into state (was a bare variable — caused scope bugs)
};

// ── DOM Refs ──────────────────────────────────────────────────────────────────
const $ = (id) => document.getElementById(id);

const loadingScreen    = $("loading-screen");
const app              = $("app");
const viewUpload       = $("view-upload");
const viewAnalyzing    = $("view-analyzing");
const viewResult       = $("view-result");
const viewUnsupported  = $("view-unsupported");
const viewError        = $("view-error");           // new error view

const dropZone         = $("drop-zone");
const fileInput        = $("file-input");
const previewWrap      = $("preview-wrap");
const previewImg       = $("preview-img");
const uploadPlaceholder = $("upload-placeholder");
const removePreview    = $("remove-preview");

const btnUpload        = $("btn-upload");
const btnCamera        = $("btn-camera");
const btnAnalyze       = $("btn-analyze");
const btnBack          = $("btn-back");
const btnBack2         = $("btn-back-2");
const btnBackError     = $("btn-back-error");       // error view back button
const langToggle       = $("lang-toggle");
const langLabel        = $("lang-label");

const cameraPanel      = $("camera-panel");
const cameraClose      = $("camera-close");
const cameraVideo      = $("camera-video");
const cameraCanvas     = $("camera-canvas");
const btnCapture       = $("btn-capture");
const btnRetake        = $("btn-retake");


// ═══════════════════════════════════════════════════════════
// PHASE 9: Loading Screen + App Initialization
// ═══════════════════════════════════════════════════════════
async function init() {
  await loadTranslations();
  await sleep(2200);
  loadingScreen.classList.add("fade-out");
  app.classList.remove("hidden");
  setTimeout(() => loadingScreen.style.display = "none", 650);
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }


// ═══════════════════════════════════════════════════════════
// PHASE 8: Translations (EN ↔ Hindi)
// ═══════════════════════════════════════════════════════════
async function loadTranslations() {
  try {
    const res = await fetch("/translations");
    state.translations = await res.json();
    applyTranslations(state.currentLang);
  } catch (e) {
    console.warn("Could not load translations:", e);
  }
}

function applyTranslations(lang) {
  const t = state.translations[lang] || {};
  document.querySelectorAll("[data-key]").forEach(el => {
    const key = el.dataset.key;
    if (t[key]) el.textContent = t[key];
  });
}

function toggleLanguage() {
  state.currentLang = state.currentLang === "en" ? "hi" : "en";
  langLabel.textContent = state.currentLang === "en" ? "हिं" : "EN";
  applyTranslations(state.currentLang);
  document.documentElement.lang = state.currentLang === "hi" ? "hi" : "en";

  // If we are currently showing a result, refresh the dynamic content
  if (!viewResult.classList.contains("hidden") && viewResult.classList.contains("active")) {
    // We need to store the last result data somewhere
    // For simplicity, you can re-analyze or store lastResult globally
  }
}

// ═══════════════════════════════════════════════════════════
// PHASE 2: Image Upload (File + Drag & Drop)
// ═══════════════════════════════════════════════════════════
function setImagePreview(src) {
  previewImg.src = src;
  previewWrap.style.display = "block";
  uploadPlaceholder.style.display = "none";
  btnAnalyze.disabled = false;
}

function clearImagePreview() {
  previewImg.src = "";
  previewWrap.style.display = "none";
  uploadPlaceholder.style.display = "flex";
  btnAnalyze.disabled = true;
  state.selectedFile  = null;
  state.capturedBlob  = null;
  state.capturedFrame = null;
  fileInput.value     = "";
}

dropZone.addEventListener("click", (e) => {
  if (e.target === removePreview || removePreview.contains(e.target)) return;
  fileInput.click();
});

btnUpload.addEventListener("click", () => fileInput.click());

fileInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  if (!file) return;
  if (!file.type.startsWith("image/")) { showToast("Please select an image file."); return; }
  state.selectedFile  = file;
  state.capturedBlob  = null;
  const reader = new FileReader();
  reader.onload = (ev) => setImagePreview(ev.target.result);
  reader.readAsDataURL(file);
});

removePreview.addEventListener("click", (e) => {
  e.stopPropagation();
  clearImagePreview();
});

dropZone.addEventListener("dragover",  (e) => { e.preventDefault(); dropZone.classList.add("drag-over"); });
dropZone.addEventListener("dragleave", ()  => dropZone.classList.remove("drag-over"));
dropZone.addEventListener("drop", (e) => {
  e.preventDefault();
  dropZone.classList.remove("drag-over");
  const file = e.dataTransfer.files[0];
  if (!file || !file.type.startsWith("image/")) { showToast("Please drop an image file."); return; }
  state.selectedFile  = file;
  state.capturedBlob  = null;
  const reader = new FileReader();
  reader.onload = (ev) => setImagePreview(ev.target.result);
  reader.readAsDataURL(file);
});


// ═══════════════════════════════════════════════════════════
// PHASE 7: Camera Integration (WebRTC)
// BUG FIX: Removed duplicate btnCapture listeners.
//          Original code added 3 separate listeners to btnCapture,
//          causing the capture/use logic to fire multiple times.
//          Now: ONE listener, state machine via state.captureReady.
// ═══════════════════════════════════════════════════════════
btnCamera.addEventListener("click", openCamera);
cameraClose.addEventListener("click", closeCamera);
cameraPanel.addEventListener("click", (e) => { if (e.target === cameraPanel) closeCamera(); });

async function openCamera() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    showToast("Camera not supported in this browser.");
    return;
  }
  try {
    state.cameraStream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: { ideal: "environment" }, width: { ideal: 1280 } }
    });
    cameraVideo.srcObject = state.cameraStream;
    cameraVideo.style.display = "block";
    cameraCanvas.style.display = "none";
    btnCapture.classList.remove("hidden");
    btnRetake.classList.add("hidden");

    // Reset capture state
    state.captureReady = false;
    const t = state.translations[state.currentLang] || {};
    btnCapture.textContent = t["capture_btn"] || "Capture";

    cameraPanel.classList.remove("hidden");
  } catch (err) {
    showToast("Camera access denied or unavailable.");
    console.error("Camera error:", err);
  }
}

function closeCamera() {
  if (state.cameraStream) {
    state.cameraStream.getTracks().forEach(t => t.stop());
    state.cameraStream = null;
  }
  cameraPanel.classList.add("hidden");
  state.captureReady = false;
}

// SINGLE capture listener — replaces the 3 conflicting originals
btnCapture.addEventListener("click", () => {
  if (!state.captureReady) {
    // First click: take the snapshot
    const w = cameraVideo.videoWidth;
    const h = cameraVideo.videoHeight;
    cameraCanvas.width  = w;
    cameraCanvas.height = h;
    cameraCanvas.getContext("2d").drawImage(cameraVideo, 0, 0, w, h);

    cameraVideo.style.display  = "none";
    cameraCanvas.style.display = "block";
    btnRetake.classList.remove("hidden");

    state.capturedFrame = cameraCanvas.toDataURL("image/jpeg", 0.92);

    // Convert dataURL → Blob
    fetch(state.capturedFrame)
      .then(r => r.blob())
      .then(blob => { state.capturedBlob = blob; });

    // Update button to "Use Photo"
    state.captureReady = true;
    const t = state.translations[state.currentLang] || {};
    btnCapture.textContent = t["use_photo"] || "Use Photo";

  } else {
    // Second click: use the captured image
    if (state.capturedFrame) {
      setImagePreview(state.capturedFrame);
    }
    closeCamera();
  }
});

btnRetake.addEventListener("click", () => {
  cameraVideo.style.display  = "block";
  cameraCanvas.style.display = "none";
  btnCapture.classList.remove("hidden");
  btnRetake.classList.add("hidden");

  state.capturedFrame = null;
  state.capturedBlob  = null;
  state.captureReady  = false;

  const t = state.translations[state.currentLang] || {};
  btnCapture.textContent = t["capture_btn"] || "Capture";
});


// ═══════════════════════════════════════════════════════════
// PHASE 3–5: Predict API call + Result Display
// ═══════════════════════════════════════════════════════════
btnAnalyze.addEventListener("click", analyzeImage);

// ═══════════════════════════════════════════════════════════
// PHASE 3–5: Predict API call + Result Display (UPDATED FOR HINDI)
// ═══════════════════════════════════════════════════════════

async function analyzeImage() {
  if (!previewImg.src && !state.capturedBlob) return;

  const imagePreviewSrc = previewImg.src;
  showView("analyzing");

  try {
    let resultData;
    const formData = new FormData();

    if (state.selectedFile) {
      formData.append("image", state.selectedFile);
    } else if (state.capturedBlob) {
      formData.append("image", state.capturedBlob, "camera_capture.jpg");
    } else {
      showToast("No image selected.");
      showView("upload");
      return;
    }

    const res = await fetch("/predict", { method: "POST", body: formData });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      const msg = errData.error || `Server error ${res.status}`;
      showErrorView(msg, imagePreviewSrc);
      return;
    }

    resultData = await res.json();

    if (resultData.error) {
      showErrorView(resultData.error, imagePreviewSrc);
      return;
    }

    if (!resultData.supported) {
      showUnsupportedView(resultData, imagePreviewSrc);
    } else {
      showResultView(resultData, imagePreviewSrc);
    }

  } catch (err) {
    console.error("Predict error:", err);
    showErrorView("Network error. Please check your connection and try again.", null);
  }
}

function showResultView(data, imageSrc) {
  $("result-img").src = imageSrc;
  $("res-crop").textContent = data.crop || "—";

  // Crop Confidence
  const cropConf = data.crop_confidence || 0;
  $("confidence-fill").style.width = cropConf + "%";
  $("confidence-pct").textContent = cropConf + "%";

  $("res-disease-conf").textContent = (data.disease_confidence || 0) + "%";

  // Severity badge class
  const sevBadge = $("severity-badge");
  const sev = data.severity || "unknown";
  sevBadge.className = `sev-badge severity-${sev}`;

  // Use the new function
  updateResultContent(data);

  // Re-apply static translations
  applyTranslations(state.currentLang);
  showView("result");
}

function showUnsupportedView(data, imageSrc) {
  $("res-unsupported-crop").textContent =
    `Detected: "${(data.crop || "unknown").toUpperCase()}" (${data.crop_confidence || 0}% confidence)`;
  applyTranslations(state.currentLang);
  showView("unsupported");
}
function updateResultContent(data) {
  const isHindi = state.currentLang === "hi";

  // Disease name
  const diseaseName = isHindi 
    ? (data.display_name_hi || data.display_name || "—")
    : (data.display_name || "—");
  $("res-disease").textContent = diseaseName;

  // Dynamic fields
  if (isHindi) {
    $("res-symptoms").textContent       = data.symptoms_hi       || "—";
    $("res-causes").textContent         = data.causes_hi         || "—";
    $("res-recommendation").textContent = data.recommendation_hi || "—";
  } else {
    $("res-symptoms").textContent       = data.symptoms       || "—";
    $("res-causes").textContent         = data.causes         || "—";
    $("res-recommendation").textContent = data.recommendation || "—";
  }

  // Severity (already handled with map, but make sure it's refreshed)
  const sevBadge = $("severity-badge");
  const sev = data.severity || "unknown";
  const severityMap = isHindi ? {
    "none":     "कोई नहीं — स्वस्थ",
    "mild":     "हल्का",
    "moderate": "मध्यम",
    "severe":   "गंभीर",
    "unknown":  "अज्ञात"
  } : {
    "none":     "None — Healthy",
    "mild":     "Mild",
    "moderate": "Moderate",
    "severe":   "Severe",
    "unknown":  "Unknown"
  };
  sevBadge.textContent = severityMap[sev] || sev;
}
// New: dedicated error view instead of just a toast
function showErrorView(message, imageSrc) {
  $("error-message").textContent = message || "An unexpected error occurred.";

  // Show the analyzed image in the error view if we have it
  const errImg = $("error-img");
  if (imageSrc && errImg) {
    errImg.src = imageSrc;
    errImg.style.display = "block";
  } else if (errImg) {
    errImg.style.display = "none";
  }

  // Add diagnostic tip based on the error message
  const tip = $("error-tip");
  if (tip) {
    if (message.includes("model") || message.includes("loaded")) {
      tip.textContent = "💡 The AI model file may be missing. Check that all .keras files are in the models/ directory.";
    } else if (message.includes("class") || message.includes("index") || message.includes("mismatch")) {
      tip.textContent = "💡 Class list mismatch detected. Verify the disease class names in ml_pipeline.py match the model's training order.";
    } else if (message.includes("Network") || message.includes("connection")) {
      tip.textContent = "💡 Check your internet connection and that the Flask server is running on port 5000.";
    } else if (message.includes("empty") || message.includes("corrupt")) {
      tip.textContent = "💡 The image file may be corrupt. Try a different image.";
    } else {
      tip.textContent = "💡 Try a clearer, well-lit photo of a single leaf against a plain background.";
    }
  }

  showView("error");
}


// ═══════════════════════════════════════════════════════════
// View Management
// ═══════════════════════════════════════════════════════════
function showView(name) {
  const views = {
    upload:      viewUpload,
    analyzing:   viewAnalyzing,
    result:      viewResult,
    unsupported: viewUnsupported,
    error:       viewError,
  };
  Object.values(views).forEach(v => { if (v) v.classList.remove("active"); });
  if (views[name]) views[name].classList.add("active");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

btnBack.addEventListener("click",      resetToUpload);
btnBack2.addEventListener("click",     resetToUpload);
if (btnBackError) btnBackError.addEventListener("click", resetToUpload);

function resetToUpload() {
  clearImagePreview();
  showView("upload");
}

langToggle.addEventListener("click", toggleLanguage);


// ── Toast Notification ────────────────────────────────────
function showToast(msg) {
  const existing = document.querySelector(".toast");
  if (existing) existing.remove();

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = msg;
  toast.style.cssText = `
    position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
    background: var(--green-900); color: white;
    padding: 12px 20px; border-radius: 12px;
    font-family: 'DM Sans', sans-serif; font-size: 0.875rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    z-index: 9999; animation: slide-up 0.3s ease;
    max-width: 90%; text-align: center;
  `;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}


// ── Kick off ──────────────────────────────────────────────
init();