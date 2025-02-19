def suite_fibonacci(n):
    """ Fonction pour afficher les termes d'une suite de fibonacci"""
    u_0 = 1
    u_1 = 1
    
    if n == 0 :
        print(u_0)
    elif n== 1:
        print(u_1)
    else:
    
    
      while u_0 < n :
          print(u_0)
          u_0,u_1 =u_1,u_0+u_1 
        
    

suite_fibonacci(0)

  