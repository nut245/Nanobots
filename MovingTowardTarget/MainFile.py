import tkinter as tk
import random
from SettingsFile import *
from NanobotFile import NanoBot
from BorderFile import Border

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

        self.borderCells = []

        self.createBorder()

        # make list for loop create one in each loop to add to list
        # choose random number to select how many dead cells there will be
        # add all of them to screen
        self.targetCell = random.choice(self.borderCells)
        self.targetCell.becomeTarget()
        self.TargetFound = 0

        self.nanobots = []
        for _ in range(NANOBOT_NUMBER):
            self.nanobots.append(NanoBot(main=self, canvas=self.canvas, x=random.randint(BORDERSIZE, gameWidth-BORDERSIZE), 
                                                                        y=random.randint(BORDERSIZE, gameHeight-BORDERSIZE)))
        self.move_nanobots()

    def move_nanobots(self):
        """
        Loops over list of nanobots, running the tick() method within each object.
        
        Then waits after 'FPS_MS' milliseconds to run recursively.

        Usage :
            self.move_nanobots() 
            -> requires no arguments

        Output: None
        """
        for nanobot in self.nanobots:
            nanobot.tick()
        self.root.after(FPS_MS, self.move_nanobots)

    def swarm_target(self):
        """
        Loops over list of nanobots, reassigning cell to move toward to chosen TargetCell.

        Usage :
            self.swarm_target() 
            -> requires no arguments

        Output: None
        """
        for nanobot in self.nanobots:
            nanobot.targetX, nanobot.targetY = self.targetCell.averagePosition
            nanobot.rotate()
        if SPEEDUP_WHEN_TARGET_FOUND:
            for nanobot in self.nanobots:
                nanobot.speed = NANOBOTSPEED * 5

    def gameWindow(self):
        """
        Generates the frame and canvas all objects are drawn and placed onto.

        Usage :
            self.gameWindow() 
            -> requires no arguments

        Output: None
        """
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.frame, width=self.gameWidth, height=self.gameHeight, bg="black", takefocus=1)
        self.canvas.pack(fill="both", expand=True)

    def createBorder(self):
        """
        Generates the Border objects around screen, dependant on width and height.

        Usage :
            self.createBorder() 
            -> requires no arguments

        Output: None
        """
        numberOfBordersAcrossWidth = self.gameWidth / BORDERSIZE * 2
        numberOfBordersAcrossHeight = self.gameHeight / BORDERSIZE * 2
        def accrossWidth(self):
            position = BORDERSIZE
            height = 0
            for _ in range(int(numberOfBordersAcrossWidth)):
                self.borderCells.append(Border(main=self, canvas=self.canvas, x=position, y=height))
                if position >= self.gameWidth - BORDERSIZE * 2:
                    position = BORDERSIZE
                    height = self.gameHeight - BORDERSIZE
                else:
                    position += BORDERSIZE
        def accrossHeight(self):
            position = BORDERSIZE
            width = 0
            for _ in range(int(numberOfBordersAcrossHeight)):
                self.borderCells.append(Border(main=self, canvas=self.canvas, x=width, y=position))
                if position >= self.gameHeight - BORDERSIZE * 2:
                    position = BORDERSIZE
                    width = self.gameWidth - BORDERSIZE
                else:
                    position += BORDERSIZE            
        accrossWidth(self)
        accrossHeight(self)

if __name__ == "__main__":
    Main(gameWidth=GAMEWIDTH, gameHeight=GAMEHEIGHT).root.mainloop()