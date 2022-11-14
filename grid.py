import tkinter

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
username = tkinter.Label(window, text='Username:')
username.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
username_entry=tkinter.Entry(window)
username_entry.grid(column=1,row=0,sticky=tkinter.E,padx=5,pady=5)
password = tkinter.Label(window, text='Password:')
password.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

password_entry=tkinter.Entry(window,show='*')
password_entry.grid(column=1,row=1,sticky=tkinter.E,pady=5,padx=5)

login_button=tkinter.Button(window,text='Login')
login_button.grid(column=1,row=3,sticky=tkinter.E,padx=5,pady=5)

window.mainloop()
