import random

questions = [

    {"question": "Quelle est la capitale de la France ?", "reponse": "Paris"},
    {"question": "Combien font 2 + 2 ?", "reponse": "4"},
    {"question": "Quelle est la couleur du ciel ?", "reponse": "bleu"}
]

def poser_question():
    "Pose une question aléatoire à l'utilisateur"
    question = random.choice(questions)
    user_reponse= input(f"{question['question']}:").strip().lower()

    return user_reponse == question['reponse'].lower()