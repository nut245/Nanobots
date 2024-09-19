import tkinter as tk
import random
import math

BORDERSIZE = 50
NANOBOTSPEED = 3
FPS_MS = 1
NANOBOT_NUMBER = 200
TARGET_FOUND_CONDITION = 20
SPEEDUP_WHEN_TARGET_FOUND = False
TOGGLE_DELETE_NANOBOTS = False

class Main:
    def __init__(self, gameWidth, gameHeight):
        self.root = tk.Tk()
        self.root.title("Nanobot Program")
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.gameWindow()

        self.objectsHistoryDatabase = []

        self.createBorder()

        self.targetCell = random.choice(self.objectsHistoryDatabase)
        self.targetCell.becomeTarget()
        self.TargetFound = 0
        self.nanobots = []
        for _ in range(NANOBOT_NUMBER):
            self.nanobots.append(NanoBot(main=self, canvas=self.canvas, x=random.randint(BORDERSIZE, gameWidth-BORDERSIZE), y=random.randint(BORDERSIZE, gameHeight-BORDERSIZE)))

        self.move_nanobots()

        self.root.mainloop()

    def move_nanobots(self):
        for nanobot in self.nanobots:
            nanobot.tick()
        self.root.after(FPS_MS, self.move_nanobots)

    def swarm_target(self):
        for nanobot in self.nanobots:
            nanobot.targetX, nanobot.targetY = self.targetCell.averagePosition
            nanobot.rotate()
        if SPEEDUP_WHEN_TARGET_FOUND:
            for nanobot in self.nanobots:
                nanobot.speed = NANOBOTSPEED * 5

    def gameWindow(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.frame, width=self.gameWidth, height=self.gameHeight, bg="black", takefocus=1)
        self.canvas.pack(fill="both", expand=True)

    def createBorder(self):
        numberOfObjectsAcrossWidth = self.gameWidth / BORDERSIZE * 2
        numberOfObjectsAcrossHeight = self.gameHeight / BORDERSIZE * 2
        def accrossWidth(self):
            position = BORDERSIZE
            height = 0
            for _ in range(int(numberOfObjectsAcrossWidth)):
                self.objectsHistoryDatabase.append(Object(main=self, canvas=self.canvas, x=position, y=height))
                if position >= self.gameWidth - BORDERSIZE * 2:
                    position = BORDERSIZE
                    height = self.gameHeight - BORDERSIZE
                else:
                    position += BORDERSIZE
        def accrossHeight(self):
            position = BORDERSIZE
            width = 0
            for _ in range(int(numberOfObjectsAcrossHeight)):
                self.objectsHistoryDatabase.append(Object(main=self, canvas=self.canvas, x=width, y=position))
                if position >= self.gameHeight - BORDERSIZE * 2:
                    position = BORDERSIZE
                    width = self.gameWidth - BORDERSIZE
                else:
                    position += BORDERSIZE            
        accrossWidth(self)
        accrossHeight(self)

class NanoBot:
    def __init__(self, main, canvas, x, y):
        self.main = main
        self.canvas = canvas
        self.speed = NANOBOTSPEED
        self.runOnce = 0

        self.x, self.y = x, y
        self.nanobot = self.canvas.create_oval((self.x, self.y, self.x, self.y), outline='white', width=3)

        self.chosenObject = random.choice(self.main.objectsHistoryDatabase)
        self.targetX, self.targetY = self.chosenObject.averagePosition
        self.changeCoords()
        self.rotate()

    def changeCoords(self):
        self.canvas.moveto(self.nanobot, self.x, self.y)
        self.distanceFromTarget = abs(math.sqrt( ((self.targetX-self.x)**2) + ((self.targetY-self.y)**2) ))

    def rotate(self, keyPressed=None):
        self.targetAngle = math.atan2( (self.targetY-self.y), (self.targetX-self.x) )

        def _rot(x, y):
            x -= self.x
            y -= self.y
            _x = x * math.cos(self.targetAngle) + y * math.sin(self.targetAngle)
            _y = -x * math.sin(self.targetAngle) + y * math.cos(self.targetAngle)
            return _x + self.x, _y + self.y

        self.x, self.y = _rot(self.x, self.y)

        self.changeCoords()

    def tick(self, keyPressed=None):
        if self.distanceFromTarget > BORDERSIZE + 5:
            self.x += self.speed * math.cos(self.targetAngle)
            self.y += self.speed * math.sin(self.targetAngle)
            self.changeCoords()

        elif self.main.TargetFound >= TARGET_FOUND_CONDITION:
            if TOGGLE_DELETE_NANOBOTS:
                self.canvas.delete(self.nanobot)

        else:
            self.chosenObject = random.choice(self.main.objectsHistoryDatabase)
            self.targetX, self.targetY = self.chosenObject.averagePosition
            self.rotate()
            self.distanceFromTarget = abs(math.sqrt( ((self.targetX-self.x)**2) + ((self.targetY-self.y)**2) ))

        if self.chosenObject.isTarget and self.runOnce == 0:
            self.runOnce += 1
            self.main.TargetFound += 1
            print(self.main.TargetFound)
            if self.main.TargetFound >= TARGET_FOUND_CONDITION:
                self.main.swarm_target()

        if self.x < BORDERSIZE:
            self.x = BORDERSIZE
            self.y += self.speed * math.sin(self.targetAngle)
            self.changeCoords()

        elif self.x > self.main.gameWidth - BORDERSIZE:
            self.x = self.main.gameWidth - BORDERSIZE
            self.y += self.speed * math.sin(self.targetAngle)
            self.changeCoords()

        if self.y < BORDERSIZE:
            self.y = BORDERSIZE
            self.x += self.speed * math.cos(self.targetAngle)
            self.changeCoords()

        elif self.y > self.main.gameHeight - BORDERSIZE:
            self.y = self.main.gameHeight - BORDERSIZE
            self.x += self.speed * math.cos(self.targetAngle)
            self.changeCoords()

class Object:
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

if __name__ == "__main__":
    Main(gameWidth=1000, gameHeight=700)