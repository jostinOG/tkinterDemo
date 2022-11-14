import tkinter

window = tkinter.Tk()
label1 = tkinter.Label(window, text='posicoon', bg='blue', fg='white')
label1.place(x=10,y=50)
label2 = tkinter.Label(window, text='dddd', bg='blue', fg='white')
label2.place(relx=10,rely=50,relwidth=10,anchor='n')

window.mainloop()
