from work_with_db import work_db


class User:

    def __init__(self, phone, first_name, date_of_birth):
        self.phone = phone
        self.first_name = first_name
        self.date_of_birth = date_of_birth

        print(f'User {self.first_name} created')

    def create_user(self):
        work_db.add_simple_record(self.phone, self.first_name, 'cscsdcds', self.date_of_birth)
        print(f'User with Name: {self.first_name} || phone number: {self.phone} || date of birth: {self.date_of_birth} created')

    def show_all_record(self):
        print(f'Name: {self.first_name} || phone number: {self.phone} || date of birth: {self.date_of_birth}')
        work_db.show_content_table()

    def show_one_record(self):
        print("=== One record++")
        work_db.show_content_table_only_one_value(self.phone, 'phone_number')


class Developer(User):

    def __init__(self, phone, first_name, date_of_birth, language):
        super().__init__(phone, first_name, date_of_birth)
        self.language = language

    def show(self):
        print(
            f'Name: {self.first_name} || phone number: {self.phone} || date of birth: {self.date_of_birth} || language: {self.language}')


user = User(111121221, 'Ivan', '02.02.02')
user.create_user()
user.show_all_record()
user.show_one_record()



# developer = Developer('09999987', 'Dev', '121212', 'Java')
#
# developer.show()
