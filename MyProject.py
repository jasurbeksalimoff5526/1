import random

class Address:
    def __init__(self):
        self.address_lst = []


    def get_address_generate(self, n):
        for i in range(1,n+1):
            self.address_lst.append({"shahar": random.choice(cities), "ko'cha": random.choice(streets), "uy": random.randint(1, 200)})

cities = ["Toshkent", "Samarqand", "Buxoro", "Andijon", "Farg'ona", "Qarshi", "Namangan"]
streets = ["Mustaqillik", "Tinchlik", "Amir Temur", "Bog'bon", "Yoshlik", "Uchuvchilar"]

a = Address()


class Person:
    def __init__(self):
        self.persons_lst = []

    def get_person_generate(self, n):  #n ishlatilgani sababi keyinchalik yangi person(student,teacher) create qilishda shu metod qayta chaqiriladi
        for i in range(1, n+1):
            self.persons_lst.append({"id": i, "ism": random.choice(ismlar), "familiya": random.choice(familiyalar), "yosh": random.randint(18, 45)})



ismlar = ["Ali", "Vali", "Hasan", "Husan", "Jasur", "Aziz", "Bekzod", "Diyor", "Sardor", "Rustam"]
familiyalar = ["Islomov", "Sherzodov", "Mirjalolov", "Javohirov", "Abdullohov", "Muhammadov", "Temurov", "Anvarov", "Zafarov", "Otabekov"]

p = Person()


class Student:
    def __init__(self, persons, addresses):
        self.persons = persons
        self.addresses = addresses
        self.students_lst = []

    def get_student_generate(self, n):
        for i in range(n):
            p.get_person_generate(n)
            a.get_address_generate(n)
            self.students_lst.append({"id": 's'+str(p.persons_lst[i]["id"]),"Ism familiya": f"{p.persons_lst[i]["ism"]} {p.persons_lst[i]["familiya"]}","yosh": p.persons_lst[i]["yosh"],"kurs": random.randint(1, 4),"manzil": a.address_lst[i]})

    def get_student_info(self, student):
        return f"ID: {student['id']}, Ism familiya: {student['Ism familiya']}, Yosh: {student['yosh']}, Kurs: {student['kurs']}, Manzil: {student['manzil']}"



s = Student(p.persons_lst, a.address_lst)
s.get_student_generate(100)   # (n) nta student yaratildi
# print(s.students_lst[89])


class Teacher:
    def __init__(self, persons, addresses):
        self.teacher_lst = []

    def get_geneerate_teacher(self, n):
        for i in range(n):
            p.get_person_generate(n)
            a.get_address_generate(n)
            self.teacher_lst.append({"id": 't'+str(p.persons_lst[i]["id"]),"Ism familiya": f"{p.persons_lst[i]["ism"]} {p.persons_lst[i]["familiya"]}","yosh": p.persons_lst[i]["yosh"],"Malakasi": random.randint(1, 15),"manzil": a.address_lst[i]})


t = Teacher(p.persons_lst, a.address_lst)
t.get_geneerate_teacher(15)  #(n) n ta o'qituvchi yaratildi
# print(t.teacher_lst[9])


class Groups:
    def __init__(self, group_id, teacher):
        self.group_id = group_id
        self.teacher = teacher
        self.students = []

    def get_group_info(self):
        return f"Guruh: {self.group_id}\nO'qituvchi: {self.teacher['Ism familiya']}\nTalabalar soni: {len(self.students)}"


    def get_students(self, student_obj):
        for i in self.students:
            print( student_obj.get_student_info(i))

    def add_students(self, student):
        self.students.extend(student)
        return f'student qoshildi'

g1 = Groups("Matematika-1", t.teacher_lst[0])
g2 = Groups('Tarix-4', t.teacher_lst[1])
g3 = Groups('Fizika-7', t.teacher_lst[2])
g4 = Groups('Xorijiy tillar-5', t.teacher_lst[3])

g1.add_students(s.students_lst[0:25])
g2.add_students(s.students_lst[25:50])
g3.add_students(s.students_lst[50:75])
g4.add_students(s.students_lst[75:100])

print(g4.get_group_info())
# g2.get_students(s)
