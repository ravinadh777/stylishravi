from tkinter import*
root = Tk()
root.geometry('500x500')
def open():  
    top = Toplevel(root)  
    top.mainloop()  
    root.title("Welcome To Skyrim")
label_0 = Label(root, text="Log in Page",width=20,font=("bold", 20))
label_0.pack()
Button(root, text='Student',width=20,bg='brown',fg='white').pack()
Button(root, text='Parent',width=20,bg='brown',fg='white').pack()
# it is use for display the registration form on the window
root.mainloop()