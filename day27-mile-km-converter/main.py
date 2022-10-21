from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=100, height=100)

blank = Label(text="")
blank.grid(column=2, row=0)

entry = Entry(width=30)
entry.insert(END, string="10")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

converted_value = Label(text="0")
converted_value.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

def convert():
    value = int(entry.get()) * 1.61
    converted_value.config(text=f"{value}")
button = Button(text="Click Me", command=convert)
button.grid(column=1, row=2)

window.mainloop()