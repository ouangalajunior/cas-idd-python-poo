import random

user_number = 0
random_list = list(range(1,11))
random_number = random.choice(random_list)

while user_number != random_number:
     user_number = int(input('Devinez un nombre entre 1 et 10:'))
     if user_number < random_number:
          print(f'Votre proposition est : {user_number}')
          print('Non plus')
     else :
          print(f'Votre proposition est : {user_number}')
          print('Non moins')

print(f'Votre proposition est : {user_number}')
print('Bravo')

   
   

 


