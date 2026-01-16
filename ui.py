import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
COLOR_CORRECT = "#9bdeac"
COLOR_WRONG = "#e7305b"
FONT_MAIN = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tk.Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280, 
            text="Loading...", 
            fill=THEME_COLOR,
            font=FONT_MAIN
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = tk.Button(text="TRUE", highlightthickness=0, bg="green", fg="green",
                                     font=("Arial", 12, "bold"), command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(text="FALSE", highlightthickness=0, bg="red", fg="red",
                                      font=("Arial", 12, "bold"), command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.enable_buttons()
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.disable_buttons()

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct: bool):
        self.disable_buttons() # prevent spam clicking
        
        if is_correct:
            self.canvas.config(bg=COLOR_CORRECT)
        else:
            self.canvas.config(bg=COLOR_WRONG)
            
        # wait 1s then go to next question
        self.window.after(1000, self.get_next_question)

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_buttons(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")