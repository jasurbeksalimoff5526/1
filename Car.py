class CarBrand:
    def __init__(self, brand_name, country, year,  founders):
        self.country = country
        self.year = year
        self.founder = founders
        self.name = brand_name

    def get_car_brand_info(self):
        return f"{self.name} avtokompaniyasiga {self.year}-yilda {self.founder} tomonidan asos solingan "


bmw = CarBrand("BMW", "Germaniya", 1916, "Camillo Castiglioni")
lamborghini = CarBrand("Lamborghini", "Italiya", 1963, "Ferruccio Lamborghini")

class Car:
    def __init__(self, brand, model, car_type, engine_capacity, max_speed, price_usd):
        self.brand = brand
        self.model = model
        self.car_type = car_type
        self.engine = engine_capacity
        self.speed = max_speed
        self.price = price_usd

    def car_info(self):
        return f"model: {self.model}\nYoqilg'i turi: {self.car_type}\nMotor hajmi: {self.engine}\nMaksimal tezligi: {self.speed}\nNarxi: {self.price}$"


car1 = Car(bmw,"M3 GTR e46", "Oil", 5, 350, 65000 )
car2 = Car(lamborghini, "Huracan", "Oil", 5, 260, 80000)


class AutoSalon:
    def __init__(self):
        self.allcars = []

    def add_car(self, car):
        self.allcars.append(car)
        return f"{car.model} rusumli avtomobil qo'shildi"

    def get_cars(self):
        for i in self.allcars:
            return i.car_info()

    def detail_cars(self, car_name):
        for i in self.allcars:
            if i.model == car_name:
                return i.car_info()
        else:
            return f"Bizda bunday mashina yo'q"

    def update_cars(self, car_name, car_type=None, price=None, max_speed=None):
        for i in self.allcars:
            if i.model == car_name:
                if car_type:
                    i.car_type = car_type
                if price:
                    i.price = price
                if max_speed:
                    i.speed = max_speed

                return f"Mashina o'zgartirildi\n{i.car_info()}"

c1 = AutoSalon()

c1.add_car(car1)
c1.add_car(car2)


print(c1.update_cars("Huracan", "Electro", 100000, 320))

# print(c1.get_cars())



