# emotion_detection.py  (Task 2)
import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

def emotion_detector(text_to_analyze: str) -> str:
    """Call Watson EmotionPredict and return the RAW JSON TEXT."""
    payload = {"raw_document": {"text": text_to_analyze}}
    resp = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
    return resp.text  # Task 2 specifically asks for .text (raw JSON string)
