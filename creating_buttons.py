from tkinter import * 
root = Tk() #root widget. This has to go first.

#create function - Has to be before the click command in the button.
def myClick():
    myLabel1 = Label(root, text= "Look I make a button do something.", fg="red", bg="#000000") # fg = foreground color. #bg = background color. You can also use hex for color.
    # myLabel1.pack()
    myLabel1.grid(row=1, column=0)
    myLabel2 = Label(root, text= "Label Two Text", fg="gray", bg="#ffffff") # fg = foreground color. #bg = background color. You can also use hex for color.
    myLabel2.grid(row=2, column=0)

#myButton = Button(root, text="Click Me", state=DISABLED)#state  not necesary, but you can control it. 
myButton = Button(root, text="Click Me", padx= 50, pady= 50, command=myClick, fg="blue")#you can control the size of the button.
# myButton.pack()
myButton.grid(row=0, column=0)


root.mainloop()
