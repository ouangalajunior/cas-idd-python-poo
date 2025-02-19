import timeit

def common(word1,word2):
    """ fonction common qui implémente la recherche d’éléments communs en utilisant le type set """
    #word1 = input("word1 =")
    #word2 = input("word2 =")
    word1 =set(word1)
    word2 = set(word2)
    list_word = []
    for w in word1:
      #list_word = []
      if w in word2:
          list_word.append(w)
        
          #print(w)
    #print(list_word)
  #print(word1)
  #print(word2)
    return list_word

word1 = "anticontisutionnellement"
word2 = "eclesiastique"
#common(word1,word2 )

def common2(word1, word2):
    list_word = []
    for w in word1:
        if w in word2:
            if w not in list_word:
              list_word.append(w)
    #print(list_word)
    
    return list_word

#common2(word1,word2 )

print(sorted(common(word1,word2 )))
print(sorted(common2(word1,word2 )))
print(sorted(common(word1,word2 )) == sorted(common2(word1,word2 )))

print(timeit.timeit('common(word1,word2)', globals=globals()))
#La fonction common est plus performante que common2. L'exécution se fait 0.76 s alors que common2 se fait en 1.4 s (presque le double)
print(timeit.timeit('common2(word1,word2)', globals=globals()))

