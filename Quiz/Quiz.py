import random
import json

def load_questions(filename):
        try:
            with open(filename, 'r') as f:
                questions = json.load(f)
                if not questions:
                    raise ValueError("JSON file is empty")
                for question, options in questions.items():
                    if not isinstance(options, dict):
                        raise ValueError("Options must be a dictionary")
                    if "Correct" not in options:
                        raise ValueError("Each question must have a 'Correct' key")
                    if options["Correct"] not in ['A', 'B', 'C']:
                        raise ValueError("Invalid 'Correct' value")
                return questions
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")
            return None
        except ValueError as e:
            print(f"Error: {e}")
            return None

def ask_question(question, options):
    """Ask a quiz question and return the user's answer."""
    print("\n" + question + "\n")
    for option, description in options.items():
        if option != "Correct":
            print(f"{option}: {description}")
    while True:
        answer = input("\nChoose the correct option (A, B, C): ")
        if answer.upper() in ['A', 'B', 'C']:
            return answer
        else:
            print("Invalid option. Please enter A, B, or C.")

def check_answer(answer, correct_answer):
    """Check if the user's answer is correct."""
    if answer.upper() == correct_answer:
        print("\nCorrect!\n")
        return True
    else:
        print(f"\nIncorrect. The correct answer is {correct_answer}.\n")
        return False

def display_score(score, total):
    """Display the final score."""
    print(f"\nYour final score is {score} out of {total}")

def main():
    questions = load_questions('questions.json')
    selected_questions = random.sample(list(questions.items()), 3)
    score = 0
    for question, options in selected_questions:
        answer = ask_question(question, options)
        if check_answer(answer, options["Correct"]):
            score += 1
    display_score(score, len(selected_questions))

if __name__ == "__main__":
    main()