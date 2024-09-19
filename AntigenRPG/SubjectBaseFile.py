import tkinter as tk

class SubjectBase():
    def __init__(self, main, canvas, x = None, y = None):
        self.main = main
        self.canvas = canvas
        self.x, self.y = x, y

        self.subject = self.canvas.create_oval((self.x,self.y, self.x,self.y), outline='white', width=3)

    def updateOnScreen(self):
        print('yes')
        self.canvas.moveto(self.subject, self.x,self.y, self.x,self.y)