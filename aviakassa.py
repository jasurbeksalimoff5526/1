class Airplane:
    def __init__(self, brand, model, capacity, max_speed):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.max_speed = max_speed

    def plane_info(self):
        return f"Samolyot: {self.brand} {self.model}\nO'rindiqlar soni: {self.capacity}\nMaksimal tezlik: {self.max_speed}"


boeing = Airplane("Boeing", "737", 180, 850)
airbus = Airplane("Airbus", "A320", 170, 830)


class Ticket:
    def __init__(self, airplane, from_city, to_city, price):
        self.airplane = airplane
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

    def ticket_info(self):
        return f"{self.from_city} → {self.to_city}\nSamolyot: {self.airplane.brand} {self.airplane.model}\nNarx: {self.price}$"


ticket1 = Ticket(boeing, "Toshkent", "Istanbul", 450)
ticket2 = Ticket(airbus, "Qarshi", "Dubai", 500)


class Aviakassa:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)
        return "Bilet qo‘shildi"

    def get_tickets(self):
        for i in self.tickets:
            return i.ticket_info()

    def detail_ticket(self, from_city):
        for i in self.tickets:
            if i.from_city == from_city:
                return i.ticket_info()
        return "Bunday reys topilmadi"

    def update_ticket(self, from_city, to_city=None, price=None, airplane=None):
        for i in self.tickets:
            if i.from_city == from_city:
                if to_city:
                    i.to_city = to_city
                if price:
                    i.price = price
                if airplane:
                    i.airplane = airplane
                return "Bilet yangilandi"
        return "Bilet topilmadi"


kassa = Aviakassa()
kassa.add_ticket(ticket1)
kassa.add_ticket(ticket2)

print(kassa.update_ticket("Toshkent", "Los angelas", 550, airbus))
print(kassa.detail_ticket("Toshkent"))

# print(kassa.update_ticket("Qarshi", "Tokio", 700, boeing))
# print(kassa.detail_ticket("Qarshi"))





