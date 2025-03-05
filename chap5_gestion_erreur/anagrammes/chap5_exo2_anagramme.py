from collections import defaultdict

# Charger le fichier et créer un dictionnaire
anagram_dict = defaultdict(list)

with open('french_words.txt', encoding='utf-8') as f:
    for word in f:
        sorted_word = "".join(sorted(word.strip()))  # Trié comme clé
        anagram_dict[sorted_word].append(word.strip())  # Ajouter le mot correspondant

# Demander à l'utilisateur de saisir un mot
while True:
    word = input('Entrez un mot: ').strip()
    if not word:
        break

    key = "".join(sorted(word))  # Chercher la clé triée
    if key in anagram_dict:
        print("Anagrammes trouvés :", ", ".join(anagram_dict[key]))
    else:
        print("Aucun anagramme trouvé.")

print('Au revoir')