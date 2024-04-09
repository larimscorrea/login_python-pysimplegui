import PySimpleGUI as sg
import database

sg.theme('LightGrey1')

layout_login = [
    [sg.Image(filename="icons/icon.png", size=(100, 100))],
    [sg.Text('Username:', font=('Century Gothic', 12)), sg.InputText(key='-USERNAME-', size=(20, 1))],
    [sg.Text('Password:', font=('Century Gothic', 12)), sg.InputText(key='-PASSWORD-', size=(20, 1), password_char='*')],
    [sg.Button('Login', size=(10, 1)), sg.Button('Register', size=(10, 1))]
]

layout_register = [
    [sg.Text('Name:', font=('Century Gothic', 12)), sg.InputText(key='-NAME-', size=(20, 1))],
    [sg.Text('Email:', font=('Century Gothic', 12)), sg.InputText(key='-EMAIL-', size=(20, 1))],
    [sg.Text('Username:', font=('Century Gothic', 12)), sg.InputText(key='-REG_USERNAME-', size=(20, 1))],
    [sg.Text('Password:', font=('Century Gothic', 12)), sg.InputText(key='-REG_PASSWORD-', size=(20, 1), password_char='*')],
    [sg.Button('Register', size=(10, 1)), sg.Button('Back', size=(10, 1))]
]

window_login = sg.Window('System - Access Panel', layout_login, element_justification='c', finalize=True)
window_register = None

def open_register_window():
    global window_register
    if window_register is None:
        window_register = sg.Window('Register', layout_register, element_justification='c', finalize=True)

def close_register_window():
    global window_register
    if window_register is not None:
        window_register.close()
        window_register = None

while True:
    event, values = window_login.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Login':
        user = values['-USERNAME-']
        password = values['-PASSWORD-']
        database.cursor.execute("""SELECT * FROM Users WHERE (User = ? and Password = ?)""", (user, password))
        if database.cursor.fetchone():
            sg.popup('Login Info', 'Access confirmed. Welcome!')
        else:
            sg.popup_error('Login Info', 'Access denied. Please check if you are registered in the system.')
    if event == 'Register':
        open_register_window()
    if window_register is not None:
        event_register, values_register = window_register.read()
        if event_register == sg.WINDOW_CLOSED:
            close_register_window()
        if event_register == 'Register':
            name = values_register['-NAME-']
            email = values_register['-EMAIL-']
            reg_user = values_register['-REG_USERNAME-']
            reg_pass = values_register['-REG_PASSWORD-']
            if name == "" or email == "" or reg_user == "" or reg_pass == "":
                sg.popup_error('Register Error', 'Please fill in all fields.')
            else:
                database.cursor.execute("""INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)""",
                                        (name, email, reg_user, reg_pass))
                database.conn.commit()
                sg.popup('Register Info', 'Account created successfully')
                close_register_window()

window_login.close()
