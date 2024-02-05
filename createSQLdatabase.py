import sqlite3

from faker import Faker

conn = sqlite3.connect("personData.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE person
(id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
address TEXT,
phone TEXT,
email TEXT         
)
"""
)

fake = Faker()
for i in range(500):
    name = fake.name()
    age = fake.random_int(min=18, max=80, step=1)
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()
    # c.execute(__sql:"INSERT INTO person (name, age, address, phone, email) VALUES(?, ?, ?, ?, ?)", __parameters:(name, age, address, phone, email))
    c.execute(
        "INSERT INTO person (name, age, address, phone, email) VALUES(?, ?, ?, ?, ?)",
        (name, age, address, phone, email),
    )

conn.commit()
conn.close()
