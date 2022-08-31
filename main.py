import tkinter, time
import InterfaceToTkinter as ITT

FPS = 60

master = tkinter.Tk()
SIZE = [1920, 1080]

canvas = tkinter.Canvas(master, width=SIZE[0], height=SIZE[1])





canvas.create_rectangle((10, 1000), (1910, 1070), fill="red")
oval = ITT.Oval(SIZE[0] // 2 - 50, SIZE[1] // 2 - 50, SIZE[0] // 2 + 50, SIZE[1] // 2 + 50, "green", canvas, isPhysics=True)

keys = []
def press(event):
    keys.append(event.char)

def release(event):
    keys.remove(event.char)

force = 0.5
def move():
    for i in keys:
        if i == 'a':
            oval.addForce(-force, 0)
        if i == 's':
            oval.addForce(0, force)
        if i == 'd':
            oval.addForce(force, 0)
        if i == 'w':
            oval.addForce(0, -force)




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

    # canvas.move(oval.object, 0, GRAVITY)

    # global y
    # canvas.create_line((10, y), (100, y), fill="red")
    # y += 1

    move()
    trace()
    master.after(1000 // 60, game)


master.bind('<KeyPress>', press)
master.bind('<KeyRelease>', release)


canvas.pack()
startTime = time.time()
game()
master.mainloop()







