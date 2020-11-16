import tkinter as tk
from tkinter import *
import string
from random import *

# from tkinter import filedialog, Text
HEIGHT= 250
WIDTH = 250

# set background of window to white and size
root = tk.Tk()
root.configure(background='white')
root.geometry('500x500')

# this function generates a random password for the user
def new_password():
    char = string.ascii_letters + string.digits + string.punctuation
    pswd = "".join(choice(char) for x in range(randint(10, 20)))
    myLabel = Label(root, text= "Your new password is: \n" + pswd , bg='#800000')
    myLabel.place(relx=0.35, rely=0.3)
    myLabel.configure(font=("Ubuntu Light", 10, "italic"))

# This is my Frame
frame = tk.Frame(root, bg= '#800000')
frame.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8) 

# This is the UNCRACKABLE LABEL
UC = tk.Label(frame, text='WELCOME TO UNCRACKABLE', bg= '#800000')
UC.place(relx=0.2, rely=0.1)
UC.configure(font=("Ubuntu Light", 12, "italic"))


# GENERATE PASSWORD BUTTON IS HERE
button = tk.Button(frame, text='GET A PASSWORD', command=new_password)
button.place(relx=0.3, rely=0.4, width=150, height=50)
button.configure(font=("Ubuntu Light", 10, "italic"))


root.mainloop()