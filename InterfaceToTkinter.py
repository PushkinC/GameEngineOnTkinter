
objects = []
GRAVITY = 0.1

class Oval:
    def __init__(self, x1, y1, x2, y2, color, canvas, isPhysics=False, collision=[], mass=1, resistens=0.01):
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
        self.resistens = resistens
        self.canvas = canvas

    def gravity(self):
        if self.isPhysics == True:
            self.velocity['y'] += GRAVITY


        self.velocity['x'] -= self.velocity['x'] * self.resistens
        self.velocity['y'] -= self.velocity['y'] * self.resistens

        self.canvas.move(self.object, self.velocity['x'], self.velocity['y'])
        print(self.velocity)

    def move(self, x, y):
        self.canvas.move(self.object, x, y)

    def addForce(self, x, y):
        self.velocity['x'] += x / self.mass
        self.velocity['y'] += y / self.mass

    def addVelocity(self, x, y):
        self.velocity['x'] += x
        self.velocity['y'] += y

    def setVelocity(self, x, y):
        self.velocity['x'] = x
        self.velocity['y'] = y

    # def bind(self, tk, ref, func):
    #     tk.bind(ref, func)

