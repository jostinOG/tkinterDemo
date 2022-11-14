import tkinter
from tkinter import END

window = tkinter.Tk()
elemento = tkinter.StringVar()
listbox = tkinter.Listbox(window,fg='yellow',bg='grey',activestyle='dotbox')
for item in ["Nachos", "Sandwich", "Burger", "Ruben", "Pizza", "Burrito"]:
    listbox.insert(END, item)
listbox.pack()
label = tkinter.Label(text="Lista de nombres de personas")
label.pack()
window.mainloop()
