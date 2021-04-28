from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

class PictureEditor:

    # Quits when called
    @staticmethod

    # Opens an image
    def open_app(self, event=None):

        self.canvas.delete(ALL)

        # Opens a window to choose a file=
        self.openfile = askopenfilename(initialdir = "Compressed_13.jpg")

        if self.openfile:

            with open(self.openfile) as _file:
                # if file is selected by user, I'm going to delete
                # the contents inside the canvas widget
                self.canvas.delete(1.0, END)

                self.im = Image.open(self.openfile)

                self.image = ImageTk.PhotoImage(self.im)

                self.a1 = self.canvas.create_image(0, 0, anchor=NW, 
                      image=self.image, tags="image")

                self.image_dim = self.canvas.bbox(self.a1)

                self.imx = self.image_dim[0]

                self.imy = self.image_dim[1]

                # updating text widget
                window.update_idletasks()



    def on_drag(self, event):

        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        self.origx = event.x
        self.origy = event.y


    def on_release(self, event):
        # when I release the mouse, this happens

        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0


        self.newx = event.x
        self.newy = event.y

        # Measures mouse movement from one point to another
        self.movex = self.origx - self.newx
        self.movey = self.origy - self.newy


    def on_motion(self, event):
        # handles the dragging of an object
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y




    def draw(self, event, x1=None, y1=None,x2=None,y2=None):

        # deleting contents of border, if any.
        try:
            self.canvas.delete(self.border)

        except:
            pass

        # if an item is selected
        selection = self.combo.get()

        if selection == 'No Crop':
            x1, y1, x2, y2 = None, None, None, None

        if selection == '2 in x 2 in':

            x1, y1, x2, y2 = self.imx, self.imy, self.imx + 200, self.imy + 200


        if selection == '1 in x 1 in':

            x1, y1, x2, y2 = self.imx, self.imy, self.imx + 100, self.imy + 100


        if selection == 'Passport Size':

            x1, y1, x2, y2 = self.imx, self.imy, self.imx + 132.28, self.imy + 170.079

        if x1 != None or y1 != None or x2 != None or y2 != None:

            self.dimensions = {"x1":x1, "y1":y1, "x2":x2, "y2":y2}

            width = 5

            self.border = self.canvas.create_rectangle(x1+ width, y1 + 
width, x2 + width, y2 + width, width=width, outline="#ffffff", fill ="", 
tags = "rectangle")

        else:
            pass


    def crop(self, event=None):

        # cropping the image

        try:

            self.crop_image = self.im.crop((self.dimensions["x1"] + 
self.movex,
                                        self.dimensions["y1"] + self.movey,
                                        self.dimensions["x2"] + self.movex,
                                        self.dimensions["y2"] + self.movey))

        except:

            print("cropping failed")
            return 1

        self.newly_cropped = ImageTk.PhotoImage(self.crop_image)

        try:
            new_image = self.canvas.create_image(120, 120, 
                        image=self.newly_cropped)
            print("Image is cropped")

        except:

            print("Cropping failed")




    def __init__(self,window):

        frame1 = Frame(bg='red')
        frame1.pack(side=TOP, fill=X)

        frame2height = 600
        frame2width = 600

        frame2 = Frame(window, bd=2, relief=SUNKEN)

        frame2.pack(side=LEFT, fill=X)

        frame3 = Frame(bg='green')
        frame3.pack(side=LEFT, fill=X)

        # Button that open pictures
        open = Button(frame1, text='Open Pic', padx=20, command = 
               self.open_app)

        open.pack(pady=5, padx=5, side=LEFT)

        # Creating a canvas widget
        self.canvas = tk.Canvas(frame2, height=frame2height, 
                      width=frame2width, 
                            bg='gray')

        self.xsb = Scrollbar(frame2, orient="horizontal", 
                         command=self.canvas.xview)
        self.ysb = Scrollbar(frame2, orient="vertical", 
                         command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, 
                          xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0, 0, 1000, 1000))

        # keeps track of data being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}


        # creating image and crop border

        self.canvas.tag_bind("image","<ButtonPress-1>", self.on_drag)
        self.canvas.tag_bind("image","<ButtonRelease-1>", self.on_release)
        self.canvas.tag_bind("image","<B1-Motion>", self.on_motion)

        # widget positions in frame2
        self.xsb.pack(side=BOTTOM, fill=X)
        self.canvas.pack(side=LEFT)
        self.ysb.pack(side=LEFT, fill=Y)

        self.combo = ttk.Combobox(frame1)

        # Combobox selections
        self.combo['values'] = ('No Crop', '2 in x 2 in', '1 in x 1 in', 
                            'Passport Size')
        self.combo.current(0)
        self.combo.pack(pady=5, padx=5, side=LEFT)
        self.combo.bind("<Button-1>", self.draw)

        # Button that crops picture
        self.crop = Button(frame1, text='Crop Pic', padx=20, 
                    command=self.crop)
        self.crop.pack(pady=5, padx=5, side=LEFT)

# this window has all the properties of tkinter.
# .Tk() declares this variable as the frame
window = tk.Tk()

# .title() will input whatever title you want for the app
window.title("ID Picture Generator")

# .geometry() sets the size in pixels of what the window will be
window.geometry("800x600")

app = PictureEditor(window)

# runs everything inside the window
window.mainloop()