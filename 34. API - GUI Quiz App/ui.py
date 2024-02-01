from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR,  fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="White", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, sticky="we")

        self.right_button = Button(command=self.right)
        right_img = PhotoImage(file="images/true.png")
        self.right_button.config(image=right_img)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(command=self.wrong)
        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button.config(image=wrong_img)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)