
import math

def calcul_factoriel(n):
    """ Fonction qui retourne la factorielle d'un nombre"""
    value_n = n
    result = 1
    if n == 0 :
        result = 1
    else :
        
        while n > 0: 
            result *= n
            n -= 1
    print(f"La factorielle de {value_n} vaut {result}")    
    return result
 
 # Exemple de calcul de factorielle de 6
calcul_factoriel(6)

print(calcul_factoriel(100) == math.factorial(100))
