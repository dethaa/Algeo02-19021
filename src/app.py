from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import os
import urllib.request
import Input_File as a
import Tab_Sim as b
import Web_Scraping as c

app = Flask(__name__)

#directory penyimpanan file yang akan diupload
UPLOAD_FOLDER = '../test/'
 
#pengaturan untuk file upload yang akan diterima
app.secret_key = "Cairocoders-Ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'html'])

#menyimpan nilai atribut dari Input_File.py
nDok=a.nDok
clean=a.clean
judul=a.judul

#fungsi untuk menghapus stopword dari dokumen
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
#fungsi untuk menyederhanakan kata ke bentuk dasar
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

#fungsi untuk memastikan file yang diupload sudah sesuai aturan (ekstensi dan ukuran)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#fungsi untuk menampilkan utama dari search engine
@app.route('/')
def index():
    return render_template('index.html')

#fungsi yang akan menerima masukan query yang akan dicari dan langsung menuju def search_query
@app.route('/', methods=['POST','GET'])
def search():
    if request.method == 'POST':
        user = request.form['query']   
    else :
        user = request.args.get('query')
    return redirect(url_for("search_query", query=user))

#fungsi yang memproses masukan query dan mengurutkan dokumen yang relevan
@app.route('/<query>')
def search_query(query):
    #membersihkan query dan memasukkannya sebagai elemen pertama array clean
    stop = stopword.remove(query)
    clean[0] = stemmer.stem(stop)

    #memasukkan kata unik pada query ke dalam array terms
    terms = list(set(clean[0].split()))
    #menyimpan banyaknya jumlah term ke dalam nTerm
    nTerm = len(terms)

    #membuat tabel frekuensi kemunculan kata pada dokumen dan query yang sesuai dengan term
    tab_frek = [[0 for j in range(nDok+1)] for i in range(nTerm)]
    for i in range(nDok+1):
	    for j in range(nTerm):
		    for k in range(len(clean[i].split())):
			    if ((clean[i].split()[k])==terms[j]):
				    tab_frek[j][i]+=1

    #menyimpan nilai fungsi tab_sim dari Tab_Sim.py
    tab_sim=b.tab_sim(nTerm,tab_frek,nDok)

    #menyimpan indeks dari pengurutan tabel similarity
    Index_SortedSim = sorted(range(len(tab_sim)),key=lambda x:tab_sim[x],reverse=True)

    # mengurutkan nilai similiarity dengan memasukkan hasil tab_sim ke array sementara
    tab_sim.sort(reverse=True)

    #memasukkan jumlah kata tiap dokumen ke dalam array Tab_countKata sesuai urutan similarity
    Tab_countKata = [0 for i in range(nDok)]
    for i in range(nDok):
        idx = Index_SortedSim[i]
        Tab_countKata[i]=len(a.d[idx].split())

    #mengurutkan judul dokumen sesuai similarity
    Tab_sortedJudul = ['*' for i in range(nDok)]
    JudulFix = ['*' for i in range (nDok)]
    for i in range(nDok):
        idx = Index_SortedSim[i]
        Tab_sortedJudul[i] = judul[idx]
        JudulFix[i]=Tab_sortedJudul[i].replace('_',' ')

    #mendapatkan kalimat pertama dari dokumen yang sudah terurut
    Tab_FirstSent = ['*' for i in range (nDok)]
    for i in range(nDok):
        idx = Index_SortedSim[i]
        Tab_FirstSent[i] = a.s[idx]

    #menyimpan gabungan array judul, Tab_countKata, tab_sim, Tab_FirstSent ke dalam array tab_info
    tab_info = [['*' for j in range(4)] for i in range(nDok)]
    for i in range(nDok):
        tab_info[i][0] = JudulFix[i]
        tab_info[i][1] = Tab_countKata[i]
        tab_info[i][2] = format(tab_sim[i]*100, '.2f')
        tab_info[i][3] = Tab_FirstSent[i]

    #menyimpan gabungan array terms dan tabel tab_frek ke dalam tabel term_frek
    term_frek = [['*' for j in range(nDok+2)] for i in range(nTerm+1)]
    JudulFix = ['*' for i in range (nDok)]
    term_frek[0][0] = 'Term'
    term_frek[0][1] = 'Query'
    for i in range (nDok):
        JudulFix[i]=judul[i].replace('_',' ')
        term_frek[0][i+2]=JudulFix[i]
    for i in range (nTerm):
        term_frek[i+1][0]=terms[i]
    for i in range(nTerm):
        for j in range(nDok+1):
            term_frek[i+1][j+1]=str(tab_frek[i][j])

    return render_template('index.html',data=tab_info,tab=term_frek)

#fungsi yang akan menampilkan informasi tentang program dan pembuatnya dalam tab perihal
@app.route('/perihal')
def perihal():
    return render_template('perihal.html')

#fungsi yang akan menampilkan halaman upload menggunakan url dari internet yang akan diunduh ke dalam folder test 
@app.route('/pranala')
def pranala():
    return render_template('pranala.html')

#fungsi yang menerima dan memroses url yang dimasukkan pengguna dan meletakkannya dalam folder test
@app.route('/pranala', methods=['POST','GET'])
def ambil_pranala():
    if request.method == 'POST':
        link = request.form['url']
        flash('File berhasil diunduh')
    c.web_scrap(link)
    return redirect('/pranala')

#fungsi yang akan menampilkan daftar dokumen yang tersedia pada folder test
@app.route("/daftar-dokumen")
def daftar():
    JudulFix = ['*' for i in range (nDok)]

    for i in range (nDok) :
        JudulFix[i]=judul[i].replace('_',' ')

    return render_template("daftar.html", title=JudulFix)

#fungsi untuk menuju hyperlink dari judul dokumen yang ada pada hasil pencarian dan membuka dokumen yang dituju
@app.route("/test/<file>")
def buka_file(file):
    return send_from_directory('../test/',file)

#fungsi untuk menampilkan halaman untuk mengunggah file dari dalam komputer sendiri
@app.route("/unggah")
def upload():
    return render_template("upload.html")

#fungsi yang menerima file yang diunggah dan menampilkan keberhasilan pengunggahan
@app.route('/unggah', methods=['POST'])
def upload_file():
    if request.method == 'POST':
    #mengecek apakah files yang dimaksud tersedia
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

#fungsi main yang akan menjalankan program secara keseluruhan
if __name__ == "__main__":
    app.run(debug=True)