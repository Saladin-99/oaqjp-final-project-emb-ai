from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detect():
    text_to_analyse = request.args.get('textToAnalyze')    
    try:
        result = emotion_detector(text_to_analyse)
        if not result['dominant_emotion']:
            return "Invalid text! Please try again!"
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text
    except Exception as e:
        return f"Error occurred: {str(e)}"
if __name__ == '__main__':
    app.run(debug=True)