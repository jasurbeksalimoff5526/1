class CarBrand:
    def __init__(self, Brand_name, country, year,  founders):
        self.country = country
        self.year = year
        self.founder = founders
        self.name = Brand_name

    def get_car_brand_info(self):
        return f"{self.name} avtokompaniyasiga {self.year}-yilda {self.founder} tomonidan asos solingan "

bmw = CarBrand("BMW", "Germaniya", 1916, "Camillo Castiglioni")


class Car:
    def __init__(self, brand, model, car_type, motor_capacity, max_speed, price_usd):
        self.model = model
        self.car_type = car_type
        self.motor = motor_capacity
        self.speed = max_speed
        self.price = price_usd
        self.brand = brand

car1 = Car(bmw,"M3 GTR e46", "Oil", 5, 350, 65000 )


class AutoSalon:
    pass