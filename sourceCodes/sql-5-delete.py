# import the sqlite module
import sqlite3

# create the connection with the database
conn = sqlite3.connect('user.db')
c = conn.cursor()

# query all the records present
c.execute("DELETE FROM users WHERE firstName='Kumar' AND lastName='Gaurav' AND password='omgykh'")
conn.commit()

# remember to close the connection to database
conn.close()