import os

from flask import Flask, jsonify, redirect, flash
from flask import request
from werkzeug.utils import secure_filename

from models.emotion_recognition import get_emotions
from models.text_recognition import get_ocr

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/emotion-detection', methods=['POST'])
def emotion_detection():
    return jsonify(get_emotions(request.args.get('text')))


@app.route('/text-recognition', methods=['POST'])
def text_recognition():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    try:
        return get_ocr(request.files)
    finally:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))


@app.route('/similar-recognition', methods=['POST'])
def similar_recognition():
    return ''


if __name__ == '__main__':
    app.run()
