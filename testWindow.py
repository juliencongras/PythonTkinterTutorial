import tkinter as tk
from tkinter import *

windowWidth = 800
windowHeight = 500

window = tk.Tk()
btn = Button(window, text="This is a button", bg="red", fg="blue")
btn.place(x=windowWidth/2, y=windowHeight/2)
lbl = Label(window, text="This is a label with a great font.", fg="black", font=("Comic Sans MS", 16))
lbl.place(x=50, y=50)
txtfld = Entry(window, bg="white", fg="black")
txtfld.place(x=50, y=100)
window.title("This is a test")
# window.geometry("widthxheight+XPOS+YPOS") the size and position of the window
window.geometry(f"{windowWidth}x{windowHeight}+10+10")
window.mainloop()
