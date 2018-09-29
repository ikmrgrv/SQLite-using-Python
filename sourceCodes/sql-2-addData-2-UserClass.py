# import the sqlite module
import sqlite3

from users import User

user1 = User('Emilie', 'Clarke', 'ValarMoghuls')

# create the connection with the database
conn = sqlite3.connect('user.db')
c = conn.cursor()

# prepare the execution of the instructions
c.execute("INSERT INTO users VALUES (:first, :last, :password)", {'first':user1.first, 'last':user1.last, 'password':user1.password})
# commit the changes
conn.commit()

# remember to close the connection to database
conn.close()