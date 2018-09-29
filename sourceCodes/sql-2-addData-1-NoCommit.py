# import the sqlite module
import sqlite3

# create the connection with the database
conn = sqlite3.connect('user.db')
c = conn.cursor()

# prepare the execution of the instructions
c.execute("INSERT INTO users VALUES ('tom', 'cruise', 'mi1234')")

# remember to close the connection to database
conn.close()