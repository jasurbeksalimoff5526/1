class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available :
            self.is_available = False
            return f"{self.title} kitobi band qilindi"
        else :
            return "Kitob hozir mavjud emas"

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"{self.title} kitobi qaytarildi"
        return "Kitob qaytarib bo'lingan"

    def info(self):
        status = "Mavjud" if self.is_available else "Band"
        return f"Kitob: {self.title}, Muallif: {self.author}, Holat: {status}"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def take_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            return book.borrow()
        return "Kitobni olish mumkin emas"

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return book.return_book()
        return "Bu kitob foydalanuvchida yo‘q"

    def show_books(self):
        if not self.borrowed_books:
            return "Foydalanuvchida olingan kitoblar yo‘q"

        result = "Olingan kitoblar:\n"
        for book in self.borrowed_books:
            result += f"- {book.title} ({book.author})\n"
        return result


# -----------------------------
# Sinov (test)
# -----------------------------
book1 = Book("Sitsiliyalik", "Mario Pyuzo")
book2 = Book("Baskervillar iti", "Artur Konan Doyl")

user1 = User("Jasurbek")

print(user1.take_book(book1))
print(user1.take_book(book2))
print(user1.show_books())

print(user1.return_book(book1))
print(book1.info())

