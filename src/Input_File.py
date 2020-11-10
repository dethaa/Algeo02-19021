from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

#fungsi untuk menghapus stopword dari dokumen
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
#fungsi untuk menyederhanakan kata ke bentuk dasar
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

#menginput file
f1 = open('d1.txt', 'r')
f2 = open('d2.txt', 'r')
f3 = open('d3.txt', 'r')
f4 = open('d4.txt', 'r')
f5 = open('d5.txt', 'r')
f6 = open('d6.txt', 'r')
f7 = open('d7.txt', 'r')
f8 = open('d8.txt', 'r')
f9 = open('d9.txt', 'r')
f10 = open('d10.txt', 'r')

#deklarasi array
d = ['*' for i in range(10)] #menyimpan dokumen asli
stop = ['*' for i in range(10)] #menyimpan hasil penghapusan stopword
clean =['*' for i in range(11)] #menyimpan hasil pembersihan dokumen (stopword + stemming)

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

#traversal untuk "pembersihan" dokumen
for i in range(10):
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