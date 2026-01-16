class Cars:
    def __init__(self, make, model, color, year, oil_type):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.oil_type = oil_type

    def get_car_info(self):
        return f"Model: {self.model}\nMake: {self.make}\nColor: {self.color}\nYear: {self.year}\nOil: {self.oil_type}"


class ElectroCars(Cars):
    def __init__(self, make, model, color, year, oil_type, battery, km):
        Cars.__init__(self, make, model, color, year, oil_type)
        self.battery = battery
        self.km = km

    def get_electro_car_info(self):
        return f"{self.get_car_info()}\nBattery: {self.battery}\nKM: {self.km}"


class OilCars(Cars):
    def __init__(self, make, model, color, year, oil_type, mator, mator_type):
        Cars.__init__(self, make, model, color, year, oil_type)
        self.mator = mator
        self.mator_type = mator_type

    def get_oil_car_info(self):
        return f"{self.get_car_info()}\nMator: {self.mator}\nMator type: {self.mator_type}"


class HybridCars(OilCars, ElectroCars):
    def __init__(self, make, model, color, year, oil_type, mator, mator_type, battery, km, hybrid_type):
        OilCars.__init__(self, make, model, color, year, oil_type, mator, mator_type)
        ElectroCars.__init__(self, make, model, color, year, oil_type, battery, km)
        self.hybrid_type = hybrid_type

    def get_hybrid_car_info(self):
        return f"Hybrid type: {self.hybrid_type}"


h1 = HybridCars("BYD", 'Chazpr', 'black', 2025, 95, 100, 1.5, 144.4, 1200, 'Plagin')
print(h1.get_hybrid_car_info())
