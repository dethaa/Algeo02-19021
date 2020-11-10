from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
#Input file
factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()
factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()
f = open('iniAsumsiInputUsernya.txt','r')
inputan = f.read()
stop = stopword.remove(inputan)
outputInput = stemmer.stem(stop)

#buatDokumen
f = open('dokumen.txt', 'r')
dokumen = f.read()
stopWDokumen = stopword.remove(dokumen)
outputDokumen = stemmer.stem(stopWDokumen)
X = outputDokumen.split()
strDok = list(X)
print(strDok)
print(len(strDok))

#buat Input sementara

kata_Unik = set(outputInput.split())
strs = list(kata_Unik)
nTerm = len(strs)

terms = ['*' for i in range(nTerm)]
iTerms = 0
queryDocs = [[0 for j in range(17)] for i in range(nTerm)]
for row in range (17):
	for column in range (nTerm):
		
print(iTerms)

f.close()