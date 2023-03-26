import tkinter
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def get_next_question(self):
        self.canvas.config(background="white")
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=f"{question_text}")

    def user_report(self):
        exit = messagebox.askokcancel(title="Your Score", message=f"Your score is {self.quiz.score}")
        if exit:
            print("someone pressed ok")
            self.window.quit()

    def get_answer(self, answer: str):
        checked_answer = self.quiz.check_answer(answer)
        if checked_answer:
            question_background = "green"
        else:
            question_background = "red"
        self.canvas.config(background=question_background)
        self.score.config(text=f"Score: {self.quiz.score}")
        print(checked_answer)
        if self.quiz.still_has_questions():
            self.window.after(1000, func=self.get_next_question)
        else:
            self.user_report()


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = tkinter.Label(
            background=THEME_COLOR, foreground="white", text=f"Score: {self.quiz.score}"
        )
        self.score.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(
            height=250,
            width=300,
        )
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Text goes here", font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_img = tkinter.PhotoImage(
            file="day34/quizzler-app-start/images/true.png"
        )
        false_button_img = tkinter.PhotoImage(
            file="day34/quizzler-app-start/images/false.png"
        )

        self.true_button = tkinter.Button(
            image=true_button_img, highlightthickness=0, padx=60, pady=60, command=lambda: self.get_answer(answer="True")
        )
        self.false_button = tkinter.Button(
            image=false_button_img, highlightthickness=0, padx=60, pady=60, command=lambda: self.get_answer(answer="False")
        )
        self.true_button.grid(column=1, row=2)
        self.false_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()
