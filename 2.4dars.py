class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Ismi: {self.name}, yoshi: {self.age}"

p1 = Person("Ali", 18, )


class Worker(Person):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession

    def get_profession(self):
        return f"{self.get_info()} lavozimi: {self.profession}"

s1 = Worker("Ali", 18, "dasturchi")

print(s1.get_info())
print(s1.get_profession())
