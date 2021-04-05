#1
class MyList:
    def __init__(self, data: list):
        self.data = data

    def __add__(self, other):
        return self.data + other.data

    def __mul__(self, other):
        return self.data*other

    def __str__(self):
        return str(self.data)


# l1 = MyList([1, 2, 3])
# l2 = MyList([6, 7])
# print(l1*2)
# print(l1+l2)
# print(str(l1))

#2
class TestPaper:
    def __init__(self, subject, mark_scheme: list, mark_pass):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.mark_pass = mark_pass


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, test: TestPaper, answers):
        correct = 0
        i = 0
        for question in test.mark_scheme:
            if answers[i] == question:
                correct += 1
            i += 1
        score = correct*100//len(test.mark_scheme)
        if (score >= int(test.mark_pass[:2])):
            message = "Passed!"
        else:
            message = "Failed!"
        if type(self.tests_taken) == str:
            self.tests_taken = dict()
        self.tests_taken[test.subject] = f"{message} ({score}%)"


# paper1 = TestPaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = TestPaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = TestPaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
# student1 = Student()
# student2 = Student()
# print(student1.tests_taken)
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# print(student1.tests_taken)
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# print(student2.tests_taken)