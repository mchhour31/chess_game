from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io

# def toggle():
#     if btn.config('relief')[-2] == 'sunken':
#         btn.config(relief="raised")
#     else:
#         btn.config(relief="sunken")

root = Tk()
root.geometry('1000x840')
# Grid.rowconfigure(root, 1, weight=1)
# Grid.columnconfigure(root, 1, weight=1)

# frame = Frame(root)
# frame.grid(row=0, column=0, sticky=N+S+E+W)
# a = 0
# b = 0

# w, h = 100, 100

img1 = ImageTk.PhotoImage((Image.open("./images/b_rook_png_128px.PNG")).resize((100, 100)))
img2 = ImageTk.PhotoImage((Image.open("./images/b_knight_png_128px.PNG")).resize((100, 100)))
img3 = ImageTk.PhotoImage((Image.open("./images/b_bishop_png_128px.png")).resize((100, 100)))
img4 = ImageTk.PhotoImage((Image.open("./images/b_queen_png_128px.PNG")).resize((100, 100)))
img5 = ImageTk.PhotoImage((Image.open("./images/b_king_png_128px.PNG")).resize((100, 100)))
img6 = ImageTk.PhotoImage((Image.open("./images/b_bishop_png_128px.PNG")).resize((100, 100)))
img7 = ImageTk.PhotoImage((Image.open("./images/b_knight_png_128px.PNG")).resize((100, 100)))
img8 = ImageTk.PhotoImage((Image.open("./images/b_rook_png_128px.PNG")).resize((100, 100)))

img = [img1, img2, img3, img4, img5, img6, img7, img8]

canvas = Canvas(root)


# def callback(e):
#     global img2
#     img2 = ImageTk.PhotoImage((Image.open("./images/b_king_png_128px.png")))
#     bg2 = canvas.create_image(e.x, e.y, image=img2)



for i in range(8):
    Grid.rowconfigure(canvas, i, weight=3)
    
    for j in range(8):
        Grid.columnconfigure(canvas, j, weight=1)
        btn = Button(canvas, background='black', height=100, width=100)
        # img2 = ImageTk.PhotoImage((Image.open("./images/b_king_png_128px.png")).resize((w, h), Image.Resampling.LANCZOS))
        # bg2 = canvas.create_image(50, 50, image=img[i])
        # canvas.tag_bind(bg2, "<Button-1>", callback)        
        # btn = Button(, bg='white', bd=0, image=img[i] )
        btn.grid(row=i, column=j, sticky=N+S+E+W)

# for row in range(8):
#     Grid.rowconfigure(canvas, row, weight=1)
    
#     for col in range(8):
#         Grid.columnconfigure(canvas, col, weight=1)
#         btn = Button(canvas, background='black', bd=0, command=callback)
#         btn.grid(row=row, column=col, sticky=N+S+E+W)

for r in range(0, 8, 2):
    for c in range(0, 8, 2):
        btn = Button(canvas, background='white', bd=0, height=100, width=100)
        btn.grid(row=r, column=c, sticky=N+S+E+W)

for r in range(1, 8, 2):
    for c in range(1, 8, 2):
        btn = Button(canvas, background='white', bd=0, height=100, width=100)
        btn.grid(row=r, column=c, sticky=N+S+E+W)

for i in range(1):
    for j in range(8):
        btn = Button(canvas, image=img[j], anchor='center')
        
        btn.grid(row=i, column=j, sticky=N+S+E+W)

root.configure(bg='')
# bg = canvas.create_image(150,150, image=img1)
# canvas.tag_bind(bg)



# img2 = PhotoImage(file="./images/.png")
# img4 = PhotoImage(file="./images/.png")
# img5 = PhotoImage(file="./images/.png")
# img6 = PhotoImage(file="./images/.png")
# img7 = PhotoImage(file="./images/.png")
# img8 = PhotoImage(file="./images/.png")




# img1 = PhotoImage(file="./images/b_rook_png_128px.png")

canvas.pack()
root.mainloop()

