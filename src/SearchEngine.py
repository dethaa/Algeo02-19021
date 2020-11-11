# FILE MAIN
import Tab_Frekuensi as TF
import Tab_Info as TI

print("################################## MY SIMPLE SEARCH ENGINE ##################################")
print("Hasil Pencarian:")
for i in range(15):
    print(i + 1, ". ", TI.Tab_sortedJudul[i])
    print("Jumlah kata: ", TI.Tab_countKata[i])
    print("Tingkat Kemiripan: ", round(TI.Tab_Sim[i]*100), "%")
    print(TI.Tab_FirstSent[i])
    print(" ")
# print Tabel Frekuensi mentah
print(TF.tab_frek)