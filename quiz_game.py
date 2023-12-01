import csv
import random


def load_questions(filename: str, number_of_questions=10: int) -> list:
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)

        # Skip the header row
        next(csvreader)

        questions = [row for row in csvreader]
    return random.sample(questions, number_of_questions)


def ask_question(question: list) -> bool:
    print(question[0])
    for i, option in enumerate(question[1:5], start=1):
        print(f"{i}. {option}")
    answer = int(input("Enter your answer (1-4): "))
    if question[answer + 1] == question[5]:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is {question[5]}")
        return False


def run_quiz() -> None:
    questions = load_questions("quiz_questions.csv")
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    print(f"You scored {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()
