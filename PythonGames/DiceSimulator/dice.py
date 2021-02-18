from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import random

rt = tk.Tk()
rt.geometry("600x600")
rt.title("Dice Rolling Simulation")
x1 = tk.Label(rt,text="Game",fg="lightgreen",bg="red",pady= 20,font="20")
x1.pack(expand=True)
dice = ["die1.png","die2.png","die3.png","die4.png","die5.png","die6.png"]
di = ImageTk.PhotoImage(Image.open(random.choice(dice)))
im = tk.Label(rt,image= di)
im.image = di
im.pack(expand= True)
def rolling():
    di = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    im.configure(image = di)
    im.image = di

b = tk.Button(rt,text=" Roll the Dice ",fg="blue",command=rolling)
b.pack(expand=True)

def close():
    rt.destroy()
b1 = tk.Button(rt,text=" Close ",fg="blue",command=close)
b1.pack(expand= True)

rt.mainloop()
