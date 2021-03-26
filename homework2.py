#1
class Book:
    def __init__(self, name, author, year, pages):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__pages = pages

    def info(self):
        return f"სახელი: {self.__name}, \n ავტორი: {self.__author} \n გამოშვების წელი: {self.__year} \n გვერდების რაოდენობა: {self.__pages} \n"

# book1 = Book("სამეფო კარის თამაშები", "ჯორჯ მარტინი", "2000", "700")
# print(book1.info())
# book2 = Book("ატლასი", "ნიკოლოზ II", "1790", "200")
# book3 = Book("წიგნი", "ავტორი", "წელი", "გვერდი")
# print(book2.info(), book3.info())

#2
class Extrema_List(list):
    # def __init__(self, **args):
    #     super().__init__(**args)

    def min(self):
        minValue = self[0]
        for i in self[1:]:
            if i<minValue:
                minValue = i
        return minValue

    def max(self):
        maxValue = self[0]
        for i in self[1:]:
            if i>maxValue:
                maxValue = i
        return maxValue

# list1 = Extrema_List((1, 4, 6, 8))
# list2 = Extrema_List((5, 18, 2, 1))
# list3 = Extrema_List((19, 3, 20, 19))
# print(list1.min(), list1.max())
# print(list2.min(), list2.max())
# print(list3.min(), list3.max())

#3
class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        return f"სახელი: {self._name}, ასაკი: {self._age}"

class Dog(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age)
        self._breed = breed
        self._color = color

    def info(self):
        return super().info() + f"\n ჯიში: {self._breed}, ფერი: {self._color}"

# dog1 = Dog("ბაქსი", "4", "დვარნიაშკა", "ყავისფერი")
# dog2 = Dog("ცუგა", "5", "ჯიში", "შავ-თეთრი")
# print(dog1.info(), "\n", dog2.info())

#4
class CallMixin:
    def call(self):
        print("ირეკება ნომერზე ", self.phone)

class Person:
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone

    def info(self):
        return f"სახელი: {self.fname}, გვარი: {self.lname} \n მობილურის ნომერი: {self.phone}"

class Contact(Person, CallMixin):
    pass

# contact1 = Contact("მიხეილ", "სააკაშვილი", "5570000001")
# contact1.call()