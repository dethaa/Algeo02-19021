from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
#Input file
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()
f = open('dokumen.txt','r')
dokumen = f.read()
stop = stopword.remove(dokumen)
output = stemmer.stem(stop)
print(output)
# di sini algoritma (countKataQuery - KataQueryYangSama), hasilnya a misalnya 
setOutput = set(output)
nTerm = len(setOutput)
print(nTerm)
#tab_Frek
#a = jumlahQuery
#terms  [][]
#query = [][]
if (nTerm!=0):
	for i in range(nTerm):
		for j in range (17):  # asumsi saat ini tabel ada 15 + 1 tabel query
			print(outputs.split()[i])
f.close()