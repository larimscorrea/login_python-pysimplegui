import streamlit as st
import bcrypt
import database

def main():
    st.markdown("<h1 style='text-align: center; color: yellow;'>System</h1>", unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Fazer Login", key="login_btn", help="Clique para fazer login"):
            login()

    with col2:
        if st.button("Registrar", key="register_btn", help="Clique para se registrar"):
            register()

def login():
    st.title("System - Access Panel")
    st.sidebar.image("icons/icon.png")
    
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        user_data = database.cursor.execute(""" 
            SELECT Password FROM Users
            WHERE User = ?
            """, (username,)).fetchone()

        if user_data:
            hashed_password = user_data[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                st.success("Acesso confirmado. Bem vindo!")
            else:
                st.error("Acesso negado. Verifique suas credenciais!")
        else:
            st.error("Acesso negado. Verifique suas credenciais!")

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
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            database.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)
                """, (name, email, username, hashed_password))  
            database.conn.commit()
            st.success("Conta criada com sucesso")

if __name__ == "__main__":
    main()
