import requests
import sqlite3

connection = sqlite3.connect('homework8.db')
cursor = connection.cursor()
URL = "https://jsonplaceholder.typicode.com"


def get_json(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        print("Get request successful", response.status_code)
        return response.json()
    else:
        raise Exception("Get request unsuccessful", response.status_code)


todo_json = get_json(f"{URL}/todos")
user_json = get_json(f"{URL}/users")
cursor.execute("CREATE TABLE IF NOT EXISTS todos(Id INTEGER NOT NULL, Title TEXT NOT NULL, Completed INTEGER NOT NULL, UserId INTEGER NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS users(Id INTEGER NOT NULL, Name TEXT, Address TEXT, Company TEXT, Email TEXT, Username Text, Phone Text, Website Text)")

for element in todo_json:
    id = element['id']
    title = element['title']
    completedBool = element['completed']
    if completedBool:
        completed = 1
    else:
        completed = 0
    userId = element['userId']
    cursor.execute(f"INSERT INTO todos VALUES ('{id}', '{title}', '{completed}', '{userId}')")

for element in user_json:
    id = element['id']
    name = element['name']
    address_dict = element['address']
    address = f"{address_dict['suite']} {address_dict['street']}, {address_dict['city']}, Zipcode: {address_dict['zipcode']}, Coordinates: {address_dict['geo']['lat']}  {address_dict['geo']['lng']}"
    company_dict = element['company']
    company = f"{company_dict['name']}: {company_dict['catchPhrase']};  {company_dict['bs']}"
    email = element['email']
    username = element['username']
    phone = element['phone']
    website = element['website']
    cursor.execute(f"INSERT INTO users VALUES ('{id}', '{name}', '{address}', '{company}', '{email}', '{username}', '{phone}', '{website}')")

connection.commit()