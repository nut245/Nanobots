import tkinter as tk
import math

class Game:
    def __init__(self, gameWidth, gameHeight):
        self.root = tk.Tk()
        self.root.title("2D stagnant camera")
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.gameWindow()

        self.player = Player(main=self, canvas=self.canvas, x=self.gameWidth / 2, y=self.gameHeight / 2)

        self.canvas.bind("<Motion>", self.targetCoords)

        self.root.mainloop()

    def targetCoords(self, event):
        self.targetX = event.x
        self.targetY = event.y
        self.player.rotate()
        print(f"Target Coords:\t{self.targetX}, {self.targetY}")
        print(f"Player Coords:\t{self.player.x}, {self.player.y}")
        print(f"Distance From Target:\t{self.player.distanceFromTarget}")
        print(f"Angle From Target:\t{self.player.targetAngle}")
        print()

    def gameWindow(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.frame, width=self.gameWidth, height=self.gameHeight, bg="black", takefocus=1)
        self.canvas.pack(fill="both", expand=True)

class Player:
    def __init__(self, main, canvas, x, y):
        self.main = main
        self.canvas = canvas
        self.speed = 0.1

        self.x, self.y = x, y
        self.dot = self.canvas.create_oval((self.x, self.y, self.x, self.y), outline='red', width=3)

        self.distanceFromTarget = 0
        self.tick()

    def changeCoords(self):
        self.canvas.moveto(self.dot, self.x, self.y)
        self.distanceFromTarget = abs(math.sqrt( ((self.main.targetX-self.x)**2) + ((self.main.targetY-self.y)**2) ))

    def rotate(self, keyPressed=None):
        self.targetAngle = math.atan2( (self.main.targetY-self.y), (self.main.targetX-self.x) )

        def _rot(x, y):
            x -= self.x
            y -= self.y
            _x = x * math.cos(self.targetAngle) + y * math.sin(self.targetAngle)
            _y = -x * math.sin(self.targetAngle) + y * math.cos(self.targetAngle)
            return _x + self.x, _y + self.y

        self.x, self.y = _rot(self.x, self.y)

        self.changeCoords()

    def tick(self, keyPressed=None):
        if self.distanceFromTarget > 10:
            self.x += self.speed * math.cos(self.targetAngle)
            self.y += self.speed * math.sin(self.targetAngle)

            self.changeCoords()

        self.canvas.after(1, self.tick)

if __name__ == '__main__':
    Game(600, 600)