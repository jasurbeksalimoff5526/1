class Address:
    def __init__(self, vil, tum, mfy, uy):
        self.vil = vil
        self.tum = tum
        self.mfy = mfy
        self.uy = uy

    def get_info_address(self):
        return f"Viloyat: {self.vil}, tuman: {self.tum}, mfy: {self.mfy}, uy: {self.uy}"


a1 = Address('Sugd', 'JAbbor Rasulov', 'Boboyev', '23')
a2 = Address('Toshkent', 'Mirzo Ulugbek', 'Feruza', '6')
a3 = Address('Buxoro', 'Vobkent', 'Qalachi', '26')
a4 = Address('Qashqadaryo', 'Qarshi', 'Tabassum', '126')


class Person:
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    def get_info_person(self):
        return f"ID: {self.id}, name: {self.name}, age: {self.age}, address: {self.address.get_info_address()}"


class Students(Person):
    def __init__(self, id, name, age, address, phone_number):
        super().__init__(id, name, age, address)
        self.phone_number = phone_number

    def get_info_student(self):
        return f"{self.get_info_person()}, phone_number: {self.phone_number}"


s1 = Students(1, 'Nozimjon', '20', a1, 998994445566)
s2 = Students(2, 'Jahongir', '30', a2, 998994445411)
s3 = Students(5, 'Marufjon', '18', a1, 998994115566)
s4 = Students(6, 'Jonibek', '17', a2, 998994245411)


class Profession:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_info_prof(self):
        return f"ID: {self.id}, name: {self.name}"


prof1 = Profession(1, 'Python')
prof2 = Profession(2, 'Java')


class Teacher(Person):
    def __init__(self, id, name, age, address, prof, staj):
        super().__init__(id, name, age, address)
        self.prof = prof
        self.staj = staj

    def get_info_teacher(self):
        return f"{self.get_info_person()}, prof: {self.prof}, staj: {self.staj}"


t1 = Teacher(3, 'Shaxriyor', '29', a3, prof1, 2)
t2 = Teacher(4, 'Jasurbek', '37', a4, prof2, 3)


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


n77 = Groups('N77', t1)
n78 = Groups('N78', t2)
n71 = Groups('N71', t2)

n71.add_student(s1)
n77.add_student(s2)
n77.add_student(s3)
n78.add_student(s4)


# n71.get_students()

class Markaz:
    def __init__(self, mazkaz_name):
        self.mazkaz_name = mazkaz_name
        self.data = {}  # {'python':['N72', 'N71']}

    def get_prof(self):
        for i in self.data:
            print(i)

    def get_markaz_groups(self):
        return [[j.group_name for j in i] for i in self.data.values()]

    def get_markaz_students(self):
        return [[[g.name for g in j.students] for j in i] for i in self.data.values()]

    def get_markaz_teachers(self):
        teachers = [{j.teacher.name for j in i} for i in self.data.values()]
        return teachers

    def get_info_markaz(self):

        return f"Name: {self.mazkaz_name}, Yonalaishlar soni: {len(self.data)},\
            Guruhlar soni: {sum([len(i) for i in self.data.values()])},\
            O'qituvchilar soni: {len(self.get_markaz_teachers())}"

    def add_group(self, prof, group):
        if prof.name not in self.data:
            self.data[prof.name] = [group, ]
        else:
            self.data[prof.name].append(group)

        return 'Guruh qoshildi'


m1 = Markaz('NT')
m1.add_group(prof1, n71)
m1.add_group(prof1, n77)
m1.add_group(prof2, n78)

print(m1.get_info_markaz())
