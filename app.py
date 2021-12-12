from flask import Flask, jsonify
from flask import request
from models.emotion_recognition import get_prediction


app = Flask(__name__)


@app.route('/emotion-detection', methods=['POST'])
def emotion_detection():
    return jsonify(get_prediction(request.args.get('text')))


@app.route('/text-recognition', methods=['POST'])
def text_recognition():
    return ''


@app.route('/similar-recognition', methods=['POST'])
def similar_recognition():
    return ''


if __name__ == '__main__':
    app.run()
