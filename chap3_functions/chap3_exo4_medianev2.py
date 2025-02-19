def enter_number():
    """ Fonction demandant à l’utilisateur d’entrer des nombres, et les mémorise dans une liste """
    numbers = []
    print("Entrez un nombre par ligne, ligne vide pour terminer. ")

    while True:
        user_input = input()
        if user_input =="":
            break
        number = float(user_input)
        numbers.append(number)
        #print(numbers)
        
        
        
    #print("Vous avez saisi:", len(numbers),numbers)
    return numbers
#enter_number()

def mediane ():
    """ fonction mediane qui prend un nombre variable de nombres saisis par l'utilisateur et calcule leur mediane"""
    liste = enter_number()
    liste.sort()
    n=len(liste)
    calcul_mediane = 0
    #print(liste)
    if len(liste)%2 == 0 :
        calcul_mediane = (liste[int(n/2) -1] + liste[int(n/2)])/2
        #calcul_mediane = round(calcul_mediane,2)
        #print(calcul_mediane)
    else:
        
        calcul_mediane = liste[int((n+1)/2)-1]
        #calcul_mediane = round(calcul_mediane,2)
                          
        #print(calcul_mediane)
    calcul_mediane = round(calcul_mediane,3)    
    print("Vous avez saisi", n, " nombres; leur médiane est : ",calcul_mediane)
    
    return calcul_mediane
mediane()


