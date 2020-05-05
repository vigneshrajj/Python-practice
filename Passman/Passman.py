from tkinter import *
from tkinter import ttk
import re,os
import string,pyperclip
os.chdir(r"D:\~Programming\Password manager")
from PasswordManager import *
from RetrievalScreen import *
from random import *

class Pass_screen():
    def __init__(self):
        
        window = Tk()
        window.title("Login")
        
        frame = Frame(window)
        frame.pack()
        
        self.pass_Label = Label(frame, text = "Password").grid(row=1, column=1, padx=5,pady=5)
        self.pass_entry = Entry(frame, show='*', width=20)
        self.pass_entry.grid(row=1, column=2,padx=5,pady=5)
        
        self.submit = Button(frame, text = "Submit", command=self.insert).grid(row=1,column = 3,padx=5,pady=5)
        window.bind('<Return>', (lambda event: self.insert()))
        window.mainloop()
        
    def insert(self):
        password_info = self.pass_entry.get()
        if(password_info =='Random'):
            self.pass_entry.delete(0, END)
            Start_screen()
        else:
            self.pass_entry.delete(0, END)

class Start_screen():
    def __init__(self):
        window = Tk()
        window.title("Choose Action")
        
        frame = Frame(window)
        frame.pack()
        
        enter = Button(frame, text = "Enter details", command = Passman).grid(row=1,column = 1,padx=5,pady=5)
        retrieve = Button(frame, text = "Retrieve Details", command = Retrieve).grid(row = 2, column = 1, padx = 5, pady = 5)
        window.mainloop()
        
Pass_screen()