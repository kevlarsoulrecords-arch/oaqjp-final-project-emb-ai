# emotion_detection.py  (Task 7)
import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

def emotion_detector(text_to_analyze: str) -> dict:
    """Call Watson Emotion model and return formatted dict with dominant emotion.
       If the service returns 400 (blank/invalid input), return all Nones."""
    payload = {"raw_document": {"text": text_to_analyze}}

    # Make the call
    try:
        resp = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
    except requests.RequestException:
        # Network or transport error -> treat like invalid
        return {
            "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None,
            "dominant_emotion": None,
        }

    # Task 7 requirement: use status_code to detect blank/invalid input
    if resp.status_code == 400:
        return {
            "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None,
            "dominant_emotion": None,
        }

    resp.raise_for_status()
    data = resp.json()  # Watson returns JSON

    emo = data["emotionPredictions"][0]["emotion"]
    out = {
        "anger": float(emo.get("anger", 0.0)),
        "disgust": float(emo.get("disgust", 0.0)),
        "fear": float(emo.get("fear", 0.0)),
        "joy": float(emo.get("joy", 0.0)),
        "sadness": float(emo.get("sadness", 0.0)),
    }
    out["dominant_emotion"] = max(out, key=out.get)
    return out
