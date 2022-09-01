import tkinter, time
import InterfaceToTkinter as ITT

FPS = 60

master = tkinter.Tk()
SIZE = [1920, 1080]

canvas = tkinter.Canvas(master, width=SIZE[0], height=SIZE[1])





# canvas.create_rectangle((10, 1000), (1910, 1070), fill="red")
rec = ITT.Rectangle(10, 1000, 1910, 1070, 'red', canvas, isPhysics=False, resistens=0.01)
rec1 = ITT.Rectangle(1000, 900, 1910, 960, 'red', canvas, isPhysics=True, resistens=0.01)
oval = ITT.Oval(SIZE[0] // 2 - 50, SIZE[1] // 2 - 50, SIZE[0] // 2 + 50, SIZE[1] // 2 + 50, "green", canvas, isPhysics=True, resistens=0.01)

keys = []
force = 1

canJump = False

def collisionEnter(event):
    global canJump
    canJump = True

def press(event):
    global canJump
    i = event.char
    if i == 'a':
        oval.addForce(-force, 0)
    if i == 's':
        oval.addForce(0, force)
    if i == 'd':
        oval.addForce(force, 0)
    if i == 'w':
        if canJump:
            oval.addForce(0, -force * 10)
            canJump = False




def trace():
    for object in ITT.objects:
        object.gravity()



def game():
    global startTime
    endTime = time.time()
    if endTime - startTime != 0:
        print(int(1 // (endTime - startTime)))
    else:
        print("Ошибка")
    startTime = time.time()


    trace()
    master.after(1000 // 60, game)


master.bind('<KeyPress>', press)



canvas.pack()
ITT.collisionEnter = collisionEnter
startTime = time.time()
game()
master.mainloop()







