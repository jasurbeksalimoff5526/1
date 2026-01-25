class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_available = False

    def make_available(self):
        self.is_available = True

    def make_unavailable(self):
        self.is_available = False

    def food_status(self):
        if self.is_available == True:
            return f"{self.name} taomi narxi {self.price} so'm, xozirda buyurtma berish uchun mavjud"
        else:
            return f"{self.name} taomi narxi {self.price} so'm, xozirda buyurtma berish uchun mavjud emas"

food1 = MenuItem("Osh", 35000)
food2 = MenuItem("Manti", 12000)
food3 = MenuItem("Sho'rva", 40000)
food4 = MenuItem("Shashlik", 17000)

food1.make_available()
food2.make_available()
food3.make_available()
food4.make_available()


class Order:
    def __init__(self, order_id, status="new"):
        self.order_id = order_id
        self.order_items = {}    # {food : quantity}
        self.status = status

    def add_item(self, food):
        if food.is_available == True:
            if food not in self.order_items:
                self.order_items[food] = 1
                return f"{self.order_id}-buyurtmaga {food.name} qo'shildi"
            elif food in self.order_items:
                self.order_items[food] += 1
                return f"{self.order_id}-buyurtmaga {food.name} qo'shildi"
        else :
            return f"{self.order_id}-buyurtmaga {food.name} qo'shilmadi, {food.name} taomi xozirda mavjud emas"

    def remove_item(self, food):
        if food in self.order_items:
            del self.order_items[food]
        else :
            return f"{self.order_id} buyurtmada bunday taom yo'q"

    def get_total(self):
        total = 0
        for i,k in self.order_items.items():
            total += i.price * k
        return total

    def change_status(self, new_status):
        self.status = new_status

order1 = Order("N1")
order2 = Order("N2")
order3 = Order("N3")
order4 = Order("N4")

order1.change_status("cooking")
order2.change_status("done")

order1.add_item(food1)
order1.add_item(food2)
order1.add_item(food2)
order1.add_item(food3)
order2.add_item(food2)
order2.add_item(food4)
order2.add_item(food4)
order3.add_item(food3)


class Cashier:
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name

    def accept_payment(self, order):
        if order.status == "done":
            return f"{order.order_id} bururtma tayyor mijozdan to'lov qabul qiling"
        else:
            return f"to'lov qabul qilib bo'lmaydi, {order.order_id} buyurtma hali tayyor emas"

    def print_receipt(self, order):
        info = f"Chek --{order.order_id}--\nKassir: {self.cashier_name}\n"
        for i,k in order.order_items.items():
            info += f"'{i.name}' {k} ta, {i.price}x{k}\n"
        if order.get_total() > 40000:
            info += f"(non va choy bonus)"    # buyurtma 40mingdan oshsa non choy bonus
        return f"{info}\numumiy narx: {order.get_total()}"

c1 = Cashier("Sardor")
c2 = Cashier("Javohir")


class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = {}

    def add_menu_item(self, food):
        if food not in self.menu:
            self.menu.append(food)
            return f"Menyuga {food.name} taomi qo'shildi"
        else:
            return f"{food.name} menyuda avvaldan mavjud"

    def show_menu(self):
        available_menu = []
        for i in self.menu:
            if i.is_available == True:
                available_menu.append(i.name)
        return f"Hozirda {', '.join(available_menu)} taomlari mavjud"

    def add_order(self, order):
        if order in self.orders:
            return f"{order.order_id} buyurtma allaqachon qo'shib bo'lingan"
        self.orders[order.order_id] = order
        return f"{order.order_id} buyurtma qo'shildi"

    def create_order(self, new_order_id, food):
        if new_order_id in self.orders:
            return "bu buyurtma avval yaratib bo'lingan"

        order = Order(new_order_id)
        order.add_item(food)
        self.orders[new_order_id] = order
        return order


r = Restaurant()

r.add_menu_item(food1)
r.add_menu_item(food2)
r.add_menu_item(food3)

# r.add_order(order1)
r.add_order(order2)
r.add_order(order3)
r.add_order(order4)

r.create_order("A1" , food3)
r.create_order("A2" , food3)
r.create_order("A3" , food3)
r.create_order("A4" , food3)
# print(r.create_order("A5" , food3))


# print(r.orders)
# print(r.add_menu_item(food4))
# print(food1.food_status())
# print(order1.remove_item(food4))
# print(c1.print_receipt(order1))
# print(c2.accept_payment(order2))
# print(r.show_menu())

