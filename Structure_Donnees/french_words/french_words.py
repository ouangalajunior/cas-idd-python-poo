words = [w.strip() for w in open('french_words.txt' , encoding='utf-8')]
#words = ["Bon","Papa","mère","tata","Manger", "Boisson", "Mimi"]
# combien y a-t-il de mots en tout?
#print(words.count())
print("Nombre total de mots: ",len(words))
# combien de mots de 4 lettres?

counter = 0
for word in words:
    if len(word)==4 :
        counter +=1
        
print("Nombre de mots de 4 caractères :",counter)

# combien de mots commençant par z?

counter2 = 0
for word in words:
    if word.startswith('z'):
        counter2 += 1
print("Nombre de mots commençant par z :",counter2)
# combien de mots contenant la lettre z?

counter3 = 0
for word in words:
    if "z" in word:
        counter3 += 1
        
print("Nombre de mots  contenant la lettre z :",counter3)


# combien de mots commençant par a et finissant par s?

counter4 = 0
for word in words:
    if word.startswith('a') and  word.endswith('s'):
        counter4 += 1
        
print("Nombre de mots commençant par par a et finissant par s :",counter4)
