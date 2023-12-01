import csv
import random
import os


def load_questions(filename: str, number_of_questions: int = 10) -> list:
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


def save_score(name: str, score: int) -> None:
    with open("high_scores.csv", "a") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, score])


def display_high_scores() -> None:
    if not os.path.exists("high_scores.csv"):
        return

    with open("high_scores.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        high_scores = sorted(csvreader, key=lambda x: int(x[1]), reverse=True)

    print("\nHigh Scores:")
    for name, score in high_scores[:10]:
        print(f"{name}: {score}")


def run_quiz() -> None:
    questions = load_questions("quiz_questions.csv")
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
 
    name = input("Enter your name to save your score: ")
    if name.strip():
        save_score(name, score)

    print(f"You scored {score}/{len(questions)}")
    display_high_scores()


if __name__ == "__main__":
    run_quiz()
