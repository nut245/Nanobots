import tkinter as tk
from SettingsFile import *
from SubjectBaseFile import SubjectBase

"""
AntigenRPG was meant to replicate the nanobot's ability to copy the antigens along the "victimCell".
It was to copy and display the antigens along the "whiteCell" to disguise the victimCell.

All functionality was not implemented due to scope creep.
"""

class Main:
    """Main controller class 
    
    Purpose: manages connections between subclasses and running of program
    
    Usage ::

        Main(gameWidth, gameHeight) 
        # (int) gameWidth specifies width of window
        # (int) gameHeight specifies height of window
    -> Output: runs main window that displays simulation

    Version Number: 2.0 | Author: Imran Almashoor | Date: 09-08-2024
    """
    def __init__(self, gameWidth, gameHeight):
        self.root = tk.Tk()
        self.root.title("Nanobot Program")
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.gameWindow()

        self.subjects = {}

        self.instantiateSubjects()

        self.root.bind("<Configure>", self.updateGameWindow)

    def instantiateSubjects(self):
        self.whiteCellPosition = (self.gameWidth / 4, self.gameHeight / 2)
        self.whiteCell = SubjectBase(main=self, canvas=self.canvas, x=self.whiteCellPosition[0], y=self.whiteCellPosition[1])
        self.subjects[self.whiteCell] = self.whiteCellPosition

        self.nanoBotPosition = (self.gameWidth / 2, self.gameHeight / 2)
        self.nanoBot = SubjectBase(main=self, canvas=self.canvas, x=self.nanoBotPosition[0], y=self.nanoBotPosition[1])
        self.subjects[self.nanoBot] = self.nanoBotPosition

        self.victimCellPosition = (self.gameWidth - self.gameWidth / 4, self.gameHeight / 2)
        self.victimCell = SubjectBase(main=self, canvas=self.canvas, x=self.victimCellPosition[0], y=self.victimCellPosition[1])
        self.subjects[self.victimCell] = self.victimCellPosition

    def updateGameWindow(self, event=None):
        self.gameWidth = self.root.winfo_width()
        self.gameHeight = self.root.winfo_height()

        self.subjects[self.whiteCell] = (self.gameWidth / 4, self.gameHeight / 2)
        self.subjects[self.nanoBot] = (self.gameWidth / 2, self.gameHeight / 2)
        self.subjects[self.victimCell] = (self.gameWidth - self.gameWidth / 4, self.gameHeight / 2)
        
        for subject, coord in self.subjects.items():
            self.canvas.moveto(subject.subject, coord[0], coord[1])

    def gameWindow(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.frame, width=self.gameWidth, height=self.gameHeight, bg="black", takefocus=1)
        self.canvas.pack(fill="both", expand=True)

if __name__ == "__main__":
    Main(gameWidth=GAMEWIDTH, gameHeight=GAMEHEIGHT).root.mainloop()