from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import Input_File as a

#fungsi untuk menghapus stopword dari dokumen
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
#fungsi untuk menyederhanakan kata ke bentuk dasar
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

#menginput query melalui keyboard
query = input("Masukkan query: ")

#membersihkan query dan memasukkannya sebagai elemen pertama array clean
stop = stopword.remove(query)
a.clean[0] = stemmer.stem(stop)

#memasukkan kata unik pada query ke dalam array terms
terms = list(set(a.clean[0].split()))
nTerm = len(terms)

#membuat tabel frekuensi kemunculan kata pada dokumen dan query yang sesuai dengan terms
tab_frek = [[0 for j in range(16)] for i in range(nTerm)]
for i in range(16):
	for j in range(nTerm):
		for k in range(len(a.clean[i].split())):
			if ((a.clean[i].split()[k])==terms[j]):
				tab_frek[j][i]+=1

