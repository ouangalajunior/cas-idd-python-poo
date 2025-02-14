#if, elif et else
# vérifier age
# age = int(input("Entrez votre age:"))

# if age<18:
#     print("Vous êtes mineur")
# elif age == 18:
#     print("Vous avez exactement 18 ans")
# else: 
#     print("Vous êtes majeur")


#For boucle
# for i in range(10):
#     print(" Itération:",i)

# fruits = ["Pomme", "banne", "Orange", "Citron"]

# for fruit in fruits:
#     print(fruit)

#While boucle
""" compteur = 0
while compteur < 10:
    print("Compteur:", compteur)
    compteur +=1 """

#Break
# for i in range(20):
#     if i ==7:
#         break
#     print(i)



#Continue
# for i in range(20):
#     if i % 2 ==0:
#         continue
#     print(i)




#Verifier si un nombre est pair ou impair

# nombre = int(input("Entrez un nombre:"))
# if nombre % 2 == 0:
#     print(nombre, "est un nombre pair")
# else:
#     print(nombre, "est un nombre impair")





# Compte à rebours
# Demander un nombre à l'utilisateur et faire le compte à rebours jusqu'à 0
nombre = int(input("Entrez un nombre:"))
while nombre >= 0 :
    print("Compte à rebours:" , nombre)
    nombre -=1


nombre = int(input("Entrez un nombre:"))