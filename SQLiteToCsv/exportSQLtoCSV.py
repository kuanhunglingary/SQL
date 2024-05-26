import sqlite3

import pandas as pd

conn = sqlite3.connect("personData.db")

df = pd.read_sql_query("SELECT * FROM person", conn)

df.to_csv("person_info.csv", index=False)

conn.close()
