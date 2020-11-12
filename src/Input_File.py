from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

#fungsi untuk menghapus stopword dari dokumen
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
#fungsi untuk menyederhanakan kata ke bentuk dasar
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

#fungsi untuk menghitung jumlah dokumen yang ada dalam folder uploads
nDok = len(os.listdir("uploads/"))

#menginput file
f1 = open('uploads/d1.txt', 'r', encoding='utf-8')
f2 = open('uploads/d2.txt', 'r', encoding='utf-8')
f3 = open('uploads/d3.txt', 'r', encoding='utf-8')
f4 = open('uploads/d4.txt', 'r', encoding='utf-8')
f5 = open('uploads/d5.txt', 'r', encoding='utf-8')
f6 = open('uploads/d6.txt', 'r', encoding='utf-8')
f7 = open('uploads/d7.txt', 'r', encoding='utf-8')
f8 = open('uploads/d8.txt', 'r', encoding='utf-8')
f9 = open('uploads/d9.txt', 'r', encoding='utf-8')
f10 = open('uploads/d10.txt', 'r', encoding='utf-8')
f11 = open('uploads/d11.txt', 'r', encoding='utf-8')
f12 = open('uploads/d12.txt', 'r', encoding='utf-8')
f13 = open('uploads/d13.txt', 'r', encoding='utf-8')
f14 = open('uploads/d14.txt', 'r', encoding='utf-8')
f15 = open('uploads/d15.txt', 'r', encoding='utf-8')

#deklarasi array
judul = ['*' for i in range(nDok)]
d = ['*' for i in range(nDok)] #menyimpan dokumen asli
stop = ['*' for i in range(nDok)] #menyimpan hasil penghapusan stopword
clean =['*' for i in range(nDok+1)] #menyimpan hasil pembersihan dokumen (stopword + stemming)
s = ['*' for i in range(nDok)] #menyimpan kalimat pertama dokumen

#menyimpan judul dokumen ke dalam array judul
judul[0] = 'Satu Hikmah Terpenting yang Bisa Kita Ambil dari Pandemi Covid-19'
judul[1] = 'Tiga Hal yang Bisa Kamu Lakukan Saat Social Distancing'
judul[2] = 'Tujuh Hal yang Bisa Dilakukan Brand Lewat Konten di Saat Krisis Covid-19'
judul[3] = 'Analisis Pola Komunikasi Masyarakat di Twitter selama Pandemi COVID-19'
judul[4] = 'Bagaimana Adaptasi Pelajar dan Para Pengajar di Masa Pandemi Covid-19'
judul[5] = 'COVID-19: Kita Dalam Bahaya'
judul[6] = 'Dampak Pandemi COVID-19 Pada Berbagai Sektor Bisnis'
judul[7] = 'Dampak Pandemi COVID-19: Perjuangan Pendidikan Indonesia'
judul[8] = 'Dampak Platform Digital dan Perannya Selama Pandemi COVID-19 pada Pemasaran Produk di Indonesia'
judul[9] = 'Pandemi Covid-19: Tanggap Darurat Dunia Kesehatan Global'
judul[10] = 'Pangan di Tengah Pandemi Covid-19'
judul[11] = 'Pembelajaran Jarak Jauh; Peran dan Hikmah Teknologi bagi Masyarakat Pembelajar di Era Pandemi COVID-19'
judul[12] = 'Pendidikan Indonesia di Tengah Pandemi Covid-19'
judul[13] = 'Perubahan Perilaku Belanja Konsumen Indonesia Saat Covid-19'
judul[14] = 'Solusi Untuk Medapatkan Penghasilan Tambahan Selama Pandemi Covid-19'

#menyimpan pembacaan dokumen ke dalam array d
d[0] = f1.read()
d[1] = f2.read()
d[2] = f3.read()
d[3] = f4.read()
d[4] = f5.read()
d[5] = f6.read()
d[6] = f7.read()
d[7] = f8.read()
d[8] = f9.read()
d[9] = f10.read()
d[10] = f11.read()
d[11] = f12.read()
d[12] = f13.read()
d[13] = f14.read()
d[14] = f15.read()

#menyimpan kalimat pertama tiap file
s[0] = d[0].partition('.')[0] + '.'
s[1] = d[1].partition('.')[0] + '.'
s[2] = d[2].partition('.')[0] + '.'
s[3] = d[3].partition('.')[0] + '.'
s[4] = d[4].partition('.')[0] + '.'
s[5] = d[5].partition('.')[0] + '.'
s[6] = d[6].partition('.')[0] + '.'
s[7] = d[7].partition('.')[0] + '.'
s[8] = d[8].partition('.')[0] + '.'
s[9] = d[9].partition('.')[0] + '.'
s[10] = d[10].partition('.')[0] + '.'
s[11] = d[11].partition('.')[0] + '.'
s[12] = d[12].partition('.')[0] + '.'
s[13] = d[13].partition('.')[0] + '.'
s[14] = d[14].partition('.')[0] + '.'

#traversal untuk "pembersihan" dokumen
for i in range(nDok):
    stop[i] = stopword.remove(d[i])
    clean[i+1] = stemmer.stem(stop[i])

#menutup file
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()
f13.close()
f14.close()
f15.close()