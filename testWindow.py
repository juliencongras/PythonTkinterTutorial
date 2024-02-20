import tkinter as tk, tkinter.font as tk_font
from tkinter.ttk import Combobox
from tkinter import *

def new_font():
    print(all_fonts[cb.current()])
    fontName = str(all_fonts[cb.current()])
    lbl.config(font=(fontName, fontSize))

windowWidth = 800
windowHeight = 500
fontSize = 16
fontName = "Comic Sans MS"

window = tk.Tk()
btn = Button(window, text="This is a button", bg="red", fg="blue")
btn.place(x=windowWidth / 2, y=windowHeight / 2)
lbl = Label(window, text="This is a label with a great font.", fg="black", font=(fontName, fontSize))
lbl.place(x=50, y=50)
txtfld = Entry(window, bg="white", fg="black")
txtfld.place(x=50, y=100)

all_fonts = tk_font.families()
cb = Combobox(window, values=all_fonts)
cb.place(x=50, y=150)
cb.bind("<FocusIn>", new_font)

window.title("This is a test")

# window.geometry("widthxheight+XPOS+YPOS") the size and position of the window
window.geometry(f"{windowWidth}x{windowHeight}+10+10")
window.mainloop()
