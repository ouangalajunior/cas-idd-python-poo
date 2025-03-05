import unicodedata

def normaliser_texte(texte):
    texte = " ".join(texte)
    texte = texte.lower()
    texte = ''.join(c for c in texte if c.isalpha())# Garde seulement les lettres
    texte = ''.join(unicodedata.normalize('NFD', c) for c in texte) # Supprime les accents
    
    return texte
    


def afficher_caracteres_frequence(texte):
    texte_normalise = normaliser_texte(texte)  # Convertir la liste en une chaîne de caractères
    total_caractere = len(texte_normalise)
    
    frequences = {}

    # Comptage manuel des fréquences
    for caractere in texte_normalise:
        if caractere in frequences:
            frequences[caractere] += 1
        else:
            frequences[caractere] = 1

    

    frequences_triees = sorted(frequences.items(), key = lambda x: x[1], reverse = True)
    
    # Affichage des résultats
    for caractere, frequence in frequences_triees:  # Tri alphabétique des caractères
        frequence_pourcentage = round(frequence * 100 / total_caractere, 2)
        print(f"{caractere} :  {frequence_pourcentage} %")
    
    

# Chargement du texte et appel de la fonction
with open('texte_guttember.txt', encoding='utf-8') as f:
    texte = f.readlines()  # Lire toutes les lignes du fichier

afficher_caracteres_frequence(texte)