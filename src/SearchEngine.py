from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import Input_File as a
import Tab_Sim as b

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

#menginput query melalui keyboard
query = input("Masukkan query: ")

#membersihkan query dan memasukkannya sebagai elemen pertama array clean
stop = stopword.remove(query)
clean[0] = stemmer.stem(stop)

#memasukkan kata unik pada query ke dalam array terms
terms = list(set(clean[0].split()))
nTerm = len(terms)

#membuat tabel frekuensi kemunculan kata pada dokumen dan query yang sesuai dengan terms
tab_frek = [[0 for j in range(nDok+1)] for i in range(nTerm)]
for i in range(nDok+1):
	for j in range(nTerm):
		for k in range(len(clean[i].split())):
			if ((clean[i].split()[k])==terms[j]):
				tab_frek[j][i]+=1

#menyimpan nilai fungsi Tab_Sim dari Tab_Info.py
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

#mengurutkan isi judul dokumen sesuai similarity
Tab_sortedJudul = ['*' for i in range(nDok)]
for i in range(nDok):
    idx = Index_SortedSim[i]
    Tab_sortedJudul[i] = judul[idx]

#mendapatkan kalimat pertama dari dokumen
Tab_FirstSent = ['*' for i in range (nDok)]
for i in range(nDok):
    idx = Index_SortedSim[i]
    Tab_FirstSent[i] = a.s[idx]

#menyimpan gabungan array judul, Tab_countkata, Tab_Sim,Tab_FirstSent ke dalam array tab_info
tab_info = [['*' for j in range(4)] for i in range(nDok)]
for i in range(nDok):
    tab_info[i][0] = judul[i]
    tab_info[i][1] = Tab_countKata[i]
    tab_info[i][2] = round(Tab_Sim[i], 2)
    tab_info[i][3] = Tab_FirstSent[i]

#menyimpan gabungan array terms dan tabel tab_frek ke dalam tabel term_frek
term_frek = [['*' for j in range(nDok+2)] for i in range(nTerm+1)]
term_frek[0][0] = 'Term'
term_frek[0][1] = 'Query'
for i in range (nDok):
    term_frek[0][i+2]=judul[i]
for i in range (nTerm):
    term_frek[i+1][0]=terms[i]
for i in range(nTerm):
    for j in range(nDok+1):
        term_frek[i+1][j+1]=str(tab_frek[i][j])