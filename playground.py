from tkinter import *
window = Tk()
window.title("My first gui program")
window.minsize(width=200, height=50)
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

def conversion():
    miles =float(miles_entry.get())
    converted = miles * 1.6
    kilo_label.config(text=converted)

miles_entry = Entry(width=10)
miles_entry.grid(column=0, row=0)
miles_entry.insert(END, string="0")

miles_label = Label(text="Miles")
miles_label.grid(column=1, row=0)

text = Label(text="is equal to ")
text.grid(column=2, row=0)

kilo_label = Label(text="0")
kilo_label.grid(column=3, row=0)

km_label = Label(text="Km")
km_label.grid(column=4, row=0)

converssion_buttom = Button(text="Convert", command=conversion)
converssion_buttom.grid(column=2, row=1)
#km_text = Label(converted)









window.mainloop()