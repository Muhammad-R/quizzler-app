THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:


    def __init__(self,quiz_brain:QuizBrain):

        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: ", fg="white" ,bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg='white')
        self.question_text=self.canvas.create_text(150,125,
                                                   text="Some Question",
                                                   fill=THEME_COLOR,
                                                   width=280,
                                                   font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        trueimg=PhotoImage(file="images/true.png")
        self.truebtn=Button(image=trueimg,highlightthickness=0,command=self.clicky)
        self.truebtn.grid(row=2,column=1)


        fimg= PhotoImage(file="images/false.png")
        self.fbtn = Button(image=fimg,highlightthickness=0,command=self.clickn)
        self.fbtn.grid(row=2, column=0)
        self.get_next()

        self.window.mainloop()


    def get_next(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz!")
            self.truebtn.config(state="disabled")
            self.fbtn.config(state="disabled")

    def clicky(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def clickn(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next)


