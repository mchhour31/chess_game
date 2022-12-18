from tkinter import *

def generateGrid():
    root = Tk()
    root.geometry('1100x850')
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    frame = Frame(root)
    frame.grid(row=0, column=0, sticky=N+S+E+W)

    for row in range(8):
        Grid.rowconfigure(frame, row, weight=1)
        
        for col in range(8):
            Grid.columnconfigure(frame, col, weight=1)
            btn = Button(frame, bg='black', bd=0)
            btn.grid(row=row, column=col, sticky=N+S+E+W)

    x = 0
    for r in range(0, 8, 2):
        for c in range(0, 8, 2):
            btn = Button(frame, bg='white', bd=0)
            btn.grid(row=r, column=c, sticky=N+S+E+W)

    for r in range(1, 8, 2):
        for c in range(1, 8, 2):
            btn = Button(frame, bg='white', bd=0)
            btn.grid(row=r, column=c, sticky=N+S+E+W)
            
    root.mainloop()



generateGrid()

