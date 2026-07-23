"""
main.py
-------
Entry point of the Student Result Management System.
Run this file to start the application:

    python main.py
"""

import tkinter as tk
from database.db_manager import DBManager
from gui.login_window import LoginWindow


def main():
    db = DBManager()          # sets up the SQLite database (creates it on first run)
    root = tk.Tk()
    LoginWindow(root, db)      # start with the login screen
    root.mainloop()
    db.close()                 # close the database connection when the app is closed


if __name__ == "__main__":
    main()
