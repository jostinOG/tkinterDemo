import tkinter


def selec():
    list.config(text="Has seleccionado la opción {}".format(opcion.get()))


window = tkinter.Tk()

opcion = tkinter.IntVar()  # Como StrinVar pero en entero

tkinter.Radiobutton(window, text="Opción 1", variable=opcion,
                    value=1, command=selec).pack()
tkinter.Radiobutton(window, text="Opción 2", variable=opcion,
                    value=2, command=selec).pack()
tkinter.Radiobutton(window, text="Opción 3", variable=opcion,
                    value=3, command=selec).pack()

list = tkinter.Label(window)
list.pack()


def reset():
    opcion.set(None)  # Reiniciamos el seleccionable
    list.config(text='')  # Reiniciamos la etiqueta


tkinter.Button(window, text="Reiniciar", command=reset).pack()
window.mainloop()
