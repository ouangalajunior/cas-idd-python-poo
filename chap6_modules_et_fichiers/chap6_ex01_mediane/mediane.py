def mediane (*liste):
    liste = list(liste)
    liste.sort()
    n=len(liste)
    calcul_mediane = 0
    #print(liste)
    if len(liste)%2 == 0 :
        calcul_mediane = (liste[int(n/2) -1] + liste[int(n/2)])/2
        #print(calcul_mediane)
    else:
        calcul_mediane = liste[int((n+1)/2)-1]
        print(calcul_mediane)
    
    return calcul_mediane
