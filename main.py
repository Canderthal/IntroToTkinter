from tkinter import *


def button_clicked():
    print("I got pressed")
    new_text = input.get()
    first_label.config(text=new_text)

#Creates Window
window = Tk()
window.title("My first gui program")
window.minsize(width=500, height=500)

first_label = Label(text="I am a label", font=("Arial", 24, "bold"))
first_label.pack()


button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()


window.mainloop()