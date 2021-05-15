import requests
import json
from pprint import pprint

URL = "https://crudcrud.com/api/73992a0a93244d2bb4da787c7fd6787d"
header = {"Content-type" : "Application/json"}


def employee_dict(id, name, surname, age, gender, salary):
    result = {
        "id" : id,
        "name" : name,
        "surname" : surname,
        "age" : age,
        "gender" : gender,
        "salary" : salary
    }
    return result


def post_employee(employee):
    response = requests.post(f"{URL}/employees", data=json.dumps(employee), headers=header)
    if 200<= response.status_code < 300:
        print("Employee successfully added", {response.status_code})
    else:
        print("Error adding employee", {response.status_code})


employees = []
employees.append(employee_dict(1, "Nichola", "Davies", 34, "Male", 1230))
employees.append(employee_dict(2, "Deirdre", "Paterson", 41, "Female", 1000))
employees.append(employee_dict(3, "Sonia", "Butler", 28, "Female", 1500))
employees.append(employee_dict(4, "Jacob", "Metcalfe", 42, "Male", 2000))
employees.append(employee_dict(5, "Fiona", "Clarkson", 39, "Female", 1850))

# ქმნის რესურსებს
for employee in employees:
    post_employee(employee)

response = requests.get(f"{URL}/employees")
if 200 <= response.status_code < 300:
    print("Success reading resources", response.status_code)
    data = json.loads(response.content)
    id_dict = {}
    for employee in data:
        id_dict[employee['id']] = employee['_id']


    def update_employee(id, key, value):
        employees[id-1][key] = value
        response = requests.put(f"{URL}/employees/{id_dict[id]}", data=json.dumps(employees[id-1]), headers=header)
        if 200 <= response.status_code < 300:
            print("Resource updated successfully", response.status_code)
        else:
            print("Error updating resource", response.status_code)


    def delete_employee(id):
        response = requests.delete(f"{URL}/employees/{id_dict[id]}")
        if 200 <= response.status_code < 300:
            print("Resource removed successfully", response.status_code)
        else:
            print("Error removing resource", response.status_code)

    # ანახლებს რესურსებს
    update_employee(3, "salary", 1700)
    update_employee(1, "name", "Nicholas")
    update_employee(5, "age", 40)
    delete_employee(4)

    response = requests.get(f"{URL}/employees")
    if 200 <= response.status_code < 300:
        print("Success reading resources", response.status_code)
        updated_data = json.loads(response.content)
        pprint(updated_data)
    else:
        print("Error reading resources", response.status_code)

else:
    print("Error reading resources", response.status_code)