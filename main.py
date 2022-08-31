import tkinter, time
import InterfaceToTkinter as ITT

FPS = 60

master = tkinter.Tk()
SIZE = [1920, 1080]

canvas = tkinter.Canvas(master, width=SIZE[0], height=SIZE[1])





canvas.create_rectangle((10, 1000), (1910, 1070), fill="red")
oval = ITT.Oval(SIZE[0] // 2 - 50, SIZE[1] // 2 - 50, SIZE[0] // 2 + 50, SIZE[1] // 2 + 50, "green", canvas, isPhysics=True)


def move():
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
    master.after(1000 // 60, game)




canvas.pack()
startTime = time.time()
game()
master.mainloop()







