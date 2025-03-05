import unicodedata

def normalize(word):
    """ Supprime les accents et mets en minuscule"""
    return ''.join(c for c in unicodedata.normalize('NFD', word.lower()) if c.isalpha())
#with open('french_words.txt', encoding='utf-8') as f:

def construire_dictionnaire(fichier):
    """ Construire dictionnaire à partir du fichier"""
    anagrammes = {}
    
    
    words = [w.strip() for w in open(fichier)]
    for word in words:
        if word:
            key = ''.join(sorted(normalize(word)))
            if key in anagrammes:
                anagrammes[key].append(word)
            else:
                anagrammes[key] = [word]
                
    return anagrammes
"""    
def alpha(word):
    word = word.lower()
    word =word.replace('-', '')
    for accent in ('é', 'è', 'ê'):
        word = word.replace(accent, 'e')
        
    for accent in ('à', 'á', 'â'):
        word = word.replace(accent, 'a')
        
    for accent in ('ô', 'ó', 'ò'):
        word = word.replace(accent, 'o')
    
    return sorted(word)
    
    
"""

anagrammes = construire_dictionnaire('french_words.txt')
while True:
    word = input('Entrez un mot: ').strip()
    if not word: break
    
    key = ''.join(sorted(normalize(word)))
    
    if key in anagrammes:
        print('\n'.join(anagrammes[key]))
    else:
        print('Aucun anagramme trouvé')

"""
    to_find = alpha(word)

    for w in words:
        if alpha(w) == to_find:
            print(f'Anagramme trouvé : {w}')
            
            """

print('Au revoir')