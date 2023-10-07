import MySQLdb
from MySQLdb import *


connection=MySQLdb.connect(host='localhost',database='empdata',user='root',password='rahul@1234')

cursor=connection.cursor()

cursor.execute("select * from item")

row=cursor.fetchone()
print(row)
rows=cursor.fetchall()

print("Total number of rows",cursor.rowcount)
for row in rows:
    # print(row)
    empid=row[0]
    item_id=row[1]
    item_dispatch=row[3]
    print(empid,item_id,item_dispatch)


cursor.close()

connection.close()