from tkinter import *
from PIL import Image, ImageTk

class Chess:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x840")
        self.canvas = Canvas(self.root)
        
        self.img = self.loadImages()
        self.generateGrid()
        self.generateWhite()
        self.generateBlack()
        
        
        self.canvas.pack()
        self.root.mainloop()
        
    ### initialise chess sprite colours
    def color(self, i, j):
        if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
            return 'black'
        else:
            return 'white'
    
    def loadImages(self):
        img1 = ImageTk.PhotoImage((Image.open("./images/b_rook_png_128px.PNG")).resize((100, 100)))
        img2 = ImageTk.PhotoImage((Image.open("./images/b_knight_png_128px.PNG")).resize((100, 100)))
        img3 = ImageTk.PhotoImage((Image.open("./images/b_bishop_png_128px.png")).resize((100, 100)))
        img4 = ImageTk.PhotoImage((Image.open("./images/b_queen_png_128px.PNG")).resize((100, 100)))
        img5 = ImageTk.PhotoImage((Image.open("./images/b_king_png_128px.PNG")).resize((100, 100)))
        img6 = ImageTk.PhotoImage((Image.open("./images/b_bishop_png_128px.PNG")).resize((100, 100)))
        img7 = ImageTk.PhotoImage((Image.open("./images/b_knight_png_128px.PNG")).resize((100, 100)))
        img8 = ImageTk.PhotoImage((Image.open("./images/b_rook_png_128px.PNG")).resize((100, 100)))
        
        pawn = ImageTk.PhotoImage((Image.open("./images/b_pawn_png_128px.PNG")).resize((100, 100)))

        return [img1, img2, img3, img4, img5, img6, img7, img8, pawn]
    
    ## generates chess grid
    def generateGrid(self):
        
        ## generate black cells
        for i in range(8):
            Grid.rowconfigure(self.canvas, i, weight=3)
            
            for j in range(8):
                Grid.columnconfigure(self.canvas, j, weight=1)
                btn = Button(self.canvas, background='black', height=100, width=100)
                btn.grid(row=i, column=j, sticky=N+S+E+W)

        ## generate white cells
        for r in range(0, 8, 2):
            for c in range(0, 8, 2):
                btn = Button(self.canvas, background='white', bd=0)
                btn.grid(row=r, column=c, sticky=N+S+E+W)

        for r in range(1, 8, 2):
            for c in range(1, 8, 2):
                btn = Button(self.canvas, background='white')
                btn.grid(row=r, column=c, sticky=N+S+E+W)
    
    ## white pieces
    def generateWhite(self):
        for i in range(1):
            for j in range(8):
                btn = Button(self.canvas, image=self.img[j], anchor='center', bg=self.color(i, j))
                self.root.bind('<Button-1>')
                btn.grid(row=i, column=j, sticky=N+S+E+W)

        for i in range(1, 2):
            for j in range(8):
                btn = Button(self.canvas, image=self.img[-1], anchor='center', bg=self.color(i, j))
                self.root.bind('<Button-1>')
                btn.grid(row=i, column=j, sticky=N+S+E+W)
    
    ## black pieces
    def generateBlack(self):
        img_copy = self.img.copy()
        img_copy[3], img_copy[4] = img_copy[4], img_copy[3] # swapping king, queen for black side
        
        for i in range(7,8):
            for j in range(8):
                btn = Button(self.canvas, image=img_copy[j], anchor='center', bg=self.color(i, j))
                self.root.bind('<Button-1>')
                btn.grid(row=i, column=j, sticky=N+S+E+W)

        for i in range(6,7):
            for j in range(8):
                btn = Button(self.canvas, image=img_copy[-1], anchor='center', bg=self.color(i, j))
                self.root.bind('<Button-1>')
                btn.grid(row=i, column=j, sticky=N+S+E+W)

chess = Chess()