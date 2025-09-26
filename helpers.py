import random


class Helpers():
    @staticmethod
    def create_random_password():
        password = random.randint(100000, 999999)
        return password

    @staticmethod
    def create_random_email():
        number = random.randint(000000, 999999)
        email = f'mariakobzar_{number}@gmail.com'
        return email

    @staticmethod
    def create_random_error_password():
        password = random.randint(0, 99999)
        return password