import random

class Address:
    def __init__(self):
        self.city = random.choice(["Toshkent", "Samarqand", "Buxoro", "Andijon", "Farg'ona"])
        self.street = random.choice(["Mustaqillik", "Navoi", "Amir Temur", "Bog'bon", "Yoshlik"])
        self.house_number = random.randint(1, 200)


    def get_info_address(self):
        return f"Shahar: {self.city}, Ko'cha: {self.street}, Uy: {self.house_number}"


a1 = Address()
a2 = Address()
a3 = Address()
a4 = Address()
a5 = Address()
a6 = Address()
a7 = Address()
a8 = Address()
a9 = Address()
a10 = Address()
a11 = Address()
a12 = Address()


class Person:
    def __init__(self, id, address):
        self.id = id
        self.first_name = random.choice(["Ali", "Vali", "Sardor","Toshmat","Alisher","Oybek","Umid"])
        self.last_name = random.choice(["Bekmurodov", "Odilov", "Abrorov","Xolmurodov","Mirjalolov","Farxodov","G'aybullayev"])
        self.age = random.randint(18, 45)
        self.address = address

    def get_person_info(self):
        return f"Ism: {self.first_name}, Familiya: {self.last_name}, Yosh: {self.age}\nManzil => {self.address.get_info_address()}"


class Student(Person):
    def __init__(self, id, address, ):
        super().__init__(id, address)
        self.course = random.randint(1,4)

    def get_student_info(self):
        return f"Ism: {self.first_name}, Familiya: {self.last_name}, Yosh: {self.age}\nManzil => {self.address.get_info_address()}\nKurs: {self.course}-kurs"


s1 = Student(1, a1)
s2 = Student(2, a2)
s3 = Student(3, a3)
s4 = Student(4, a4)
s5 = Student(5, a5)
s6 = Student(6, a6)
s7 = Student(7, a7)
s8 = Student(8, a8)
s9 = Student(9, a9)
s10 = Student(10, a10)
s11 = Student(11, a11)
s12 = Student(12, a12)


class Teacher(Person):
    def __init__(self, id, address, qualification ):
        super().__init__(id, address)
        self.qualification = qualification

    def get_teacher_info(self):
        return f"Ism: {self.first_name}, Familiya: {self.last_name}, Yosh: {self.age}\nManzil => {self.address.get_info_address()}\nMalakasi: {self.qualification} yil"


t1 = Teacher(13, a1, 5)
t2 = Teacher(14, a2, 17)
t3 = Teacher(15, a3, 9)
t4 = Teacher(16, a4, 8)
t5 = Teacher(17, a5, 22)



class Groups:
    def __init__(self, group_name, teacher):
        self.group_name = group_name
        self.teacher = teacher
        self.students = []

    def get_info_group(self):
        return f"Name: {self.group_name}, teacher: {self.teacher}, Student count: {len(self.students)}"

    def get_students(self):
        for i in self.students:
            print(i.get_info_student())

    def add_student(self, student):
        self.students.append(student)
        return f'{student.name} qoshildi'


class Speciality:
    pass


class Faculty:
    pass


class StatusUniversity:
    pass


print(s1.get_student_info())
print(t3.get_teacher_info())