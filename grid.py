from tkinter import * 
# import everyon
# everything is a widget in tkinter

root = Tk() #root widget. This has to go first.

some_text ="Hello Ninja!"

#Here are are creating the object
myLabel1 = Label(root, text = "This is the start of packing.") 
myLabel2 = Label(root, text = some_text)

#Here we are displaying the object.
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
# No longer stays in the middle when resized.

# You can also chain them together. 
myLabel3 = Label(root, text = "This is more random text. \n Ninja Ninja \n Random text here. \n More Randomness.").grid(row=1, column=1)

#now we need to create an event loop so the screen refreshes. This is where we create the loop.
root.mainloop()
