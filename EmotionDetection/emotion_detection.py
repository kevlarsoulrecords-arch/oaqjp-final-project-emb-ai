# emotion_detection.py  (Task 3)
import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

def emotion_detector(text_to_analyze: str) -> dict:
    """Call Watson Emotion model and return formatted dict with dominant emotion."""
    payload = {"raw_document": {"text": text_to_analyze}}
    resp = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()  # Watson returns JSON

    # Extract scores (model returns a list with one prediction object)
    emo = data["emotionPredictions"][0]["emotion"]

    out = {
        "anger":   float(emo.get("anger", 0)),
        "disgust": float(emo.get("disgust", 0)),
        "fear":    float(emo.get("fear", 0)),
        "joy":     float(emo.get("joy", 0)),
        "sadness": float(emo.get("sadness", 0)),
    }
    out["dominant_emotion"] = max(out, key=out.get)
    return out
