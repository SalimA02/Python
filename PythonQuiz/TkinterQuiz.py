import random
import json
import tkinter as tk

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.questions = self.load_questions('questions.json')
        self.selected_questions = random.sample(list(self.questions.items()), 3)
        self.score = 0
        self.current_question = 0
        self.display_question()

    def load_questions(self, filename='questions.json'):
        """Load quiz questions from a JSON file."""
        with open(filename, 'r') as f:
            return json.load(f)

    def display_question(self):
        """Display the current question."""
        if self.current_question < len(self.selected_questions):
            question, options = self.selected_questions[self.current_question]
            self.clear_window()
            main_frame = tk.Frame(self.root, bg="#f0f0f0")
            main_frame.pack(fill="both", expand=True)
            tk.Label(main_frame, text="Quiz Game", font=("Arial", 24), bg="#f0f0f0").pack(pady=10)
            question_frame = tk.Frame(main_frame, bg="#f0f0f0")
            question_frame.pack(fill="both", expand=True)
            tk.Label(question_frame, text=question, font=("Arial", 18), wraplength=400, bg="#f0f0f0").pack(pady=20)
            options_frame = tk.Frame(main_frame, bg="#f0f0f0")
            options_frame.pack(fill="both", expand=True)
            for option, description in options.items():
                if option != "Correct":
                    tk.Button(options_frame, text=f"{option}: {description}", font=("Arial", 14), command=lambda option=option: self.check_answer(option, options["Correct"]), bg="#ccccff").pack(pady=10, fill="x")
        else:
            self.display_score()

    def check_answer(self, answer, correct_answer):
        """Check if the user's answer is correct."""
        if answer.upper() == correct_answer:
            self.score += 1
            result_text = "Correct!"
            result_color = "#00ff00"  # green
        else:
            result_text = f"Incorrect. The correct answer is {correct_answer}."
            result_color = "#ff0000"  # red
        result_frame = tk.Frame(self.root, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True)
        tk.Label(result_frame, text=result_text, font=("Arial", 18), bg="#f0f0f0", fg=result_color).pack(pady=20)
        tk.Button(result_frame, text="Next Question", font=("Arial", 14), command=self.next_question, bg="#ccccff").pack(pady=10, fill="x")

    def next_question(self):
        self.current_question += 1
        self.display_question()

    def display_score(self):
        """Display the final score."""
        self.clear_window()
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True)
        tk.Label(main_frame, text="Quiz Game", font=("Arial", 24), bg="#f0f0f0").pack(pady=10)
        score_frame = tk.Frame(main_frame, bg="#f0f0f0")
        score_frame.pack(fill="both", expand=True)
        tk.Label(score_frame, text=f"Your final score is {self.score} out of {len(self.selected_questions)}", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)
        tk.Button(score_frame, text="Retry", font=("Arial", 14), command=self.retry, bg="#ccccff").pack(pady=10, fill="x")

    def retry(self):
        self.score = 0
        self.current_question = 0
        self.selected_questions = random.sample(list(self.questions.items()), 3)
        self.display_question()

    def clear_window(self):
        """Clear the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    quiz = Quiz(root)
    root.mainloop()