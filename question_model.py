"""Defines the Question class representing each quiz question."""

class Question:
    def __init__(self, q_text, q_answer):
        """
        Initialize a Question object.

        Args:
            q_text (str): The question text.
            q_answer (str): The correct answer ("True" or "False").
        """
        self.text = q_text
        self.answer = q_answer
