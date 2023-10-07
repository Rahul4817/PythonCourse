import MySQLdb


def insert_rows(e_no, e_name, Type, sal):
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor = connection.cursor()

    sql = "INSERT INTO empdata(e_no, e_name, Type, salary) VALUES (%s, %s, %s, %s)"
    args = (e_no, e_name, Type, sal)

    cursor.execute(sql, args)
    connection.commit()
    print('One row inserted..')

    cursor.close()
    connection.close()


def show_table_data():
    connection = MySQLdb.connect(host='localhost', database='mydatabase', user='root', password='rahul@1234')
    cursor = connection.cursor()

    sql = "SELECT * FROM empdata"
    cursor.execute(sql)

    rows = cursor.fetchall()

    if not rows:
        print("No data found in the table.")
    else:
        print("Table Data:")
        for row in rows:
            print(f"e_no: {row[0]}, e_name: {row[1]}, Type: {row[2]}, salary: {row[3]}")

    cursor.close()
    connection.close()


n = int(input("How many rows?"))

for i in range(n):
    x = int(input("e_no: "))
    y = input("e_name: ")
    a = input("type: ")
    z = float(input("salary: "))
    insert_rows(x, y, a, z)
    print('-------------------------')

show_table_data()
