from tkinter import * 
# import everyon
# everything is a widget in tkinter

root = Tk() #root widget. This has to go first.

some_text ="Hello Ninja!"

myLabel = Label(root, text = "This is the start of packing.") #Created a label widget, but now it needs to go into the root widget. We're going to pack it in there. This is just one method.

# Shoving  the label on to the screen.
myLabel.pack()

myLabel2 = Label(root, text = some_text)
myLabel2.pack()

#now we need to create an event loop so the screen refreshes. This is where we create the loop.
root.mainloop()

# https://www.youtube.com/watch?v=YXPyB4XeYLA



















