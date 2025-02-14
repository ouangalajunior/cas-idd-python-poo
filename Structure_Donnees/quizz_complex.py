import random
questions = [
    {"question": "Quelle est la capitale de la France ?", "choix": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "reponse": "C"},
    {"question": "Combien font 7 x 8 ?", "choix": ["A) 48", "B) 56", "C) 64", "D) 72"], "reponse": "B"},
    {"question": "Qui a écrit 'Les Misérables' ?", "choix": ["A) Victor Hugo", "B) Molière", "C) Balzac", "D) Zola"], "reponse": "A"},
    {"question": "Quel est le symbole chimique de l'eau ?", "choix": ["A) O2", "B) CO2", "C) H2O", "D) CH4"], "reponse": "C"},
    {"question": "Quel est le plus grand océan du monde ?", "choix": ["A) Atlantique", "B) Indien", "C) Pacifique", "D) Arctique"], "reponse": "C"},
    {"question": "Combien y a-t-il de continents sur Terre ?", "choix": ["A) 5", "B) 6", "C) 7", "D) 8"], "reponse": "C"},
    {"question": "Quel est le plus grand pays du monde en superficie ?", "choix": ["A) Chine", "B) Canada", "C) Russie", "D) États-Unis"], "reponse": "C"},
    {"question": "Quel est l'élément chimique représenté par la lettre 'O' ?", "choix": ["A) Or", "B) Oxygène", "C) Ozone", "D) Osmium"], "reponse": "B"},
    {"question": "Qui a peint La Joconde ?", "choix": ["A) Michel-Ange", "B) Van Gogh", "C) Léonard de Vinci", "D) Picasso"], "reponse": "C"},
    {"question": "Quelle planète est surnommée la 'planète rouge' ?", "choix": ["A) Vénus", "B) Mars", "C) Jupiter", "D) Saturne"], "reponse": "B"}
]
bonne_reponse_consecutive = 0


while bonne_reponse_consecutive < 3:
    question = random.choice(questions)

    print(question["question"])
    for choix in question["choix"]:
        print(choix)

    reponse_utilisateur = input("Votre réponse (A,B,C ou D) : ").strip().upper()

    if reponse_utilisateur == question["reponse"]:
        bonne_reponse_consecutive +=1
        print(f"Bonne réponse. Score: {bonne_reponse_consecutive}/3")
    else:
        bonne_reponse_consecutive = 0
        print(f"Mauvaise réponse. Score: {bonne_reponse_consecutive}/3")
    
print(f"Félicitations, Vous avez repondu correctement 3 fois de suite")
