import psycopg2

NEWDB = 'najot_kutubxona'
p = '5526' # o'z parolimgizni kiriting

def connect(dbname):
    conn = psycopg2.connect(
        dbname=dbname,
        user='postgres',
        password=p,
        port=5432,
        host='localhost'
    )
    conn.autocommit = True
    return conn


def create_database(dbname):
    conn = connect('postgres')
    cur = conn.cursor()

    cur.execute(f"CREATE DATABASE {dbname}")
    print(cur.statusmessage)
    conn.close()

create_database(NEWDB)


def create_table(db_name, table_name, columns_type):
    conn = connect(f"{db_name}")
    cur = conn.cursor()

    cur.execute(f"""
        CREATE TABLE {table_name}({columns_type})
        """)
    print(cur.statusmessage)
    conn.close()

users_column_type = 'id SERIAL PRIMARY KEY, full_name VARCHAR(100), email VARCHAR(100), password TEXT, created_at TIMESTAMP'
genres_column_type = 'id SERIAL PRIMARY KEY, name VARCHAR(50)'
authors_column_type = 'id SERIAL PRIMARY KEY, full_name VARCHAR(100), country VARCHAR(100)'
books_column_type = 'id SERIAL PRIMARY KEY, title VARCHAR(150), authors_id INT REFERENCES authors(id), description TEXT, published_year INT, genres_id INT REFERENCES genres(id)'
comments_column_type = 'id SERIAL PRIMARY KEY, user_id INT REFERENCES users(id), book_id INT REFERENCES books(id), content TEXT, created_at TIMESTAMP'

create_table(NEWDB, 'users', users_column_type)
create_table(NEWDB, 'genres', genres_column_type)
create_table(NEWDB, 'authors', authors_column_type)
create_table(NEWDB, 'books', books_column_type)
create_table(NEWDB, 'comments', comments_column_type)

def add_data(db_name, table_name, columns, values):
    conn = connect(f"{db_name}")
    cur = conn.cursor()

    cur.execute(f"""
            INSERT INTO  {table_name} ({columns}) VALUES {values}
            """)
    print(cur.statusmessage)
    conn.close()

column1 = "full_name, email, password"
data1 = "('XASAN', 'xasan@mail.com', 'xasan'),  ('XUSAN', 'xusan@mail.com', 'xusan'), ('ALI', 'ali@gmail.com', 'ali777')"


add_data(NEWDB, 'users', column1, data1 )


#1 SELECT * FROM books ORDER BY published_year;
#2 SELECT genres_id, COUNT(*) FROM books LEFT JOIN genres ON genres.id = books.genres_id GROUP BY genres_id;
#3 SELECT * FROM comments LEFT JOIN books ON comments.book_id = books.id WHERE content IS NULL;
