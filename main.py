import pprint
import tkinter

window = tkinter.Tk()
label_saludo = tkinter.Label(window, text='hola',bg='red',foreground='blue')
label_saludo.pack(ipadx=60,ipady=50,expand=True,side='left')
label_adios = tkinter.Label(window, text='ADIOS',bg='red',foreground='white')
label_adios.pack(fill='both',expand=True,side='right')

window.mainloop()

# print(type(window))
# pprint.pprint(dir(window))
