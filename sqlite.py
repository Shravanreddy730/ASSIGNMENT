import sqlite3
  
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')
  
# cursor object
cursor_obj = connection_obj.cursor()
  
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS USER")
  
# Creating table
table = """ CREATE TABLE USER (
            Email VARCHAR(255) NOT NULL,
            NAME CHAR(25) NOT NULL,
            PHONENUMBER VARCHAR(12),
            Age INT,
            DATEOFBIRTH DATE
        ); """
  
cursor_obj.execute(table)
  
print("Table is Ready")


cursor_obj.execute('''INSERT INTO USER(
   Email, NAME, PHONENUMBER, Age, DATEOFBIRTH) VALUES 
   ('test1@gmail.com', 'shrabn', 33333327, 22, 1994-04-20)''')

print("Records inserted........")
######## 2 Task Filter By name
data=cursor_obj.execute("""SELECT * FROM USER WHERE NAME = 'shrabn'""")
ss = False
for row in data:
	print(row)
	ss  = True
if ss == False:
	print("Details NOT Found")
  
# Commit your changes in the database    
connection_obj.commit()
# Close the coonection
connection_obj.close()

