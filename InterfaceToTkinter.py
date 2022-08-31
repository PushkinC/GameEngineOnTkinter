import math
objects = []
GRAVITY = 0.1



class Object:
    def __init__(self, x1, y1, x2, y2, color, canvas, isPhysics=False, collision=[], mass=1, resistens=0.01):
        if collision == []:
            collision = [x1, y1, x2, y2]
        self.velocity = {'x': 0, 'y': 0}
        self.size = [x1, y1, x2, y2]
        self.color = color
        self.isPhysics = isPhysics
        objects.append(self)
        self.collision = collision
        self.mass = mass
        self.resistens = resistens
        self.canvas = canvas

    def gravity(self):
        if self.isPhysics == True:
            self.velocity['y'] += GRAVITY

        self.velocity['x'] -= self.velocity['x'] * self.resistens
        self.velocity['y'] -= self.velocity['y'] * self.resistens

        self.canvas.move(self.object, self.velocity['x'], self.velocity['y'])
        print(self.velocity)
        print(self.velocity['y'] * self.resistens)

    def move(self, x, y):
        self.canvas.move(self.object, x, y)

    def addForce(self, x, y):
        self.velocity['x'] += x / self.mass
        self.velocity['y'] += y / self.mass
        print('asdasd')

    def addVelocity(self, x, y):
        self.velocity['x'] += x
        self.velocity['y'] += y

    def setVelocity(self, x, y):
        self.velocity['x'] = x
        self.velocity['y'] = y




class Oval(Object):
    def __init__(self, x1, y1, x2, y2, color, canvas, isPhysics=False, collision=[], mass=1, resistens=0.01):
        super().__init__(x1, y1, x2, y2, color, canvas, isPhysics, collision, mass, resistens)
        self.object = canvas.create_oval((x1, y1), (x2, y2), fill=color)

