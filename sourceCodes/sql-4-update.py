# import the sqlite module
import sqlite3

# create the connection with the database
conn = sqlite3.connect('user.db')
c = conn.cursor()

# update a record in the table
c.execute("UPDATE users SET firstName='Kumar' WHERE firstName='kumar'")
# c.execute("UPDATE users SET lastName='Gaurav' WHERE lastName='gaurav'")
# c.execute("UPDATE users SET password='raabata' WHERE firstName='deepika'")
# ensure committing the changes
conn.commit()

# query all the records present
c.execute("SELECT * FROM users")
print(c.fetchall())
conn.commit()

# remember to close the connection to database
conn.close()