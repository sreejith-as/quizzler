"""Contains the core quiz logic for iterating through questions and checking answers."""

import html

class QuizBrain:
    def __init__(self, q_list):
        """
        Initialize the QuizBrain object.

        Args:
            q_list (list): List of Question objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Return True if there are more questions left."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Get the next question and increment the counter."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Decode HTML entities like &quot; from API
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        """
        Check if the user's answer matches the correct one.

        Args:
            user_answer (str): User's selected answer ("True"/"False").

        Returns:
            bool: True if correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
