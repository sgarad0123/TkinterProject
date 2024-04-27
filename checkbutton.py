import psycopg2
import tkinter as tk


# function to verify login credentials
def verify_login(username, password):
    try:
        # connect to the database
        conn = psycopg2.connect(dbname='test', user='postgres', password='admin@123', host='localhost')
        cursor = conn.cursor()
        print("successuful connected")
        # query the database for the user
        savequry="select * from login"
        cursor.execute(savequry)
        rows = cursor.fetchall()

        # if a match is found, return True
        if rows:
            return True
        else:
            return False
    except psycopg2.Error as e:
        print(e)
        return False


# function to handle the login button press
def login():
    # get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # verify the login credentials
    if verify_login(username, password):
        # show a successful login message
        tk.Label(window, text='Login successful').pack()
    else:
        # show a failed login message
        tk.Label(window, text='Invalid login').pack()


# create the main window
window = tk.Tk()

# create the username and password entries
username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show='*')

# create the login button
login_button = tk.Button(window, text='Login',bg='orange', command=login)

# pack the widgets into the window
username_entry.pack()
password_entry.pack()
login_button.pack()

# run the main loop
window.mainloop()

