# import the sqlite module
import sqlite3

# create the connection with the database
conn = sqlite3.connect('user.db')
c = conn.cursor()

# query with conditions
c.execute("SELECT * FROM users WHERE firstName='Tom' AND lastName='Cruise' AND password='MI12345'")
print(c.fetchone())

# remember to close the connection to database
conn.close()