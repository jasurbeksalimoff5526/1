#1

'''
def read_lines():
    with open("data.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line.strip()

for line in read_lines():
    print(line)
'''

#2

'''
def juft():
    with open("numbers.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            for num in line.split():
                num = int(num)
                if num % 2 == 0:
                    yield num

for line in juft():
    print(line)
'''

#3

'''
def word():
    with open("text.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            for word in line.split():
                if len(word) > 5:
                    yield word

for line in word():
    print(line)
'''

#4

'''
def kvadrat():
    with open("numbers.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            for num in line.split():
                num = int(num)
                yield num**2

for line in kvadrat():
    print(line)
'''

#5

'''
def words():
    with open("words.txt", "r") as f:
        for line in f:
            for word in line.split():
                yield word


for w in words():
    print(w)
'''

#6

'''
import psycopg2

PASSWORD = "5526"   # o'z parolingizni kiriting
DBNAME = "n77_jasurbek" #database nomini yozing

def get_user_names():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user="postgres",
        password=PASSWORD,
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("SELECT first_name FROM users")

    for row in cur:
        yield row[0]

    cur.close()
    conn.close()


for name in get_user_names():
    print(name)
'''

#7

'''
import psycopg2

PASSWORD = "5526"   # o'z parolingizni kiriting
DBNAME = "shop" #database nomini yozing

def price():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user="postgres",
        password=PASSWORD,
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE price > 10000")

    for row in cur:
        yield row

    cur.close()
    conn.close()


for i in price():
    print(i)
'''

#8

'''
import psycopg2

PASSWORD = "5526"   # o'z parolingizni kiriting
DBNAME = "n77_jasurbek" #database nomini yozing

def get_email():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user="postgres",
        password=PASSWORD,
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("SELECT email FROM users")

    for row in cur:
        yield row[0]

    cur.close()
    conn.close()


for email in get_email():
    print(email)
'''

#9

'''
import psycopg2

PASSWORD = "5526"   # o'z parolingizni kiriting
DBNAME = "n77_jasurbek" #database nomini yozing

def users():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user="postgres",
        password=PASSWORD,
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("SELECT first_name FROM users")

    for row in cur:
        yield row[0]

    cur.close()
    conn.close()

longest = ""

for name in users():
    if len(name) > len(longest):
        longest = name

print(longest)
'''

#10

'''
import psycopg2

PASSWORD = "5526"   # o'z parolingizni kiriting
DBNAME = "shop" #database nomini yozing

def users():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user="postgres",
        password=PASSWORD,
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    page = []

    for row in cur:
        page.append(row)

        if len(page) == 5:
            yield page
            page = []

    if page:
        yield page

    cur.close()
    conn.close()


for page in users():
    print(page)
'''


