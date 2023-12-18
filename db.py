from tkinter import *
import sqlite3

root = Tk()
root.title("股價資料庫")

# Create a database or connect to one
conn = sqlite3.connect('stock.db')

# Create cursor
con = conn.cursor()

# Create table
con.execute("""CREATE TABLE IF NOT EXISTS stock (
            "id" INTEGER,
            "Date" INTEGER NOT NULL,
            "Open" INTEGER NOT NULL,
            "High" INTEGER NOT NULL,
            "Low" INTEGER NOT NULL,
            "Close" INTEGER NOT NULL,
            "Adj Close" INTEGER NOT NULL,
            "Volume" INTEGER NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            )""")

# Create Submit Function For databse
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('stock.db')

    # Create cursor
    con = conn.cursor()

# Create Text Boxes
Date = Entry(root, width=30)
Date.grid(row=0, column=1, padx=20)
Open = Entry(root, width=30)
Open.grid(row=1, column=1, padx=20)
High = Entry(root, width=30)
High.grid(row=2, column=1, padx=20)
Low = Entry(root, width=30)
Low.grid(row=3, column=1, padx=20)
Close = Entry(root, width=30)
Close.grid(row=4, column=1, padx=20)
AdjClose = Entry(root, width=30)
AdjClose.grid(row=5, column=1, padx=20)
Volume = Entry(root, width=30)
Volume.grid(row=6, column=1, padx=20)

# Create Text Box Label
Date_label = Label(root, text="Date")
Date_label.grid(row=0, column=0)
Open_label = Label(root, text="Open")
Open_label.grid(row=1, column=0)
High_label = Label(root, text="High")
High_label.grid(row=2, column=0)
Low_label = Label(root, text="Low")
Low_label.grid(row=3, column=0)
Close_label = Label(root, text="Close")
Close_label.grid(row=4, column=0)
AdjClose_label = Label(root, text="AdjClose")
AdjClose_label.grid(row=5, column=0)
Volume_label = Label(root, text="Volume")
Volume_label.grid(row=6, column=0)


# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=10, pady=10, padx=10, ipadx=100)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

# # Create a menu item
# file_menu = Menu(my_menu)
# my_menu.add_cascade(Label="File", menu=file_menu)
# file_menu.add_command(Label="Exit", command=root.quit)

root.mainloop()