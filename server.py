"""Flask web for Emotion Detection (Task 6–7)."""
from flask import Flask, jsonify, render_template, request
# import the function you exposed in EmotionDetection/__init__.py
from EmotionDetection import emotion_detector

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.get("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_endpoint():
    """Accept GET (from mywebscript.js) and POST (manual/curl)"""
    text = ""
    if request.method == "GET":
        # mywebscript.js sends ?textToAnalyze=...
        text = (request.args.get("textToAnalyze") or request.args.get("text") or "").strip()
    else:
        if request.is_json:
            data = request.get_json(silent=True) or {}
            text = (data.get("textToAnalyze") or data.get("text") or "").strip()
        if not text:  # form-encoded fallback
            text = (request.form.get("textToAnalyze") or request.form.get("text") or "").strip()

    if not text:
        return jsonify(error="Text is required."), 400

    result = emotion_detector(text)
    return jsonify(result), 200


@app.errorhandler(404)
def not_found(_e):
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    # Keep port 5000 for the lab
    app.run(host="0.0.0.0", port=5000, debug=True)
