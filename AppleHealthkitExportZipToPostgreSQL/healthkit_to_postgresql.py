# List the zip file
import pathlib
import zipfile

directory = pathlib.Path("/Users//userSQL/export.zip")

# List the zip file
with zipfile.ZipFile("export.zip", mode="r") as archive:
    archive.printdir()

# Extract the zip file
import pathlib
import zipfile
directory = pathlib.Path("/Users//userSQL/export.zip")
with zipfile.ZipFile("export.zip", mode="r") as archive:
    for file in archive.namelist():
        archive.extract(file, "/Users/user/SQL")

# Parse XML file
import xml.etree.ElementTree as ET
tree = ET.parse('apple_health_export/export.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag,child.attrib)

record_list = [x.attrib for x in root.iter('Record')]
print(record_list)

import psycopg2
# Database connection details (replace with your actual details)
dbname = "appleHealthExport"
user = "postgres"
password = "password"
host = "localhost"
port = 5432
# Connect to PostgreSQL
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()
# Create a table to store the data
cur.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id SERIAL PRIMARY KEY,
        creationDate TIMESTAMP,
        startDate TIMESTAMP,
        endDate TIMESTAMP,
        value NUMERIC
    );
""")
# Insert records into the table, handling potential data type mismatches
insert_query = """
    INSERT INTO records (creationDate, startDate, endDate, value)
    VALUES (%s, %s, %s, %s)
"""
# Insert data into table
for record in record_list:
    values = (record.get('creationDate'), record.get('startDate'),
              record.get('endDate'), record.get('value'))
    cur.execute(insert_query, values)

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("Data inserted into PostgreSQL successfully!")
