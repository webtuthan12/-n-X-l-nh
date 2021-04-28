from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Image viewer')

root.filename = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

my_label = Label(root, text = root.filename).pack()
img= Image.open(root.filename)
root.mainloop()
img.show()