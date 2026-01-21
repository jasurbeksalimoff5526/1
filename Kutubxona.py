class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.borrowed_by = None

    def borrow(self, user):
        if self.is_available :
            self.is_available = False
            self.borrowed_by = user
            return f"'{self.title}' kitobi {user.name} tomonidan band qilindi"
        else :
            return f"Kitob hozir mavjud emas, {self.borrowed_by.name} tomonidan band qilingan"

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            self.borrowed_by = None
            return f"'{self.title}' kitobi qaytarildi"
        else:
            return "Kitob qaytarib bo'lingan"

    def info(self):
        if self.is_available:
            status = "Mavjud"
        else:
            status = "Band"
        return f"Kitob: {self.title}, Muallif: {self.author}, Holat: {status}"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def take_book(self, book):
        if book in self.borrowed_books:
            return "Bu kitob allaqachon foydalanuvchida"
        elif book.is_available == True :
            self.borrowed_books.append(book)
            return book.borrow(self)
        return f"{book.title} kitobi hozir mavjud emas, {book.borrowed_by.name} tomonidan band qilingan"

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return book.return_book()
        else:
            return "Bu kitob foydalanuvchida yo‘q, yoki allaqachon qaytarilgan"

    def show_books(self):
        result = f"{self.name} tomonidan olingan kitoblar:"
        if not self.borrowed_books:
            return "Foydalanuvchi kitob olmagan  "
        for i in self.borrowed_books:
            result += f" {i.title} ({i.author}),"
        return result



book1 = Book("Sitsiliyalik", "Mario Pyuzo")
book2 = Book("Baskervillar iti", "Artur Konan Doyl")
book3 = Book("Izquvar Puaro", "Agata Kristi")
book4 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev")

user1 = User("Jasurbek")
user2 = User("Javohir")

print(user1.take_book(book1))
user1.take_book(book2)
user2.take_book(book3)
user2.take_book(book4)
print(user1.take_book(book4))
print(user1.show_books())
print(user2.show_books())
print(user1.return_book(book1))
print(book4.info())



