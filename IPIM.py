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

root = Tk()

root.filename = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

my_label = Label(root, text = root.filename).pack()
root.mainloop()
# define a function for
# compressing an image
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

root = Tk()

root.filename2 = filedialog.askopenfilename(initialdir="C:/Users/maste/OneDrive/Desktop/Image Processing In Medical/Code", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

my_label2 = Label(root, text = root.filename2).pack()
root.mainloop()

compress = Image.open(root.filename2)
compress.show()