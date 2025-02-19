# liste = [4,5,10,6,9,3,3,1,2,15]
# print(len(liste))
# liste.sort()
# print(liste)
# n=len(liste)
# print(n)
# list_sort =liste.sort()
# print(liste[5])

#print(liste[int((n+1)/2)-1])

#print((liste[int(n/2) -1] + liste[int(n/2)])/2)
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
        #print(calcul_mediane)
    
    return calcul_mediane

#ma_liste = [4,5,10,6,9,3,3,1,2,15,6]
#ma_liste2 = [7,4,5,6,7,8,9,2,14,6]
#mediane(ma_liste)
#mediane(ma_liste2)
#mediane(1,2,3,4,5)
#mediane(20,10,39,40)

        
    