import unittest
from unittest.mock import patch
from Quiz import load_questions, ask_question, check_answer, display_score
import json
import os

class TestQuiz(unittest.TestCase):

    def test_load_questions(self):
        questions = load_questions('questions.json')
        self.assertIsInstance(questions, dict)
        self.assertGreater(len(questions), 0)

    @patch('builtins.input', return_value='B')
    def test_ask_question(self, input_mock):
        question = "What is the print function in Python?"
        options = {
            "A": "It prints the type of a variable",
            "B": "It prints the output of a function or a variable",
            "C": "It asks for user input",
            "Correct": "B"
        }
        answer = ask_question(question, options)
        self.assertEqual(answer, 'B')

    def test_check_answer_correct(self):
        answer = 'B'
        correct_answer = 'B'
        result = check_answer(answer, correct_answer)
        self.assertTrue(result)

    def test_check_answer_incorrect(self):
        answer = 'A'
        correct_answer = 'B'
        result = check_answer(answer, correct_answer)
        self.assertFalse(result)

    @patch('builtins.print')
    def test_display_score(self, print_mock):
        score = 3
        total = 5
        display_score(score, total)
        print_mock.assert_called_with(f"\nYour final score is {score} out of {total}")

    def test_load_questions_empty_file(self):
        with open('empty.json', 'w') as f:
            pass
        questions = load_questions('empty.json')
        self.assertIsNone(questions)
        os.remove('empty.json')

    def test_load_questions_invalid_json(self):
        with open('invalid.json', 'w') as f:
            f.write('Invalid JSON')
        questions = load_questions('invalid.json')
        self.assertIsNone(questions)
        os.remove('invalid.json')

    def test_load_questions_missing_correct_key(self):
        with open('missing_correct.json', 'w') as f:
            json.dump({
                "What is the print function in Python?": {
                    "A": "It prints the type of a variable",
                    "B": "It prints the output of a function or a variable",
                    "C": "It asks for user input"
                }
            }, f)
        questions = load_questions('missing_correct.json')
        self.assertIsNone(questions)
        os.remove('missing_correct.json')

    def test_load_questions_invalid_correct_value(self):
        with open('invalid_correct.json', 'w') as f:
            json.dump({
                "What is the print function in Python?": {
                    "A": "It prints the type of a variable",
                    "B": "It prints the output of a function or a variable",
                    "C": "It asks for user input",
                    "Correct": "D"
                }
            }, f)
        questions = load_questions('invalid_correct.json')
        self.assertIsNone(questions)
        os.remove('invalid_correct.json')

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(unittest.makeSuite(TestQuiz))
    print(f"\n{result.testsRun} Tests, {result.testsRun - len(result.errors) - len(result.failures)} Passed, {len(result.failures)} Failed, {len(result.errors)} Errors")