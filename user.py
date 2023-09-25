from work_with_db import work_db
import datetime as dt


class User:

    def __init__(self, phone, first_name, date, month, year):
        self.phone = phone
        self.first_name = first_name
        self.date = date
        self.month = month
        self.year = year
        self.birthday = (dt.datetime(self.year, self.month, self.date)).strftime('%Y-%m-%d')

        print(f'User {self.first_name} created')

    def create_user(self):
        work_db.add_simple_record(self.phone, self.first_name, 'cscsdcds', self.birthday)
        print(
            f'User with Name: {self.first_name} || phone number: {self.phone} || birthday: {self.birthday} created')

    def show_all_record(self):
        print(f'Name: {self.first_name} || phone number: {self.phone} || birthday: {self.birthday}')
        work_db.show_content_table()

    def show_one_record(self):
        print("=== One record++")
        work_db.show_content_table_only_one_value(self.phone, 'phone_number')


class Developer(User):

    def __init__(self, phone, first_name, date, month, year, language):
        super().__init__(phone, first_name, self.date, self.month, self.year)
        self.language = language

    def show(self):
        print(
            f'Name: {self.first_name} || phone number: {self.phone} || date of birth: {self.birthday} || language: {self.language}')


user = User(22222222, 'Ivan', 2, 12, 1979)
user.create_user()
user.show_all_record()
user.show_one_record()

# developer = Developer('09999987', 'Dev', '121212', 'Java')
#
# developer.show()
