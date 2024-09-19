from SettingsFile import *

class Border:
    """Border that surrounds screen
    
    Purpose: to replicate vessels in human body, to contain nanobots
    
    Usage ::

        Nanobot(main, canvas, x, y) 
        # (Main object) main to access attributes/methods out of scope
        # (Canvas object) canvas to place nanobots on same widget
        # (int) x, (int) y specifies intial position to place nanobot
    -> Output: dot with (x,y) to be placed and accessed by nanobots
    
    Version Number: 2.0 | Author: Imran Almashoor | Date: 09/08/2024
    """
    def __init__(self, main, canvas, x, y):
        self.main = main
        self.canvas = canvas
        self.isChecked = False
        self.isTarget = False

        self.object = self.canvas.create_polygon(self.create_coordinates(x, y), outline='white', width=3)

        self.averagePosition = [int(self.x2-BORDERSIZE/2), int(self.y3-BORDERSIZE/2)]

    def becomeTarget(self):
        self.isTarget = True
        self.canvas.itemconfig(self.object, outline='red')
        self.canvas.tag_raise(self.object)

    def create_coordinates(self, x, y):
        self.x0, self.y0 = x, y
        self.x1 = self.x0 + BORDERSIZE
        self.y1 = self.y0
        self.x2 = self.x0 + BORDERSIZE
        self.y2 = self.y0 + BORDERSIZE
        self.x3 = self.x0
        self.y3 = self.y0 + BORDERSIZE
        return (self.x0, self.y0, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
