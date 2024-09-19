import random
import math
from SettingsFile import *

class NanoBot:
    """Nanobot (projected as dot)
    
    Purpose: not to be given specific variable name to deplicate hundreds/thousands of times to replicate large autonomy
    
    Usage ::

        Nanobot(main, canvas, x, y) 
        # (Main object) main to access attributes/methods out of scope
        # (Canvas object) canvas to place nanobots on same widget
        # (int) x, (int) y specifies intial position to place nanobot
    -> Output: dot with (x,y), direction, and target to move toward
    
    Version Number: 2.0 | Author: Imran Almashoor | Date: 09/08/2024
    """
    def __init__(self, main, canvas, x, y):
        self.main = main
        self.canvas = canvas
        self.speed = NANOBOTSPEED
        self.runOnce = 0

        self.x, self.y = x, y
        self.nanobot = self.canvas.create_oval((self.x, self.y, self.x, self.y), outline='white', width=3)
        self.cosineOfTargetAngle = 0
        self.sineOfTargetAngle = 0

        self.chosenObject = random.choice(self.main.borderCells)
        self.targetX, self.targetY = self.chosenObject.averagePosition
        self.changeCoords()
        self.rotate()

    def changeCoords(self):
        """
        Incrementally updates/moves nanobot toward chosenObject.

        Utilises coordinates recalculated by rotate() and tick() methods.

        Distance from target also recalculated for validation within tick() method.

        Usage :
            self.changeCoords() 
            -> requires no arguments

        Output: None
        """
        self.canvas.moveto(self.nanobot, self.x, self.y)
        self.distanceFromTarget = abs(math.sqrt( ((self.targetX-self.x)**2) + ((self.targetY-self.y)**2) ))

    def rotate(self, event=None):
        """
        Solves for angle between nanobot and chosenObject.

        Angle utilised to move toward chosenObject in straight path.

        Usage :
            self.rotate() 
            -> requires no arguments
            (event paramater is to disregard argument passed by tkinter .bind() method)

        Output: None
        """
        self.targetAngle = math.atan2( (self.targetY-self.y), (self.targetX-self.x) )

        def _rot(x, y):
            """
            codified version of rotation formula of point found on wikipedia.

            preceeding underscore signals function only meant for inner use within Nanobot class only.

            Usage :
                _rot(x, y) 
                -> (int) x
                -> (int) y

            Output: (rotated) x, y coordinates
            """
            x -= self.x
            y -= self.y
            self.cosineOfTargetAngle = math.cos(self.targetAngle)
            self.sineOfTargetAngle = math.sin(self.targetAngle)
            _x = x * self.cosineOfTargetAngle + y * self.sineOfTargetAngle
            _y = -x * self.sineOfTargetAngle + y * self.cosineOfTargetAngle
            return _x + self.x, _y + self.y

        self.x, self.y = _rot(self.x, self.y)

    def tick(self, event=None):
        """
        Run outside of Nanobot class for to modify (x, y) coordinates incrementally.

        Validates for certain conditions to proceed with branching statements and dynamic responses.

        Usage :
            self.tick() 
            -> requires no arguments

        Output: None
        """
        if self.distanceFromTarget > BORDERSIZE + 5:
            self.x += self.speed * self.cosineOfTargetAngle
            self.y += self.speed * self.sineOfTargetAngle

        elif self.main.TargetFound >= TARGET_FOUND_CONDITION and TOGGLE_DELETE_NANOBOTS:
            self.canvas.delete(self.nanobot)

        else:
            self.chosenObject = random.choice(self.main.borderCells)
            self.targetX, self.targetY = self.chosenObject.averagePosition
            self.rotate()

        if self.chosenObject.isTarget and self.runOnce == 0:
            self.runOnce += 1
            self.main.TargetFound += 1
            print(self.main.TargetFound)
            if self.main.TargetFound >= TARGET_FOUND_CONDITION:
                self.main.swarm_target()

        if self.x < BORDERSIZE:
            self.x = BORDERSIZE
            self.y += self.speed * self.sineOfTargetAngle

        elif self.x > self.main.gameWidth - BORDERSIZE:
            self.x = self.main.gameWidth - BORDERSIZE
            self.y += self.speed * self.sineOfTargetAngle

        if self.y < BORDERSIZE:
            self.y = BORDERSIZE
            self.x += self.speed * self.cosineOfTargetAngle

        elif self.y > self.main.gameHeight - BORDERSIZE:
            self.y = self.main.gameHeight - BORDERSIZE
            self.x += self.speed * self.cosineOfTargetAngle

        self.changeCoords()
