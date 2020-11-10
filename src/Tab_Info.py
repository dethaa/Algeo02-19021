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
Tab_Sim=[0 for i in range(10)]
for i in range(10):
    Tab_Sim[i]=similiarity(i+1)

