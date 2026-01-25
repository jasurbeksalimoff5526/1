class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    @property
    def narx(self):
        return self.__price

    @narx.setter
    def narx(self, a):
        if a < 0:
            print("Narx manfiy bo'la olmaydi")
        else:
            self.__price = a
            print(f"{self.name} narxi {a} ga o'zgardi")

    @property
    def soni(self):
        return self.__stock

    @soni.setter
    def soni(self, a):
        if a < 0:
            print("maxsulot soni manfiy bo'la olmaydi")
        else:
            self.__stock = a
            print(f"{self.name} soni {a} taga o'zgardi")


    def reduce_stock(self, quantity):
        if quantity > self.__stock:
            print(f"{self.name} dan yetarli mahsulot yoq!")
            return False
        self.__stock -= quantity
        return True


p1 = Product("daftar", 30000, 20)
p2 = Product("ruchka", 19000, 55)
p3 = Product("qalam", 20000, 68)
p4 = Product("marker", 35000, 15)




class Order:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = quantity
        return self.products

    def calculate(self):
        total = 0
        for product, quantity in self.products.items():
            total += product.narx * quantity
        return total

    def all_products(self):
        for product, quantity in self.products.items():
            print(f"{product.name} {quantity} ta")


savat = Order()
savat.add_product(p1, 25)
savat.add_product(p2, 15)
savat.add_product(p3, 55)

savat.all_products()



class Warehouse:
    @staticmethod
    def check_stock(order):
        """Agar biron mahsulot yetarli bolmasa, False qaytaradi"""
        for i, k in order.products.items():
            if i.soni < k:
                del order.products[i]
                print(f"{i.name} dan yetarli mahsulot yoq. Buyurtmadan {i.name} chiqarib yuborildi!")
                return False
        return True


class SmartOrder(Order):
    def __init__(self):
        super().__init__()

    def apply_discount(self):
        total = super().calculate()
        if total > 1000000:
            total *= 0.9
        return int(total)



s = SmartOrder()
s.products = savat.products
p1.narx=32000
print(p1.narx)
print("buyurtmaning umimiy narxi:", savat.calculate())
print(Warehouse.check_stock(savat))
print("yakuniy chegirmadagi narx:", s.apply_discount())

savat.all_products()












