import unittest
from unittest.mock import patch, MagicMock
from kinter7     import Quiz
import tkinter as tk
import json

class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.quiz = Quiz(self.root)

    def test_load_questions(self):
        questions = self.quiz.load_questions('questions.json')
        self.assertIsInstance(questions, dict)
        self.assertGreater(len(questions), 0)

    @patch('tkinter.Tk')
    def test_display_question(self, mock_tk):
        self.quiz.display_question()
        mock_tk.assert_called_once()

    @patch('tkinter.Label')
    def test_check_answer_correct(self, mock_label):
        answer = 'B'
        correct_answer = 'B'
        self.quiz.check_answer(answer, correct_answer)
        mock_label.assert_called_once_with(text="Correct!", font=("Arial", 18), bg="#f0f0f0", fg="#00ff00")

    @patch('tkinter.Label')
    def test_check_answer_incorrect(self, mock_label):
        answer = 'A'
        correct_answer = 'B'
        self.quiz.check_answer(answer, correct_answer)
        mock_label.assert_called_once_with(text=f"Incorrect. The correct answer is {correct_answer}.", font=("Arial", 18), bg="#f0f0f0", fg="#ff0000")

    def test_next_question(self):
        self.quiz.next_question()
        self.assertEqual(self.quiz.current_question, 1)

    @patch('tkinter.Label')
    def test_display_score(self, mock_label):
        self.quiz.display_score()
        mock_label.assert_called_once_with(text=f"Your final score is {self.quiz.score} out of {len(self.quiz.selected_questions)}", font=("Arial", 24), bg="#f0f0f0")

    def test_retry(self):
        self.quiz.retry()
        self.assertEqual(self.quiz.score, 0)
        self.assertEqual(self.quiz.current_question, 0)

    def test_clear_window(self):
        self.quiz.clear_window()
        self.assertEqual(len(self.root.winfo_children()), 0)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(unittest.makeSuite(TestQuiz))
    print(f"\n{result.testsRun} Tests, {result.testsRun - len(result.errors) - len(result.failures)} Passed, {len(result.failures)} Failed, {len(result.errors)} Errors")