import random


random_list = list(range(1,11))



while True:
  random_number1 = random.choice(random_list)
  random_number2 = random.choice(random_list)

  while True:
    print(random_number1, "x", random_number2, "=")
    user_answer = int(input())
    multiply = random_number1*random_number2

    if user_answer == multiply:
      print(random_number1, "x", random_number2, "=", user_answer)
      print("Bravo")
      break
    else:
       print(random_number1, "x", random_number2, "=", user_answer)
       print("Non, ré-essayez")
      

  
 

