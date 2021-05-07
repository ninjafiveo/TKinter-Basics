from tkinter import * 
root = Tk() #root widget. This has to go first.

#in tkinter you use an entry widget not input.
e = Entry(root, width= 100, bg="yellow", fg="red", textvariable="Enter your name")
e.insert(0, "Enter your name.")# use insert to add placeholder text. 
e.pack();


#create function - Has to be before the click command in the button.
def myClick():
    myLabel1 = Label(root, text= e.get(), fg="red", bg="#000000") # fg = foreground color. #bg = background color. You can also use hex for color.
    myLabel1.pack()

#myButton = Button(root, text="Click Me", state=DISABLED)#state  not necesary, but you can control it. 
myButton = Button(root, text="Click Me", padx= 50, pady= 50, command=myClick, fg="blue")#you can control the size of the button.
myButton.pack()



root.mainloop()
