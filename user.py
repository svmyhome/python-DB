class User:

    def __init__(self, phone, first_name, date_of_birth):
        self.phone = phone
        self.first_name = first_name
        self.date_of_birth = date_of_birth

        print(f'User {self.first_name} created')

    def show(self):
        print(f'Name: {self.first_name} || phone number: {self.phone} || date of birth: {self.date_of_birth}')


class Developer(User):

    def __init__(self, phone, first_name, date_of_birth, language):
        super().__init__(phone, first_name, date_of_birth)
        self.language = language

    def show(self):
        print(
            f'Name: {self.first_name} || phone number: {self.phone} || date of birth: {self.date_of_birth} || language: {self.language}')


user = User('23456789', 'Ivan', '01.01.01')
user.show()

developer = Developer('09999987', 'Dev', '121212', 'Java')

developer.show()
