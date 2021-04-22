import sqlite3

connection = sqlite3.connect('homework5.db')
cursor = connection.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS orders(OrderDate DATETIME NOT NULL, Region TEXT NOT NULL, Client TEXT NOT NULL, Item TEXT NOT NULL, Units INTEGER NOT NULL, UnitsCost REAL NOT NULL, Total REAL NOT NULL)")
    with open('dataset2.csv') as file:
        file.readline()
        for line in file:
            if line[-2] == '"':
                split_line = line.split('"')
                split_data = split_line[0].split(',') + split_line[1].split(',')
                data = [split_data[0], split_data[1], split_data[2], split_data[3], split_data[4], split_data[5], int(split_data[7])*1000 + float(split_data[8])]
            else:
                data = line.split(',')
            cursor.execute(f"INSERT INTO orders VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}')")
    connection.commit()

def print_rows(cursor):
        for row in cursor.fetchall():
            print(row)

# create_table()
cursor.execute("SELECT Region, SUM (Total) FROM orders GROUP BY Region")
print("a. რა ღირებულების პროდუქცია გაიყიდა თითოეულ რეგიონში: ")
print_rows(cursor)
cursor.execute("SELECT Client, SUM (Units) FROM orders GROUP BY Client ORDER BY SUM (Units) DESC")
print("b. კლიენტი, რომელმაც ყველაზე მეტი ივაჭრა: ")
print(cursor.fetchone())
cursor.execute("SELECT Item, SUM (Units) FROM orders GROUP BY Item ORDER BY SUM (Units) DESC")
print("c. პროდუქტი, რომელიც ყველაზე მეტი გაიყიდა: ")
print(cursor.fetchone())
cursor.execute("SELECT Item, SUM (Total)/ SUM (Units) AS Average_Price FROM orders GROUP BY Item ORDER BY Average_Price DESC")
print("d. პროდუქციების საშუალო ფასი: ")
print_rows(cursor)
cursor.execute("SELECT SUM (Total) FROM orders")
print("e. გაყიდული პროდუქციის ჯამური ღირებულება: ")
print(cursor.fetchone()[0])
