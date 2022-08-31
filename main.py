import tkinter
import time

FPS = 60

master = tkinter.Tk()
SIZE = [1920, 1080]
objects = []
canvas = tkinter.Canvas(master, width=SIZE[0], height=SIZE[1])
GRAVITY = 0.1

class Oval:
    def __init__(self, x1, y1, x2, y2, color, isPhysics=False, collision=[], mass=1):
        if collision == []:
            collision = [x1, y1, x2, y2]
        self.velocity = {'x': 0, 'y': 0}
        self.size = [x1, y1, x2, y2]
        self.color = color
        self.object = canvas.create_oval((x1, y1), (x2, y2), fill=color)
        self.isPhysics = isPhysics
        objects.append(self)
        self.collision = collision
        self.mass = mass

    def gravity(self):
        if self.isPhysics == True:
            self.velocity['y'] += GRAVITY

        canvas.move(self.object, self.velocity['x'], self.velocity['y'])
        print(self.velocity)

    def move(self, x, y):
        canvas.move(self.object, x, y)

    def addForce(self, x, y):
        self.velocity['x'] += x / self.mass
        self.velocity['y'] += y / self.mass

    def addVelocity(self, x, y):
        self.velocity['x'] += x
        self.velocity['y'] += y

    def setVelocity(self, x, y):
        self.velocity['x'] = x
        self.velocity['y'] = y


canvas.create_rectangle((10, 1000), (1910, 1070), fill="red")
oval = Oval(SIZE[0] // 2 - 50, SIZE[1] // 2 - 50, SIZE[0] // 2 + 50, SIZE[1] // 2 + 50, "green", isPhysics=True)


def move():
    for object in objects:
        object.gravity()



def game():
    global startTime
    endTime = time.time()
    if endTime - startTime != 0:
        print(int(1 // (endTime - startTime)))
    else:
        print("Ошибка")
    startTime = time.time()
    oval.addForce(0, -0.1)

    # canvas.move(oval.object, 0, GRAVITY)

    # global y
    # canvas.create_line((10, y), (100, y), fill="red")
    # y += 1


    move()
    master.after(1000 // 60, game)



canvas.pack()
startTime = time.time()
game()
master.mainloop()







