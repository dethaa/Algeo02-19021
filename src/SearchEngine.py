# FILE MAIN
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import Input_File as IF
import Tab_Frekuensi as TF 
import Tab_Info as TI


print("################################## MY SIMPLE SEARCH ENGINE ##################################")
print("Hasil Pencarian:")
for jumlahDoc in range (15):
	print(jumlahDoc+1)
	print("Jumlah kata: ", TI.Tab_countKata[jumlahDoc])
	print("Tingkat Kemiripan: ", TI.Tab_Sim[jumlahDoc])
	print("<Kalimat pertama dari Dokumen ", TI.Index_SortedSim[jumlahDoc], " >")
#print Tabel Frekuensi mentah
print(TF.tab_frek)