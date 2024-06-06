import customtkinter as ctk
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox

class passta:
    def __init__(self):
        self.login_window = ctk.CTk()
        self.login_window.title('Login')
        self.window_center(self.login_window, 500, 500)
        self.login_window.resizable(width=False, height=False)
        self.login_window.grab_set()
        
        
        #self.login_screen()
        self.open_user_interface()       
        self.login_window.mainloop()
        
    
        
        
        

        
    def login_screen(self):
        brandFont = ctk.CTkFont(family='open sans',size=50)
        buttonFont = ctk.CTkFont(family='open sans',slant='roman')
        loginFrame = ctk.CTkFrame(self.login_window,fg_color='#242424',width=300,height=300)
        loginFrame.grid(row=1,column=0,padx=10,pady=(0,10),columnspan=2)
            
            
            
        brand = ctk.CTkLabel(self.login_window,text='Passta',font=brandFont)
        brand.grid(row=0,column=0,pady=(25,25),sticky='e')
            
            
        self.userNameEntry = ctk.CTkEntry(loginFrame,placeholder_text='Username',width=460,height=40)
        self.userNameEntry.grid(row=0,column=0,columnspan=2,pady=10)
        
        self.passwordEntry = ctk.CTkEntry(loginFrame,placeholder_text='Password',width=460,height=40)
        self.passwordEntry.grid(row=1,column=0,columnspan=2,pady=(0,10),padx=10)
            
        loginButton = ctk.CTkButton(loginFrame,text='Login',fg_color='#48773B',font=buttonFont,command=self.login_user)
        loginButton.grid(row=2,column=0,padx=10,pady=(5,0))
            
        registerButton = ctk.CTkButton(loginFrame,text='Register',fg_color='#48773B',font=buttonFont,command=self.register_user)
        registerButton.grid(row=2,column=1,padx=10,pady=(5,0))
    
    
        
        

        
    def connect_db(self):
        conn = sqlite3.connect('passta.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        conn.commit()
        conn.close()
        
    def register_user(self):
        userName = tk.StringVar()
        password = tk.StringVar()
        userName = self.userNameEntry.get()
        password = self.passwordEntry.get()
        if userName and password:
            conn = sqlite3.connect('passta.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (userName,password) VALUES (?,?)"
                        ,(userName,password))
            conn.commit()
            conn.close()
            
    def login_user(self):
        username = self.userNameEntry.get()
        password = self.passwordEntry.get()
        self.loginFlag = False
        if username and password:
            conn = sqlite3.connect('passta.db')
            c = conn.cursor()
            c.execute("select password from users where userName =?",(username,))
            passwordFetch = c.fetchone()
            if passwordFetch:
                if passwordFetch[0] == password:
                    self.login_window.destroy()
                    self.open_user_interface()
                else:
                    messagebox.showerror('fail','wrong username or password')
            else: messagebox.showerror('fail','wrong username or password')
        else: messagebox.showerror('fail','please enter valid username or password')

    def open_user_interface(self):
        self.user_interface = ctk.CTk()
        self.user_interface.title('Wellcome')
        self.user_interface.geometry('500x500')
        self.user_interface.state('zoomed')
        self.user_interface.mainloop()
            
            
    def window_center(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
            
        x = (screen_width-width)//2
        y = (screen_height-height)//2
            
        window.geometry(f"{width}x{height}+{x}+{y}")
        
passta()