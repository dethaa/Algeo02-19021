def tab_sim(nTerm,tab_frek,nDok):
    #mengembalikan array yang berisi nilai similiarity dokumen i dengan query
    sim = [0 for i in range(nDok)]
    for i in range(nDok):
        if (norm(i+1,nTerm,tab_frek)>0):
            sim[i] = (kalidot(i+1,nTerm,tab_frek)/(norm(0,nTerm,tab_frek)*norm(i+1,nTerm,tab_frek)))
    return(sim)

def norm(d,nTerm,tab_frek):
    #menghitung normal dari vektor dokumen d
    sum=0
    for i in range(0,nTerm):
        sum+=(tab_frek[i][d]**2)
    return(sum**0.5)

def kalidot(d,nTerm,tab_frek):
    #mengembalikan hasil perkalian dot antara vektor dokumen ke-d dengan query
    sum=0
    for i in range(0,nTerm):
        sum+=(tab_frek[i][0]*tab_frek[i][d])
    return(sum)




