class Movie:
    def __init__(self, movie_name,  duration_time, director, company):
       self.movie_name = movie_name
       self.duration_time = duration_time
       self.director = director
       self.company = company

    def minute_to_hour(self):
        hour =  self.duration_time//60
        minute = self.duration_time % 60
        return f"{hour} soat {minute} daqiqa"

    def movie_info(self):
        return f"Film nomi: {self.movie_name}\nDavomiyligi: {self.minute_to_hour()}\nRejissior: {self.director}\n{self.company} kino studiyasi maxsuloti"


movie1 = Movie("Interstellar", 169, "Christopher Nolan", "Warner Bros. Pictures")
movie2 = Movie("The Godfather", 177, "Francis Ford Coppola", "Paramount Pictures")
movie3 = Movie("Dark Knight", 152, "Christopher Nolan", "Warner Bros. Pictures")
movie4 = Movie("Shawshenk Redemption", 142, "Frank Darabont", "Columbia Pictures")
movie5 = Movie("Fight Club", 139, "David Fincher", "20th Century Fox")

class Seat:
    def __init__(self, seat_number, is_available=True):
        self.seat_number = seat_number
        self.is_available = is_available

    def __str__(self):
        return f"O‘rin {self.seat_number} ({'bo‘sh' if self.is_available else 'band'})"


class Cinema:
    def __init__(self, cinema_id, cinema_name):
        self.cinema_id = cinema_id
        self.cinema_name = cinema_name
        self.all_movies = []

    def add_movie(self, movie):
        self.all_movies.append(movie)
        return "film qo‘shildi"

cinema1 = Cinema(1, "Compass Cinema")
cinema2 = Cinema(2, "Cinematica")
cinema3 = Cinema(3, "Next Cinema")

cinema1.add_movie(movie1)
cinema1.add_movie(movie2)
cinema1.add_movie(movie3)
cinema1.add_movie(movie4)
cinema1.add_movie(movie5)

cinema2.add_movie(movie3)
cinema2.add_movie(movie4)
cinema2.add_movie(movie5)

cinema3.add_movie(movie3)
cinema3.add_movie(movie4)


class Session:
    def __init__(self, movie, cinema, date, time, price, total_seats):
        self.movie = movie
        self.cinema = cinema
        self.date = date
        self.time = time
        self.price = price
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]

    def get_seat(self, seat_number):
        if seat_number < 1 or seat_number > len(self.seats):
            return None
        return self.seats[seat_number - 1]


s1 = Session(movie1, cinema1, "1-fevral", "15:00", 65000, 35)
s2 = Session(movie2, cinema2, "2-fevral", "14:00", 50000, 50)
s3 = Session(movie3, cinema3, "2-fevral", "17:00", 65000, 60)
s4 = Session(movie4, cinema1, "3-fevral", "12:00", 65000, 45)


class User:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

user1 = User("Ali", "998901234567")
user2 = User("Vali", "998901234567")
user3 = User("Sardor", "998901234567")
user4 = User("Umid", "998901234567")

class Ticket:
    def __init__(self, user, session, seat_number):
        self.user = user
        self.session = session
        self.seat = session.get_seat(seat_number)
        self.status = "new"


    def ticket_info(self):
        if self.status != "reserved":
            return "Chipta band qilinmagan"
        if not self.seat:
            return "Joy topilmadi"
        return (
            f"Ism: {self.user.name}\nFilm: {self.session.movie.movie_name}\n"
            f"Kinoteartr: {self.session.cinema.cinema_name}\nO‘rin: {self.seat.seat_number}\n"
            f"Sana: {self.session.date} {self.session.time}\nNarx: {self.session.price}\n"
            f"Holat: {self.status}"
        )

    def ticket_reservation(self):
        if not self.seat:
            return "Bunday joy mavjud emas"

        if not self.seat.is_available:
            return "Bu joy allaqachon band"

        self.seat.is_available = False
        self.status = "reserved"
        return "Chipta muvaffaqiyatli band qilindi"

# print(movie3.movie_info())


ticket1 = Ticket(user1, s1, 5)
ticket2 = Ticket(user2, s1, 5)

print(ticket1.ticket_reservation())
print(ticket1.ticket_info())
print(ticket2.ticket_reservation())
print(ticket2.ticket_info())
