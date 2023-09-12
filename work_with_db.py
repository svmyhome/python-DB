from getpass import getpass
from mysql.connector import connect, Error

HOST = 'localhost'
USER = 'root'
PASSWORD = 'passw'
TABLE = 'users'


class Work_DB:

    def __init__(self, user, password, name_db):
        self.user = user
        self.password = password
        self.name_db = name_db

    def show_db(self):

        try:
            with connect(
                    host=HOST,
                    user=self.user,
                    password=self.password,
            ) as connection:
                show_db_query = "SHOW DATABASES"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        except Error as e:
            print(e)

    def create_new_db(self):
        try:
            with connect(
                    host=HOST,
                    user=self.user,
                    password=self.password,
            ) as connection:
                create_db_query = f'CREATE DATABASE {self.name_db}'
                with connection.cursor() as cursor:
                    cursor.execute(create_db_query)
        except Error as e:
            print(e)

    def show_tables_db(self):
        try:
            with connect(
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                show_db_query = "SHOW TABLES"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        except Error as e:
            print(e)

    def create_new_table(self, new_table):

        try:
            with connect(  # TODO Maybe this block can move to the simple def
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(new_table)
                    connection.commit()
        except Error as e:
            print(e)

    def show_structure_table(self):
        try:
            with connect(
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                show_db_query = f'DESC {TABLE}'
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        except Error as e:
            print(e)

    def show_content_table(self):
        try:
            with connect(
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                show_db_query = f'SELECT * FROM {TABLE}'
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        except Error as e:
            print(e)

    def show_content_table_only_year(self, date_of_birth):
        try:
            with connect(
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                show_db_query = f'SELECT * FROM {TABLE} WHERE date_of_birth = {date_of_birth}'
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        except Error as e:
            print(e)
    def change_type_row(self, table_name, column_name, type_data):
        alter_table_query = f"""
        ALTER TABLE {table_name} MODIFY COLUMN {column_name} {type_data}
        """
        try:
            with connect(  # TODO Maybe this block can move to the simple def
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(work_db.show_structure_table())
                    print('----')
                    cursor.execute(alter_table_query)
                    cursor.execute(work_db.show_structure_table())
                    connection.commit()
        except Error as e:
            print(e)

    def drop_table(self, table_name):
        drop_table = f"""
                DROP TABLE {table_name}
                """
        try:
            with connect(  # TODO Maybe this block can move to the simple def
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(drop_table)
                    connection.commit()
        except Error as e:
            print(e)

    def add_several_record(self, insert_query):

        try:
            with connect(  # TODO Maybe this block can move to the simple def
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(insert_query)
                    connection.commit()
        except Error as e:
            print(e)

    def add_multiple_records(self, insert_multiple_query, multiple_query):

        try:
            with connect(  # TODO Maybe this block can move to the simple def
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.executemany(insert_multiple_query,
                                       multiple_query)
                    connection.commit()
        except Error as e:
            print(e)

    def update_record(self, update_record):

        try:
            with connect(  # TODO Maybe this block can move to the simple def
                    host=HOST,
                    user=self.user,
                    password=self.password,
                    database=self.name_db
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(update_record)
                    connection.commit()
        except Error as e:
            print(e)

work_db = Work_DB(USER, PASSWORD, 'my_test')
print('====== SHOW DB =====')
work_db.show_db()
print('===== SHOW TABLES ======')
new_table = """
CREATE TABLE movies1(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""
work_db.create_new_table(new_table)

print('===========')
work_db.show_tables_db()

print('===========')
work_db.show_structure_table()

print('===========')
work_db.show_content_table()

print('===== CHANGE TYPE ROW======')
work_db.change_type_row(TABLE, 'phone_number', 'INT')

print('===== DROP TABLE ======')
work_db.drop_table('movies')
work_db.show_tables_db()

print('===== Add several records ======')
insert_query = """
INSERT INTO users(phone_number, first_name, last_name, date_of_birth) values (1212, "Ivan", "IVANKO", "2342"),(1212, "Petr", "petrov", "1112342")
"""
work_db.add_several_record(insert_query)
work_db.show_content_table()

print('===== Add several records ======')
insert_multiple_query = """
INSERT INTO users(phone_number, first_name, last_name, date_of_birth) values(%s, %s, %s, %s)
"""
multiple_query = [(1212, "Ivan", "IVANKO", "2342"), (1212, "Ivan", "IVANKO", "2342"), (1212, "Ivan", "IVANKO", "2342"),
                  (1212, "Ivan", "IVANKO", "2342"), (1212, "Ivan", "IVANKO", "2342"), (1212, "Ivan", "IVANKO", "2342")]
work_db.add_multiple_records(insert_multiple_query, multiple_query)
work_db.show_content_table()

print('===== Add several records ======')
work_db.show_content_table_only_year('2342')

print('===== Update record ======')
update_record ="""
UPDATE users SET first_name = "lcdlcldl"  WHERE date_of_birth = "1112342" 
"""
work_db.update_record(update_record)
work_db.show_content_table()
# work_db1 = Work_DB(USER, PASSWORD, 'online_movie_rating')
# work_db1.create_new_db()
#
# work_db1.show_db()
