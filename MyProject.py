import random
import sys

login = input("Login uchun ID kiriting (eslatma teacher ID 't' harfidan, student ID esa 's' harfidan boshlanadi): ")

if login[0] == "t":
    show_address = True
elif login[0] == "s":
    show_address = False
else:
    show_address = False
    print("Login xato kiritildi")
    sys.exit()


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
        self.__addresses = addresses
        self.students_lst = []

    def get_student_generate(self, n):
        for i in range(n):
            p.get_person_generate(n)
            a.get_address_generate(n)
            self.students_lst.append({"id": 's'+str(p.persons_lst[i]["id"]),
                                      "Ism familiya": f"{p.persons_lst[i]["ism"]} {p.persons_lst[i]["familiya"]}",
                                      "yosh": p.persons_lst[i]["yosh"],"kurs": random.randint(1, 4),
                                      "manzil": a.address_lst[i]})

    def get_student_info(self, student):
        info = f"ID: {student['id']}, Ism familiya: {student['Ism familiya']}, Yosh: {student['yosh']}, Kurs: {student['kurs']}"
        if show_address == True :
            info += f", Manzil: {student['manzil']}"
        return info

s = Student(p.persons_lst, a.address_lst)
s.get_student_generate(100)


class Teacher:
    def __init__(self, persons, addresses):
        self.teacher_lst = []
        self.persons = persons
        self.addresses = addresses

    def get_geneerate_teacher(self, n):
        for i in range(n):
            p.get_person_generate(n)
            a.get_address_generate(n)
            self.teacher_lst.append({"id": 't'+ str(p.persons_lst[i]["id"]),
                                     "Ism familiya": f"{p.persons_lst[i]["ism"]} {p.persons_lst[i]["familiya"]}",
                                     "yosh": p.persons_lst[i]["yosh"],"Malakasi": random.randint(1, 15),
                                     "manzil": a.address_lst[i]})

    def get_teacher_info(self, teacher):
        return f"ID: {teacher['id']}, Ism familiya: {teacher['Ism familiya']}, \
        Yosh: {teacher['yosh']}, Malaka: {teacher['Malakasi']}, \
        Manzil: {teacher['manzil']}"

t = Teacher(p.persons_lst, a.address_lst)
t.get_geneerate_teacher(15)  #(n) n ta o'qituvchi yaratildi


class Groups:
    def __init__(self, group_id, teacher):
        self.group_id = group_id
        self.teacher = teacher
        self.students = []

    def get_group_info(self):
        return f"Guruh: {self.group_id}\nO'qituvchi: {self.teacher['Ism familiya']}\nTalabalar soni: {len(self.students)}"

    def get_group_students(self, student_obj):
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


class Faculty:
    def __init__(self, faculty_name):
        self.faculty_name = faculty_name
        self.all_groups = []

    def get_faculty_info(self):
        return f"Fakultet nomi: {self.faculty_name}, \
         guruhlar: {[i.group_id for i in self.all_groups]}, \
         O'quvchilar soni: {sum(len(group.students) for group in self.all_groups)} "

    def get_group_add(self, group):
        self.all_groups.append(group)


f1 = Faculty("Aniq fanlar")
f2 = Faculty("Ijtimoiy fanlar")

f1.get_group_add(g1)
f1.get_group_add(g3)
f2.get_group_add(g2)
f2.get_group_add(g4)


class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.faculties = []   # Faculty obyektlari

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def get_university_info(self):
        total_groups = sum(len(f.all_groups) for f in self.faculties)
        total_students = sum(
            len(group.students)
            for f in self.faculties
            for group in f.all_groups
        )
        total_teachers = len({
            group.teacher["id"]
            for f in self.faculties
            for group in f.all_groups
        })

        return (
            f"Universitet: {self.university_name}\n"
            f"Fakultetlar soni: {len(self.faculties)}\n"
            f"Guruhlar soni: {total_groups}\n"
            f"O'quvchilar soni: {total_students}\n"
            f"O'qituvchilar soni: {total_teachers}"
        )

    def get_all_faculties(self):
        return [f.faculty_name for f in self.faculties]

    def get_all_groups(self):
        return [group.group_id for f in self.faculties for group in f.all_groups]

    def get_all_students(self):
        return [
            student['Ism familiya']
            for f in self.faculties
            for group in f.all_groups
            for student in group.students
        ]

    def get_all_teachers(self):
        return list({
            group.teacher["Ism familiya"]
            for f in self.faculties
            for group in f.all_groups
        })

u = University("Pedagogika")
u.add_faculty(f1)
u.add_faculty(f2)


print(u.get_all_groups())
# print(s.students_lst[89])
# print(t.teacher_lst[9])
# print(g4.get_group_info())
# g2.get_group_students(s)
# print(f1.get_faculty_info())
# print(f2.get_faculty_info())
# print(g1.get_group_info())


