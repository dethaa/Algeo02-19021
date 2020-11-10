import Input_File as a
import Tab_Frekuensi as b

def similiarity(d):
    #menghitung similiarity dari dokumen ke-d dengan query
    if (norm(d)==0):
        return 0
    else:
        return(kalidot(d)/(norm(0)*norm(d)))

def norm(d):
    #menghitung normal dari vektor dokumen d
    sum=0
    for i in range(0,b.nTerm):
        sum+=(b.tab_frek[i][d]**2)
    return(sum**0.5)

def kalidot(d):
    #mengembalikan hasil perkalian dot antara vektor dokumen ke-d dengan query
    sum=0
    for i in range(0,b.nTerm):
        sum+=(b.tab_frek[i][0]*b.tab_frek[i][d])
    return(sum)

#memasukkan nilai similiarity dokumen dengan query ke dalam array Tab_Sim
Tab_Sim=[0 for i in range(15)]
for i in range(15):
    Tab_Sim[i]=similiarity(i+1)

#mereturn indeks dari pengurutan tabel similarity
P = sorted(range(len(Tab_Sim)),key=lambda x:Tab_Sim[x],reverse=True)
Index_SortedSim = sorted(range(len(Tab_Sim)),key=lambda x:P[x])

#mengurutkan nilai similiarity dengan memasukkan hasil Tab_Sim ke array sementara
Tab_Sim.sort(reverse = True)

#memasukkan jumlah kata tiap dokumen ke dalam array Tab_countKata
Tab_countKata = [0 for i in range(15)]
for i in range(15):
    idx = Index_SortedSim[i]
    Tab_countKata[i]=len(a.d[idx].split())