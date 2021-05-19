import tkinter
from PIL import Image, ImageTk, ImageDraw

image_file = "Compressed_0.jpg"

w = tkinter.Tk()

img = Image.open(image_file)
width, height = img.size
ca = tkinter.Canvas(w, width=width, height=height)
ca.pack()
photoimg = ImageTk.PhotoImage("RGB", img.size)
photoimg.paste(img)
ca.create_image(width//2,height//2, image=photoimg)
tkinter.mainloop()