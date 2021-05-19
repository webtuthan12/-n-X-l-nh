import os
import sys
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import tkinter as tk
root = Tk()
root.filename2 = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
my_label2 = Label(root, text = root.filename2).pack() 
img = Image.open(root.filename2).convert("RGBA")

w, h = img.size

left = w/4
right = 3*w/4
upper = h/4
lower = 3*h/4

img2 = img.crop([ left, upper, right, lower])
image = ImageTk.PhotoImage(img2)

label = Label(root, image = image)
label.pack()

root.mainloop()