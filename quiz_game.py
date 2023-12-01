import csv
import random
import os


def load_questions(filename: str, number_of_questions: int = 10) -> list:
    try:
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            # Skip the header row
            next(csvreader)

            questions = [row for row in csvreader]
        return random.sample(questions, min(number_of_questions, len(questions)))
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        exit()


def ask_question(question: list) -> bool:
    # Print the question and options
    print(question[0])
    for i, option in enumerate(question[1:5], start=1):
        print(f"{i}. {option}")

    # Loop until the user enters a valid answer
    answer = None
    while answer not in range(1, 5):
        try:
            answer = int(input("Enter your answer (1-4): "))
            if answer not in range(1, 5):
                raise ValueError()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Check if the answer is correct
    if question[answer] == question[5]:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is {question[5]}")
        return False


def save_score(name: str, score: int) -> None:
    # Create the file if it doesn't exist
    if not os.path.exists("high_scores.csv"):
        with open("high_scores.csv", "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Name", "Score"])

    # Append the score to the file
    with open("high_scores.csv", "a") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, score])


def display_high_scores() -> None:
    # Return if the file doesn't exist
    if not os.path.exists("high_scores.csv"):
        return

    # Sort the scores
    with open("high_scores.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        high_scores = sorted(csvreader, key=lambda x: int(x[1]), reverse=True)

    # Display the top 10 scores
    print("\nHigh Scores:")
    for name, score in high_scores[:10]:
        print(f"{name}: {score}")


def run_quiz() -> None:
    # Load the questions
    questions = load_questions("quiz_questions.csv")
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1

    # Display the score
    print(f"You scored {score}/{len(questions)}")

    # Save the score
    name = input("Enter your name to save your score: ")
    if name.strip():
        save_score(name, score)

    display_high_scores()


if __name__ == "__main__":
    run_quiz()
