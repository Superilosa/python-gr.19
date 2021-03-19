#1
class Calculator:
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def divide(self, a, b):
        return a/b

    def multiply(self, a, b):
        return a*b


# my_calculator = Calculator()
# print(my_calculator.add(2, 3))
# print(my_calculator.subtract(5, 9))
# print(my_calculator.divide(135, 5))
# print(my_calculator.multiply(2, 3))

#2
class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.width*self.length

    def perimeter(self):
        return (self.width + self.length)*2

    def print_info(self):
        print(f"სიგრძე: {self.length}, სიგანე: {self.width} \n ფართობი: {self.area()}, პერიმეტრი: {self.perimeter()}")


# my_rectangle = Rectangle(4, 12)
# my_rectangle.print_info()

#3
class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def info(self):
        return f"სახელი: {self.name}, გვარი: {self.surname}, ასაკი: {self.age}, ხელფასი: {self.salary}"


data = open("dataset1.csv")
data.readline()
employees = []
for line in data:
    info = line.split(',')
    employees.append(Employee(info[0], info[1], info[2], info[3]))
data.close()
min_salary = min(employees, key=lambda c: c.salary)
max_age = max(employees, key=lambda c: c.age)
print("ყველაზე დაბალი ხელფასი - ", min_salary.info())
print("ყველაზე ხანდაზმული - ", max_age.info())