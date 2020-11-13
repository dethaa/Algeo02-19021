import os.path
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

#fungsi untuk menghapus stopword dari dokumen
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
#fungsi untuk menyederhanakan kata ke bentuk dasar
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

#fungsi untuk menghitung jumlah dokumen yang ada dalam folder uploads
nDok = len(os.listdir("../test/"))
#melist setiap dokumen yang ada di folder test
file_list = os.listdir("../test/")
#deklarasi array
d = ['*' for i in range(nDok)] #menyimpan dokumen asli
judul = ['*' for i in range(nDok)] #menyimpan judul dokumen
stop = ['*' for i in range(nDok)] #menyimpan hasil penghapusan stopword
clean =['*' for i in range(nDok+1)] #menyimpan hasil pembersihan dokumen (stopword + stemming)
s = ['*' for i in range(nDok)] #menyimpan kalimat pertama dokumen

#menyimpan isi dokumen ke dalam array d
j=0
for file in file_list:
    with open(os.path.join("../test/", file),'r', encoding='utf-8') as src_file:
        d[j] = src_file.read()
        j+=1

#menyimpan judul dokumen ke dalam array judul
for i in range(nDok):
    judul[i]=(os.path.splitext(file_list[i])[0])

#traversal untuk "pembersihan" dokumen
for i in range(nDok):
    stop[i] = stopword.remove(d[i])
    clean[i+1] = stemmer.stem(stop[i])

#menyimpan kalimat pertama tiap file
for i in range(nDok):
	s[i] = d[i].partition('.')[0] + '.'