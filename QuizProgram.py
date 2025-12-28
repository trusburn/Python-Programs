quiz = {
    "question1": {
        "question": "What is the full meaning of HTML",
        "answer": "HyperText Markup Language"
    },
    "question2": {
        "question": "What is the full meaning of CSS",
        "answer": "Cascading StyleSheet"
    },
    "question3": {
        "question": "What is the full meaning of JS",
        "answer": "JavaScript"
    }
    
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("What is the answer? ")

    if answer.lower() == value['answer'].lower():
        score = score + 1
        print("Correct✅")
        print(f"Your score is now {score}")
    else:
        print("Wrong answer❌")
        print(f"Your score is now {score}")

print("You got " + str(score) +" Out of 3 Questions")
print("Your percentage is " + str(int(score/7 * 100))+"%")