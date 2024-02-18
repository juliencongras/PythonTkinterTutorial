import tkinter as tk
from tkinter import *

windowWidth = 800
windowHeight = 500

window = tk.Tk()
btn = Button(window, text="This is a button", bg="red", fg="blue")
btn.place(x=windowWidth/2, y=windowHeight/2)
window.title("This is a test")
# window.geometry("widthxheight+XPOS+YPOS") the size and position of the window
window.geometry(f"{windowWidth}x{windowHeight}+10+10")
window.mainloop()
