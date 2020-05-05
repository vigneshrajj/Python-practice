from tkinter import *
from tkinter import ttk
import os
os.chdir(r"D:\~Programming\Password manager")
import pyperclip

class Retrieve:
    def __init__(self):
        window = Tk()
        window.title("Retrive Details")
        frame = Frame(window)
        frame.pack()
        self.email = Label(frame, text = 'E-mail').grid(row=1, column=2, padx=5,pady=5)
        self.pass_label = Label(frame, text = 'Password').grid(row=1, column=3, padx=5,pady=5)
        self.user_label = Label(frame, text = 'Username').grid(row=1, column=4, padx=5,pady=5)
        self.url_label = Label(frame, text = 'Site').grid(row=1, column=1, padx=5,pady=5)
        i=2
        file=open(r'D:\~Programming\Password manager\User_details.txt','rt')
        for line in file.readlines():
            line_list = line.split(',')
            line_list[-1] = line_list[-1].strip('\n')
            self.email_label = Text(frame, height=1, borderwidth=0, width = 15)
            self.email_label.insert(1.0, line_list[0])
            self.email_label.grid(row=i, column=2, padx=2,pady=2)
            
            self.pass_label = Text(frame, height=1, borderwidth=0, width = 15)
            self.pass_label.insert(1.0, line_list[1])
            self.pass_label.grid(row=i, column=3, padx=5,pady=5)
            
            self.user_label = Text(frame, height=1, borderwidth=0, width = 15)
            self.user_label.insert(1.0, line_list[2])
            self.user_label.grid(row=i, column=4, padx=5,pady=5)
            
            self.url_label = Text(frame, height=1, borderwidth=0, width = 15)
            self.url_label.insert(1.0, line_list[3])
            self.url_label.grid(row=i, column=1, padx=5,pady=5)
            
            i+=1
        window.mainloop()
Retrieve()