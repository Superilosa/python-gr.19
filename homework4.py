import sqlite3

connection = sqlite3.connect('census.db')
cursor = connection.cursor()


def fill_in_density(province, population, area):
    cursor.execute(f"INSERT INTO density VALUES ('{province}', {population}, {area})")


def print_rows(cursor, multiple):
    if multiple:
        for row in cursor.fetchall():
            print(row)
    else:
        for row in cursor.fetchall():
            print(row[0])


cursor.execute("CREATE TABLE IF NOT EXISTS density(province_or_territory TEXT, population INTEGER, land_area REAL)")
fill_in_density('Newfoundland and Labrador', 512930, 370501.69)
fill_in_density('Prince Edward Island', 135294, 5684.39)
fill_in_density('Nova Scotia', 908007, 52917.43)
fill_in_density('New Brunswick', 729498, 71355.67)
fill_in_density('Quebec', 7237479, 1357743.08)
fill_in_density('Ontario', 11410046, 907655.59)
fill_in_density('Manitoba', 1119583, 551937.87)
fill_in_density('Saskatchewan', 978933, 586561.35)
fill_in_density('Alberta', 2974807, 639987.12)
fill_in_density('British Columbia', 3907738, 926492.48)
fill_in_density('Yukon Territory', 28674, 474706.97)
fill_in_density('Northwest Territories', 37360, 1141108.37)
fill_in_density('Nunavut', 26745, 1925460.18)
connection.commit()

print("ყველა პროვინცია: ")
cursor.execute("SELECT * FROM density")
print_rows(cursor, True)
print("მოსახლეობები: ")
cursor.execute("SELECT population FROM density")
print_rows(cursor, False)
print("1000000-ზე ნაკლებ მოსახლეობიანი პროვინციები: ")
cursor.execute("SELECT * FROM density WHERE population<1000000")
print_rows(cursor, True)
print("1000000-ზე ნაკლებ ან 5000000-ზე მეტ მოსახლეობიანი პროვინციები: ")
cursor.execute("SELECT * FROM density WHERE population<1000000 OR population>5000000")
print_rows(cursor, True)
print("1000000-სა და 5000000-ს შორის მოსახლეობიანი პროვინციები: ")
cursor.execute("SELECT * FROM density WHERE population BETWEEN 1000000 AND 5000000")
print_rows(cursor, True)
print("200000 კვ.კმ-ზე დიდ ფართობიანი პროვინციების მოსახლეობები: ")
cursor.execute("SELECT population FROM density WHERE land_area > 200000")
print_rows(cursor, False)
print("პროვინციები მოსახლეობის სიმჭიდროვითურთ: ")
cursor.execute("SELECT *, population/land_area FROM density")
print_rows(cursor, True)


connection.close()