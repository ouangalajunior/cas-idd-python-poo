from quizz import poser_question

score = 0

for _ in range(3):
    if poser_question():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")

print(f"Score finale: {score}/3")