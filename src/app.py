from flask import Flask, render_template, flash, request, redirect
from werkzeug.utils import secure_filename
import os

import urllib.request

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/OMEN/OneDrive/Desktop/Tubes2Algeo/uploads'
 
app.secret_key = "Cairocoders-Ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'html'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perihal')
def perihal():
    return render_template('perihal.html')

@app.route("/daftar-dokumen")
def daftar():
    return render_template("daftar.html")

@app.route("/unggah")
def upload():
    return render_template("upload.html")

@app.route('/unggah', methods=['POST'])
def upload_file():
    if request.method == 'POST':
    # check if the post request has the files part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File berhasil diunggah')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)