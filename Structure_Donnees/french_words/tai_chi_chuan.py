#words = [w.strip() for w in open('french_words.txt' , encoding='utf-8')]
words = ["Bon","papa","mèrei","tata","Manger", "Boisson", "mimia", "memia", "mirabel"]

lettres_utilisateur = input("Entrez vos lettres:")
print("Vos lettres:", lettres_utilisateur)

print("Mot commencent par", lettres_utilisateur[0], "et qui contiennent",",".join(lettres_utilisateur[1:] ) )
# print(",".join(lettres_utilisateur[1:] ))

# for l in lettres_utilisateur:
#     print(l)
for word in words:
  word_start = lettres_utilisateur[0]
  word_remain = lettres_utilisateur[1:]
  

  if word.startswith(word_start) and "".join(word_remain) in word:
    print(word)  
    print(word_remain)
    # if word.startswith(lettres_utilisateur[0]) and word in lettres_utilisateur[1:]:
    #     print(word)
print("Merci")
