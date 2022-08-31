# import tkinter
#
# master = tkinter.Tk()
# size = [1920, 1080]
# canvas = tkinter.Canvas(master, width=size[0], height=size[1])

base = []

class Oval():
    def __init__(self, a):
        a.append(self)

a = Oval(base)

print(base)




