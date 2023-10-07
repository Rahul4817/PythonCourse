# '''CREATE TABLE "seat" (
# 	"seat_id"	TEXT,
# 	"taken"	INTEGER,
# 	"Field4"	INTEGER
# );'''
#
import MySQLdb


def create_table():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor=connection.cursor()
    cursor.execute("""
    CREATE TABLE "seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
    );
    """)
    connection.commit()
    connection.close()

def insert_record():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO "seat"("seat_id","taken","price") VALUES("A1","0","100"),("A2","1","130"),("A3","0","160")
    """)

    connection.commit()
    connection.close()
def select_all():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor=connection.cursor()
    cursor.execute("""
    SELECT * FROM "seat"
    """)
    result=cursor.fetchall()
    connection.close()
    return result

def select_specific_columns():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id","price" FROM "seat"
    """)
    result=cursor.fetchall()
    connection.close()
    return result

def select_with_condition():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id","price" FROM "seat" WHERE "price">130
    """)
    result=cursor.fetchall()
    connection.close()
    return result

def update_value():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE "seat" SET "taken"=0 WHERE "seat_id"="A1"
    """)
    connection.commit()
    connection.close()

def delete_records():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM "seat"WHERE "seat_id"="A1"
    """)
    connection.commit()
    connection.close()

create_table()
# insert_record()
# print(select_all())
# # print(select_specific_columns())
# # print(select_with_condition())
# #update_value()
# delete_records()
