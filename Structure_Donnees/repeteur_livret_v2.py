import random


random_list = list(range(1,11))
compteur = 0

while compteur < 5:
  random_number1 = random.choice(random_list)
  random_number2 = random.choice(random_list)
  
  

  while True:
    print(random_number1, "x", random_number2, "=")
    user_answer = int(input())
    multiply = random_number1*random_number2
    

    if user_answer == multiply:
      print(random_number1, "x", random_number2, "=", user_answer)
      print("Bravo")
      compteur += 1

      print("Score:", compteur,"/5")
      break
    else:
       print(random_number1, "x", random_number2, "=", user_answer)
       print("Non, ré-essayez")
       compteur = 0
    
    print("Score:", compteur,"/5")
    
    
      
print("Bravo, vous avez répondu à 5 réponses correctes")
    
