"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the application home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the input text and return the detected emotions.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"

    return (
        "Para la declaración dada, la respuesta del sistema es "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} y "
        f"'sadness': {response['sadness']}. "
        f"La emoción dominante es {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    