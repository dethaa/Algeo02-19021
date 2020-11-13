from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import Input_File as a
import Tab_Info as b

#fungsi untuk menghapus stopword dari dokumen
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
#fungsi untuk menyederhanakan kata ke bentuk dasar
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

print("################################## MY SIMPLE SEARCH ENGINE ##################################")

#menginput query melalui keyboard
query = input("Masukkan query: ")

#membersihkan query dan memasukkannya sebagai elemen pertama array clean
stop = stopword.remove(query)
a.clean[0] = stemmer.stem(stop)

#memasukkan kata unik pada query ke dalam array terms
terms = list(set(a.clean[0].split()))
nTerm = len(terms)

#membuat tabel frekuensi kemunculan kata pada dokumen dan query yang sesuai dengan terms
tab_frek = [[0 for j in range(a.nDok+1)] for i in range(nTerm)]
for i in range(a.nDok):
	for j in range(nTerm):
		for k in range(len(a.clean[i].split())):
			if ((a.clean[i].split()[k])==terms[j]):
				tab_frek[j][i]+=1

#memanggil fungsi Tab_Sim pada Tab_Info.py dan memasukkannya nilainya ke dalam variabel Tab_Sim
nDok=a.nDok
Tab_Sim=b.Tab_Sim(nTerm,tab_frek,nDok)

#mereturn indeks dari pengurutan tabel similarity
P = sorted(range(len(Tab_Sim)),key=lambda x:Tab_Sim[x],reverse=True)
Index_SortedSim = sorted(range(len(Tab_Sim)),key=lambda x:P[x])

#mengurutkan nilai similiarity dengan memasukkan hasil Tab_Sim ke array sementara
Tab_Sim.sort(reverse = True)

#memasukkan jumlah kata tiap dokumen ke dalam array Tab_countKata sesuai similarity
Tab_countKata = [0 for i in range(nDok)]
for i in range(nDok):
    idx = Index_SortedSim[i]
    Tab_countKata[i]=len(a.d[idx].split())

#Mengurutkan isi judul dokumen sesuai similarity
Tab_sortedJudul = ['*' for i in range(nDok)]
for i in range(nDok):
    idx = Index_SortedSim[i]
    Tab_sortedJudul[i] = a.judul[idx]

#mendapatkan kalimat pertama dari dokumen
Tab_FirstSent = ['*' for i in range (nDok)]
for i in range(nDok):
    idx = Index_SortedSim[i]
    Tab_FirstSent[i] = a.s[idx]

print("Hasil Pencarian:")
for i in range(nDok):
    print(i + 1, ". ", Tab_sortedJudul[i])
    print("Jumlah kata: ", Tab_countKata[i])
    print("Tingkat Kemiripan: ", round(Tab_Sim[i]*100), "%")
    print(Tab_FirstSent[i])
    print(" ")

#menampilkan tabel frekuensi mentah
print(tab_frek)


