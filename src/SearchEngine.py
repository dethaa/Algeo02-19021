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
kata_Unik = set(outputInput.split())
strs = list(kata_Unik)
nTerm = len(strs)
print(strs[0])
terms = ['*' for i in range(nTerm)]
matriksQDoc = [[0 for j in range(15)] for i in range(nTerm)]
for row in range (nTerm):
	terms[row] = strs[row]
print(terms)
f.close()