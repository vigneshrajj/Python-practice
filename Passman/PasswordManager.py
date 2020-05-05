from tkinter import *
import os,re
os.chdir(r"D:\~Programming\Password manager")
import string,pyperclip
from random import *


class Passman:
    def __init__(self):
        window = Tk()
        window.title("Enter Details")
        
        frame = Frame(window)
        frame.pack()
        self.email_Label = Label(frame, text = "Emaid ID").grid(row=1, column=1, padx=5,pady=5)
        self.email_entry = Entry(frame, text = "asdf@gmail.com")
        self.email_entry.grid(row=1, column=2,padx=5,pady=5)
        
        
        self.pass_Label = Label(frame, text = "Password").grid(row=2, column=1, padx=5,pady=5)
        self.pass_entry = Entry(frame, show='*', width=20)
        
        self.pass_entry.grid(row=2, column=2,padx=5,pady=5)
        
        copy_to_clip = Button(frame, text = "Copy", command=pyperclip.copy(self.pass_entry.get())).grid(row=2,column = 3,padx=5,pady=5)
        generate = Button(frame, text = "Generate", command=self.generate).grid(row=2,column = 4,padx=5,pady=5)
        self.username_Label = Label(frame, text = "Username").grid(row=3, column=1, padx=5,pady=5)
        self.username_entry = Entry(frame)
        self.username_entry.grid(row=3, column=2,padx=5,pady=5)
        
        self.url_Label = Label(frame, text = "Website").grid(row=4, column=1, padx=5,pady=5)
        self.url_entry = Entry(frame, width=20)
        self.url_entry.grid(row=4, column=2,padx=5,pady=5)
        window.bind('<Return>', (lambda event: self.insert()))
        submit = Button(frame, text = "Submit", command=self.insert).grid(row=5,column = 3,padx=5,pady=5)
        reset = Button(frame, text = "Reset", command=self.reset).grid(row=5,column = 4,padx=5,pady=5)

        window.mainloop()
    def insert(self):
        username_info = self.username_entry.get()
        email_info = self.email_entry.get()
        password_info = self.pass_entry.get()
        url_info = self.url_entry.get()
        
        file=open(r'D:\~Programming\Password manager\User_details.txt','at')
        file.write(email_info + ','+ password_info +','+ username_info + ',' + url_info + '\n')
        file.close()
        self.reset()

    def reset(self):
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.pass_entry.delete(0, END)
        self.url_entry.delete(0, END)
    
    def generate(self):
        characters = string.ascii_letters + string.punctuation  + string.digits
        characters = characters.replace(',',':')
        password =  "".join(choice(characters) for x in range(randint(12, 16)))
        self.pass_entry.delete(0, END)
        self.pass_entry.insert(0, password)

Passman()
