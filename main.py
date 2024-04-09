import streamlit as st
import database

def login():
    st.title("System - Access Panel")
    st.sidebar.image("icons/icon.png")
    
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        verify_login = database.cursor.execute(""" 
            SELECT * FROM Users
            WHERE (User = ? and Password = ?)
            """, (username, password)).fetchone()

        if verify_login:
            st.success("Acesso confirmado. Bem vindo!")
        else:
            st.error("Acesso negado. Verifique se está cadastrado no sistema!")

def register():
    st.title("System - Registration Panel")
    st.sidebar.image("icons/icon.png")

    name = st.text_input("Name:")
    email = st.text_input("E-mail:")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Register"):
        if name == "" or email == "" or username == "" or password == "":
            st.error("Não deixe nenhum campo vazio. Preencha todos os campos.")
        else:
            database.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)
                """, (name, email, username, password))  
            database.conn.commit()
            st.success("Conta criada com sucesso")

def main():
    page = st.sidebar.radio("Navigation", ["Login", "Register"])
    
    if page == "Login":
        login()
    elif page == "Register":
        register()

if __name__ == "__main__":
    main()
