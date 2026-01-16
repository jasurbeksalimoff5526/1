#1 single-1

'''
class Person:
    def __init__(self, ismi, yoshi, malumoti):
        self.name = ismi
        self.age = yoshi
        self.graduation = malumoti

    def get_person_info(self):
        return f"Ismi: {self.name}\nYoshi: {self.age}\nMalumoti: {self.graduation}"


class Worker(Person):
    def __init__(self, ismi, yoshi, malumoti, ish_tajribasi):
        super().__init__(ismi, yoshi, malumoti)
        self.experience = ish_tajribasi

    def get_worker_experience(self):
        return f"{self.get_person_info()}\nIsh tajribasi: {self.experience}"


w1 = Worker("Jon", 29, "Bakalavr", "4 yil")
print(w1.get_worker_experience())
'''



#2 single-2 check read message

'''
class PersonID:
    def __init__(self, username, userid ):
        self.name = username
        self.id = userid

    def get_info_user(self):
        return f"Username: {self.name}\nUserID: {self.id}"


class CheckReadMessage(PersonID):
    def __init__(self, username, userid, check = False):
        super().__init__(username, userid)
        self.check = check

    def check_read_message(self):
        if self.check == True:
            return f"{self.get_info_user()}\nCheck read status: xabar o'qildi"
        else:
            return f"{self.get_info_user()}\nCheck read status: xabar o'qilmadi"


status = CheckReadMessage("@telegram", "123456", True) 
print(status.check_read_message())
'''



#3 multilevel-1

'''
class Transport:
    def __init__(self, make, year, weight, speed ):
        self.make = make
        self.year = year
        self.weight = weight
        self.speed = speed

    def get_transport_info(self):
        return f"Ishlab chiqarilgan: {self.make}\nYili: {self.year}\nOg'irligi: {self.weight}\nTezligi: {self.speed}"


class AirTransport(Transport):
    def __init__(self, make, year, weight, speed, flight_altitude, fly_range):
        super().__init__(make, year, weight, speed)
        self.alt = flight_altitude
        self.range = fly_range

    def get_flight_altitude(self):
        return f"Uchish balandligi: {self.alt}\nUchish masofasi: {self.range}"


class Helicopter(AirTransport):
    def __init__(self, make, year, weight, speed, flight_altitude, fly_range, hover):  # hover - havoda muallaq turish vaqti
        super().__init__(make, year, weight, speed, flight_altitude, fly_range)
        self.hover = hover

    def get_helicopter_info(self):
        return f"{self.get_transport_info()}\n{self.get_flight_altitude()}\nHavoda muallaq tura olish vaqti: {self.hover}"


helicopter = Helicopter("USA", "2026", "1.5 tonna", "300km/h", "1km", "500km", "15 daqiqa")
print(helicopter.get_helicopter_info())
'''



#4 multilavel-2

'''
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_person_info(self):
        return f"Ismi: {self.first_name}\nFamiliyasi: {self.last_name}\nYoshi: {self.age}"


class Junior(Person):
    def __init__(self, first_name, last_name, age, sertificate, programming_language):
        super().__init__(first_name, last_name, age)
        self.sertificate = sertificate
        self.language = programming_language

    def get_junior_info(self):
        return f"{self.get_person_info()}\nDasturlash tili: {self.language}\nKursni tamomlagan: {self.sertificate}"


class Middle(Junior):
    def __init__(self, first_name, last_name, age, sertificate, programming_language, experience, worked):
        super().__init__(first_name, last_name, age, sertificate, programming_language)
        self.experience = experience
        self.worked = worked

    def get_middle_info(self):
        return f"Middle dasturchi ma'lumotlari\n{self.get_junior_info()}\nIshlagan joyi: {self.worked}\nTajribasi: {self.experience}"


person = Middle("Jasurbek", "Salimov", 25, "Najot ta'lim", "python", "3 yil","EPAM, GOOGLE")
print(person.get_middle_info())
'''



#5 multiple-1

'''
class Computer:
    def __init__(self, cpu_ghz, ram_gb, storage_gb):
        self.cpu = cpu_ghz
        self.ram = ram_gb
        self.storage = storage_gb

    def get_computer_info(self):
        return f"CPU: {self.cpu} GHZ, RAM: {self.ram} GB, Xotira: {self.storage} GB"


class OS:
    def __init__(self, os_name, os_year, ):
        self.os_name = os_name
        self.os_year = os_year

    def get_os_info(self):
        return f"Operatsion tizim nomi: {self.os_name}, {self.os_name} yangilangan yili: {self.os_year}"


class Application(Computer, OS):
    def __init__(self,cpu_ghz, ram_gb, storage_gb, os_name, os_year):
        Computer.__init__(self, cpu_ghz, ram_gb, storage_gb)
        OS.__init__(self, os_name, os_year)

    def get_pycharm_requirements(self):
        if self.cpu < 2 : #GHZ
            return "CPU minimal talablarga mos emas"
        if self.ram < 2 : #GB
            return "RAM yetarli emas"
        if self.storage < 4 : #GB
            return "RAM yetarli emas"
        if self.os_name not in ("windows", "macos", "linux"):
            return "Operatsion tizim mos emas"
        if self.os_year < 2019:
            return "Operatsion tizim yili talablarga mos emas"

        return f"PyCharm dasturini o'rnatish mumkin, minimal tizim talablariga mos"


app = Application(3, 4, 100, "windows", 2025)

print(app.get_computer_info())
print(app.get_os_info())
print(app.get_pycharm_requirements())
'''



#6

'''
class Person:
    def __init__(self, ismi, familiyasi, jshshir):
        self.first_name = ismi
        self.last_name = familiyasi
        self.passport_id = jshshir

    def get_person_info(self):
        return f"Yo'lovchi ismi: {self.first_name}\nYo'lovchi familiyasi: {self.last_name}\nPassport ID: {self.passport_id}"


class Train:
    def __init__(self, bu_yerdan, bu_yerga,  sanasi):
        self.fromm = bu_yerdan
        self.to = bu_yerga
        self.date = sanasi

    def get_check_train(self):
        return f"Qayerdan: {self.fromm}\nQayerga: {self.to}\nSanasi: {self.date} "


class TicketWebsite(Person, Train):
    def __init__(self, ismi, familiyasi, jshshir, bu_yerdan, bu_yerga,  sanasi, vagon, orindiq):
        Person.__init__(self, ismi, familiyasi, jshshir)
        Train.__init__(self, bu_yerdan, bu_yerga,  sanasi)
        self.wagon = vagon
        self.seat = orindiq

    def get_ticket_info(self):
        return f"Bilet ma'lumotlari\n{self.get_person_info()}\n{self.get_check_train()}\nVagon: {self.wagon}\nO'rindiq: {self.seat}"


a = TicketWebsite("Jasurbek", "Salimov", "123456", "Toshkent", "Qarshi", "25-dekabr", 6, 13)

print(a.get_ticket_info())
'''