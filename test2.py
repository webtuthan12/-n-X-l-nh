# run this in any directory
# add -v for verbose
# get Pillow (fork of PIL) from
# pip before running -->
# pip install Pillow

# import required libraries
import os
import sys
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import tkinter as tk


def myClick():
    root.filename = filedialog.askopenfilename(initialdir="C:", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text = root.filename)
    pic = Image.open(root.filename)
    pic.thumbnail((350,350))
    pic = ImageTk.PhotoImage(pic)
    pic_label1.configure(image=pic)
    pic_label1.image = pic
def compress():
    def compressMe(file, verbose = False):
	
	
	
	# open the image
	    picture = Image.open(root.filename)
	
	# Save the picture with desired quality
	# To change the quality of image,
	# set the quality variable at
	# your desired level, The more
	# the value of quality variable
	# and lesser the compression

	    picture.save("Compressed_"+file,
				"JPEG",
				optimize = True,
				quality = 50)

	    return

# Define a main function
    def main():
	
	    verbose = False
	
	# checks for verbose flag
	    if (len(sys.argv)>1):
		
		    if (sys.argv[1].lower()=="-v"):
			    verbose = True
					
	# finds current working dir
	    cwd = os.getcwd()

	    formats = ('.jpg', '.jpeg')
	
	# looping through all the files
	# in a current directory
	    for file in os.listdir(cwd):
		
		# If the file format is JPG or JPEG
		    if os.path.splitext(file)[1].lower() in formats:
			    print('compressing', file)
			    compressMe(file, verbose)

	    print("Done")

# Driver code
    if __name__ == "__main__":
	    main()

def crop1():
	root.filename2 = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label2 = Label(root, text = root.filename2)
	img = Image.open(root.filename2).convert("RGBA")

	w, h = img.size

	left = w*0
	right = w*0.5
	upper = h*0
	lower = h*0.5

	img2 = img.crop([ left, upper, right, lower])
	img2.thumbnail((350,350))
	image = ImageTk.PhotoImage(img2)

	label = Label(root, image = image)
	label.grid(row=5, column=3)


	root.mainloop()

def crop2():
	root.filename2 = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label2 = Label(root, text = root.filename2) 
	img = Image.open(root.filename2).convert("RGBA")

	w, h = img.size

	left = w*0.5
	right = w
	upper = h*0
	lower = h*0.5

	img2 = img.crop([ left, upper, right, lower])
	img2.thumbnail((350,350))
	image = ImageTk.PhotoImage(img2)

	label = Label(root, image = image)
	label.grid(row=5, column=3)

	root.mainloop()

def crop3():
	root.filename2 = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label2 = Label(root, text = root.filename2) 
	img = Image.open(root.filename2).convert("RGBA")

	w, h = img.size

	left = w*0
	right = w*0.5
	upper = h*0.5
	lower = h

	img2 = img.crop([ left, upper, right, lower])
	img2.thumbnail((350,350))
	image = ImageTk.PhotoImage(img2)

	label = Label(root, image = image)
	label.grid(row=5, column=3)

	root.mainloop()

def crop4():
	root.filename2 = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label2 = Label(root, text = root.filename2)
	img = Image.open(root.filename2).convert("RGBA")

	w, h = img.size

	left = w*0.5
	right = w
	upper = h*0.5
	lower = h

	img2 = img.crop([ left, upper, right, lower])
	img2.thumbnail((350,350))
	image = ImageTk.PhotoImage(img2)

	label = Label(root, image = image)
	label.grid(row=5, column=3)

	root.mainloop()

def crop5():
	root.filename2 = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_label2 = Label(root, text = root.filename2)
	img = Image.open(root.filename2).convert("RGBA")

	w, h = img.size

	left = w/4
	right = 3*w/4
	upper = h/4
	lower = 3*h/4

	img2 = img.crop([ left, upper, right, lower])
	img2.thumbnail((350,350))
	image = ImageTk.PhotoImage(img2)

	label = Label(root, image = image)
	label.grid(row=5, column=3)

	root.mainloop()
root = Tk() 

frm = Frame(root)
frm.grid(ipadx=15, ipady=15)

pic_label1 = Label(root)
pic_label1.grid(row=5, column=0)

pic_label2 = Label(root)
pic_label2.grid(row=5, column=3)

myButton = Button(root, text="Open",padx=20, pady=10 , command=myClick)

button_compress = Button(root, text="Compress",padx=20, pady=10 , command=compress)

button_crop1 = Button(root, text="Crop1",padx=20, pady=10 , command=crop1)
button_crop2 = Button(root, text="Crop2",padx=20, pady=10 , command=crop2)
button_crop3 = Button(root, text="Crop3",padx=20, pady=10 , command=crop3)
button_crop4 = Button(root, text="Crop4",padx=20, pady=10 , command=crop4)
button_crop5 = Button(root, text="Crop5",padx=20, pady=10 , command=crop5)

button_quit = Button(root, text="ExitProgram",padx=20, pady=10 , command=root.quit)

myButton.grid(row=1, column=0)
button_compress.grid(row=1, column=1)
button_crop1.grid(row=2, column=0)
button_crop2.grid(row=2, column=1)
button_crop3.grid(row=2, column=2)
button_crop4.grid(row=3, column=0)
button_crop5.grid(row=3, column=1)
button_quit.grid(row=4, column=0)

root.mainloop()