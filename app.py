from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

jan = Tk()
jan.title("System - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

logo = PhotoImage(file="icons/icon.png")

LeftFrame = Frame(jan, width=200, height=300, bg="#FFD700", relief="raised")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="#FFD700", relief="raised")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="#FFD700")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username: ", font=("Century Gothic", 20), bg="#FFD700", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password: ", font=("Century Gothic", 20), bg="#FFD700", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    database.cursor.execute(""" 
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))

    VerifyLogin = database.cursor.fetchone()
    

    if VerifyLogin:  # Verifica se VerifyLogin não é None
        messagebox.showinfo(title="Login Info", message="Acesso confirmado. Bem vindo!")
    else:
        messagebox.showerror(title="Login Info", message="Acesso negado. Verifique se está cadastrado no sistema!")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)  # Corrigindo o comando para chamar a função Login
LoginButton.place(x=100, y=200)


def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    NameLabel = Label(RightFrame, text="Name: ", font=("Century Gothic", 20), bg="#FFD700", fg="white")
    NameLabel.place(x=5, y=5)

    NameEntry = Entry(RightFrame, width=39)
    NameEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="E-mail: ", font=("Century Gothic", 20), bg="#FFD700", fg="white")
    EmailLabel.place(x=5, y=50)

    EmailEntry = Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=60)

    def RegisterToDataBase(): 
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Não deixe nenhum campo vazio. Preencha todos os campos.")
            return
        else:
            database.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)
            """, (Name, Email, User, Pass))  
            database.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)  
    Register.place(x=100, y=225)

    def BackToLogin():
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125,y=260)


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()
