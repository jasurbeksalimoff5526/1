#1

'''
class Country:
    def __init__(self, nomi, maydoni, aholisi, qita):
        self.name = nomi
        self.area = maydoni
        self.population = aholisi
        self.continent = qita

    def get_full_info(self):
        return f"{self.name} maydoni {self.area} ming km², aholisi {self.population} million nafar, {self.continent} qit'asida joylashgan"
    def get_area(self):
        return f"{self.name}ning yer maydoni {self.area} ming km²"
    def get_population(self):
        return f"{self.name} aholisi {self.population} mmillion nafar"
    def get_continent(self):
        return f"{self.name}  {self.continent} qit'asida joylashgan"

country1 = Country("O'zbekiston", 448.978, 38, "osiyo")
country2 = Country("Turkiya", 783.562, 86, "osiyo")
country3 = Country("Italiya", 302, 59, "yevropa")
country4 = Country("Misr", 1014, 102, "afrika")

print(country4.get_area())
print(country2.get_population())
print(country3.get_continent())
print(country1.get_full_info())
'''



#2

'''
class Car:
    def __init__(self, nomi, yili, asoschisi, mamlakat):
        self.name = nomi
        self.year = yili
        self.founder = asoschisi
        self.country = mamlakat

    def get_full_info(self):
        return f"{self.name} avtomobil zavodiga {self.year} yilda {self.founder} tomonidan {self.country}da asos solingan"
    def get_year(self):
        return f"{self.name} avtomobillari {self.year}-yildan ishlab chiqarila boshlagan"
    def get_founder(self):
        return f"{self.name} avtomobillari asoschisi {self.founder}"
    def get_country(self):
        return f"{self.name} avtomobillari {self.country}da ishlab chiqariladi"

car1 = Car("Pagani", "1992", "Horacio Pagani", "Italiya" )
car2 = Car("Bmw", "1916", "Camillio Castiglioni", "Germaniya")
car3 = Car("Bugatti", "1909", "Ettori Bugatti", "Fransiya")
car4 = Car("McLaren", "2010", "Ron Dennis", "Angliya")

print(car1.get_full_info())
print(car2.get_year())
print(car3.get_founder())
print(car4.get_country())
'''



#3

'''
class Student:
    def __init__(self, ism, fan1, fan2, fan3):
        self.name = ism
        self.fan1 = fan1
        self.fan2 = fan2
        self.fan3 = fan3

    def get_result(self):
        result = (self.fan1 + self.fan2 + self.fan3) / 3
        return f"{self.name}ning o‘rtacha bali: {result}"

    def is_passed(self):
        result = (self.fan1 + self.fan2 + self.fan3) / 3
        if result >= 60:
            return f"{self.name} o‘tdi"
        else:
            return f"{self.name} o‘tmadi"

    def get_full_info(self):
        return f"{self.name}: ballar {self.fan1}, {self.fan2}, {self.fan3}"


student1 = Student("Ali", 70, 65, 80)
student2 = Student("Vali", 55, 60, 50)
student3 = Student("Aziza", 90, 85, 88)
student4 = Student("Dilshod", 60, 62, 58)

print(student1.get_result())
print(student2.is_passed())
print(student3.get_full_info())
print(student4.get_result())
'''



#4

'''
class Phone:
    def __init__(self, nomi, dastur, kamera, antutu):
        self.name = nomi
        self.os = dastur
        self.cam = kamera
        self.benchmark = antutu

    def get_full_info(self):
        return f"{self.name} - OS: {self.os}, Kamera: {self.cam} megapixel, Antutu: {self.benchmark}"

    def get_camera(self):
        return f"{self.name} kamerasi {self.cam} megapixel"

    def get_benchmark(self):
        return f"{self.name} AnTuTu bali {self.benchmark}"

    def get_dastur(self):
        return f"{self.name} operatsion tizimi {self.os}"


phone1 = Phone("Samsung", "Android", 200, 1500000)
phone2 = Phone("Apple", "iOS", 48, 1700000)
phone3 = Phone("Xiaomi", "Android", 200, 1600000)
phone4 = Phone("Huawei", "Android", 200, 1400000)

print(phone1.get_full_info())
print(phone2.get_dastur())
print(phone3.get_camera())
print(phone4.get_benchmark())
'''



#5

'''
class Laptop:
    def __init__(self, modeli, ram, cpu, gpu = None):
        self.name = modeli
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu

    def get_full_info(self):
        if self.gpu != None :
            return f"{self.name} notebooki {self.ram}gb operativ xotira, {self.cpu} protsessor , {self.gpu} videokartasi bilan jixozlangan"
        else :
            return f"{self.name} notebooki {self.ram} operativ xotira, {self.cpu} protsessor , {self.cpu}ning integratsiyalashgan videokartasi(iGPU)ga bilan jixozlangan"

    def get_ram(self):
        return f"{self.name} notebooki {self.ram} gb tezkor xotiraga ega"

    def get_cpu(self):
        return f"{self.name} notebooki {self.cpu} protsessoriga ega"

    def get_gpu(self):
        if self.gpu != None:
            return f"{self.name} notebooki {self.gpu} videokartasiga ega"
        else :
            return f"{self.name} notebooki {self.cpu}ning integratsiyalashgan videokartasiga(iGPU)ga ega"


laptop1 = Laptop("HP Victus", 16, "Intel Core i5-13420H", "RTX 3050")
laptop2 = Laptop("Apple Macbook Air", 8, "M4 air" )
laptop3 = Laptop("Asus TUF ", 16, "AMD Ryzen 7-260", "RTX 5050")
laptop4 = Laptop("MSI KATANA", 32, "Intel Core Ultra 7-155H ", "RTX 5060")

print(laptop1.get_full_info())
print(laptop4.get_ram())
print(laptop3.get_cpu())
print(laptop2.get_gpu())
'''