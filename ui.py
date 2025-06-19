"""User interface for the Quizzler app using Tkinter."""

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """
        Initialize the GUI for the quiz.

        Args:
            quiz_brain (QuizBrain): An instance of the quiz logic handler.
        """
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Score label at the top
        self.score_label = Label(text="Score 0", foreground="White", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas to show questions
        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True button with image
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)

        # False button with image
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """Display the next question or show end message if no questions left."""
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        """Handler for when the user presses the 'True' button."""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        """Handler for when the user presses the 'False' button."""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Show feedback color (green/red) and wait 1 second before next question."""
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
