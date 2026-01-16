# class Person:
#     def __init__(self, name, city, year, age):
#         self.name = name
#         self._age = age
#         self.city = city
#         self.__year = year
#
#     def get_info(self):
#         return f"Mening ismim: {self.name}, yoshim: {self._age}, manzil: {self.city}, tugilgan yili: {self.__year}"
#
#     def get_year(self):
#         return f"Sining tugilgan yilingiz {2026 - int(self.age)}"
#
#
# person1 = Person(name="Ali", age=90, city="Tashkent", year=2009)
# person2 = Person("Shaxriyor", "Buxoro", 2010, 20, )
# person3 = Person("Umidjon", "Toshkent", 2012, 22, )
#
# # print(person1.name)
# # print(person1._age)
# # print(person1.get_info())
#
#
# class Student(Person):
#     def __init__(self, name, city, year, age, prof, group, month):
#         super().__init__(name, city, year, age)
#         self.prof = prof
#         self.group = group
#         self.month = month
#
#     def test_func(self):
#         return self.get_info()
#
#
# s1 = Student('Shaxriyor', 'Tashkent', 2007, 20, 'Go', 17, 8)
# s2 = Student('Umidjon', 'Toshkent', 2003, 45, 'Java', 89, 5)
#
# print(s1.test_func())
#


class Person:
    def __init__(self, name, city, year, age):
        self.name = name
        self.age = age
        self.city = city
        self.year = year

    def get_name(self):
        return self.name

    def __get_age(self):
        return self.age

p = Person(name="Ali", age=90, city="Tashkent", year=2009)
print(p.__get_age())



