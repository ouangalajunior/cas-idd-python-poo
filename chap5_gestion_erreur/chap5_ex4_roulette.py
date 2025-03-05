
i=0
j= 0
k=0
try:
  while True:
      print(i)
      i +=1
      
      print(j)
      j +=1
      
      print(k)
      k +=1
      
      if i==10:
          i=0
      if j==11:
          j=0
      if k==12:
         k=0
        
except KeyboardInterrupt:
    print("\nVous avez appuyé ctrl-c!")
    print(f"\nValeurs des compteurs: {i} {j} {k} ")
    if i==j==k:
        print(f"\nVous avez gagné!")
    else:
        print(f"\nVous avez perdu! ")
    
    
        
    

