class Author:
    def __init__(self, first_name, last_name, year, country):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.country = country

    def get_info(self):
        return f"Ism: {self.first_name}, familiya: {self.last_name}, tugilgan yili: {self.year}, manzili: {self.country}"


a1 = Author('Jahongir', 'Mirzayorov', 2006, 'Toshkent')
a2 = Author('Jasmina', 'Nematullayeva', 2005, 'Toshkent')
a3 = Author('Jasurbek', 'Salimov', 2000, 'Qarshi')


class Books:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_info(self):
        return f"Nomi: {self.title}, Muallifi: {self.author.first_name}, Narxi: {self.price}"


b1 = Books('Cambridge', a1, 59000)
b2 = Books('Golib Iroda', a2, 100000)
b3 = Books('Hayotga Muhabbat', a3, 85000)
b4 = Books('1984', a2, 45000)


# print(b4.get_info())


class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"{book.title} kitobi qo'shildi"

    def get_books(self):
        for i in self.books:
            print(i.get_info())

    def detail_book(self, book_name):
        for i in self.books:
            if i.title == book_name:
                return i.get_info()
        else:
            return 'Bizda bu kitob mavjud emas'

    def delete_book(self, book_name):
        for i in self.books:
            if i.title == book_name:
                self.books.remove(i)
                return f"{i.title} kitobi o'chirildi"

        else:
            return "Bizda bu kitob mavjud emas"

    def update_book(self, book_name, title=None, price=None, author=None):
        for i in self.books:
            if i.title == book_name:
                if title:
                    i.title = title
                if price:
                    i.price = price
                if author:
                    i.author = author

                return f"Kitob o'zgartirildi\n{i.get_info()}"

        else:
            return "Bizda bu kitob mavjud emas"


s1 = BookStore()

s1.add_book(b1)
s1.add_book(b2)
s1.add_book(b3)
s1.add_book(b4)

# s1.get_books()

# c-create
# r-read(detail, list)
# u-update
# d-delete


print(s1.update_book('1984', price=65000, author=a3))
# s1.get_books()
