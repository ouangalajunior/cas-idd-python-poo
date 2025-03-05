from random import randint

MIN = 0
MAX = 10

to_guess = randint(MIN, MAX)

print(f"Devinez un nombre entre {MIN} et {MAX}")

while True:

    try:
      i = int(input('Votre proposition: '))
      if i < MIN or i > MAX:
         

         print(f"Erreur: le nombre doit être supérieur à {MIN} et inférieur à {MAX}")
         continue

    except ValueError:
       
       print(f"Erreur: le nombre doit être un entier positif compris entre {MIN} et {MAX}")
       continue
    

    if i == to_guess:
        print('Bravo!')
        break

    if i < to_guess:
        print('Non, plus!')
    else:
        print('Non, moins!')