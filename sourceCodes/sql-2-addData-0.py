# import the sqlite module
import sqlite3

# create the connection with the database
conn = sqlite3.connect('user.db')
c = conn.cursor()

# prepare the execution of the instructions
c.execute("INSERT INTO users VALUES ('kumar', 'gaurav', 'ezpzlmnsqz')")
c.execute("INSERT INTO users VALUES ('Deepika', 'Padukone', 'deepika<3kumar')")
c.execute("INSERT INTO users VALUES ('Tom', 'Cruise', 'MI12345')")
# commit the changes
conn.commit()

# remember to close the connection to database
conn.close()