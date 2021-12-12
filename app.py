import os

from flask import Flask, jsonify, redirect, flash
from flask import request
from werkzeug.utils import secure_filename

from models.emotion_recognition import get_emotions
from models.text_recognition import get_ocr
from models.text_similarity import find_similarity


UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER))
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = "super secret key"


@app.route('/emotion-detection', methods=['POST'])
def emotion_detection():
    return jsonify(get_emotions(request.args.get('text')))


@app.route('/text-recognition', methods=['POST', 'GET'])
def text_recognition():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        try:
            return get_ocr(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        finally:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ''


@app.route('/similar-recognition', methods=['POST'])
def similar_recognition():
    return str(find_similarity(request.args.get('text1'), request.args.get('text2')))


if __name__ == '__main__':
    app.run()
