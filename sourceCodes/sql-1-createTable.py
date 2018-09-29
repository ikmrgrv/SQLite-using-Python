# import the sqlite module
import sqlite3

# create the connection with the database
# can use :memory: for a volatile database that lives in RAM
conn = sqlite3.connect('user.db')
c = conn.cursor()

# prepare the execution of the instructions
c.execute("""CREATE TABLE users (
        firstName text,
        lastName text,
        password text)""")
# commit the changes
conn.commit()

# remember to close the connection to database
conn.close()