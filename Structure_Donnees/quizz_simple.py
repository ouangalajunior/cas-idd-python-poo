import random
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "choix": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "reponse": "C"
    },
    {
        "question": "Combien font 7 x 8 ?",
        "choix": ["A) 48", "B) 56", "C) 64", "D) 72"],
        "reponse": "B"
    },
    {
        "question": "Qui a écrit 'Les Misérables' ?",
        "choix": ["A) Victor Hugo", "B) Molière", "C) Balzac", "D) Zola"],
        "reponse": "A"
    },
    {
        "question": "Quel est le symbole chimique de l'eau ?",
        "choix": ["A) O2", "B) CO2", "C) H2O", "D) CH4"],
        "reponse": "C"
    }
]

# while True:
#     question = random.choice(questions)
#     print("\n", question["question"])
#     for choix in question["choix"]:
#         print(choix)
#     reponse_utilisateur = input("Votre réponse(A,B,C ou D) :").strip().upper()
#     if reponse_utilisateur == question["reponse"]:
#         print("Bonne réponse")
    
#     else:
#         print(f"Mauvaise réponse. La bonne réponse était {question['reponse']}")
#
#
# version 2 rester sur la même question jusqu'à trouver la bonne réponse

while True:
    question = random.choice(questions)
    while True:
      print("\n", question["question"])
      for choix in question["choix"]:
        print(choix)
      reponse_utilisateur = input("Votre réponse(A,B,C ou D) :").strip().upper()
      if reponse_utilisateur == question["reponse"]:
        print("Bonne réponse")
        break
    
      else:
        print(f"Mauvaise réponse. Essayez encore")
    #print("Passons à la question suivante ..")
