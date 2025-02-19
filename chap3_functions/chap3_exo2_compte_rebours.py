import time
def countdown(n = None):
    """ Fonction qui affiche un compte à rebours de n secondes.
L'appel sans argument fait un decompte depuis 10 """
    
    result = 1
    if n is None :
        n = 10
        while n >= 1:
            result = n
            print(f"Il reste {result} secondes")
            time.sleep(1)
            n -=1
    else :
        while n > 0 :
            result = n
            print(f"Il reste {result} secondes")
            time.sleep(1)
            n -= 1
    return result
        
    


    
    
countdown()
countdown(4)


