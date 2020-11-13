from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

import urllib.request

import Input_File as a
import Tab_Info as TI
import Tab_Frekuensi as TF

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

@app.route('/', methods=['POST','GET'])
def search():
    if request.method == 'POST':
        user = request.form['query']
    else :
        user = request.args.get('query')
    return redirect(url_for("search_query", que=user))

@app.route('/<que>')
def search_query(que):
    for i in range(15):
        flash(str(i + 1)+ '. '+ TI.Tab_sortedJudul[i])
        flash('Jumlah kata: '+ str(TI.Tab_countKata[i]))
        flash('Tingkat Kemiripan: '+ str(round(TI.Tab_Sim[i]*100))+ '%')
        flash(TI.Tab_FirstSent[i])
        flash('')
    return render_template('index.html')

@app.route('/perihal')
def perihal():
    return render_template('perihal.html')

@app.route("/daftar-dokumen")
def daftar():
    for i in range(15):
        flash(str(i+1)+'. '+a.judul[i])
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
    return redirect('/unggah')

if __name__ == "__main__":
    app.run(debug=True)