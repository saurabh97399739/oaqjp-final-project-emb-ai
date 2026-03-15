from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    dominant_emotion = max(response, key=response.get)

    return f"For the given statement, the system response is anger: {anger}, disgust: {disgust}, fear: {fear}, joy: {joy}, sadness: {sadness}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run()