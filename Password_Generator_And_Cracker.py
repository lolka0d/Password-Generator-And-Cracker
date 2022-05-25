import itertools
import random
import time


class Password_Generator:
    def __init__(self, password_length: int, password_symbols: str):
        self.password = ''
        self.password_length = password_length
        self.password_symbols = password_symbols

    def generate_password(self):
        for i in range(self.password_length):
            self.password += random.choice(self.password_symbols)

        return self.password


class Password_Cracker:
    def __init__(self, password_length: int, password_symbols: str, real_password=None):
        self.password_length = password_length
        self.password_symbols = password_symbols
        self.not_accepted_password = ''
        self.real_password = real_password
        self.password_count = 0

    def crack_password(self):
        start_time = time.time()
        for password in itertools.product(self.password_symbols, repeat=self.password_length):
            password = ''.join(password)
            if password == self.real_password:
                print('\nPassword: ' + password)
                print(f'Cracked in {time.time() - start_time}')
                exit(1)
            else:
                self.password_count += 1
                print(f'Incorrect count password: {self.password_count}', end='\r')
        return '\nIncorrect data!'

    def random_crack_password(self):
        cracked_list = []
        start_time = time.time()
        while True:
            for i in range(self.password_length):
                self.not_accepted_password += random.choice(self.password_symbols)
            if self.not_accepted_password in cracked_list:
                continue
            if self.not_accepted_password == self.real_password:
                print(f"\nPassword: {self.not_accepted_password}")
                print(f'Cracked in {time.time() - start_time}')
                exit(1)
            else:
                print(f'Incorrect count password: {len(cracked_list)}', end='\r')
            if len(self.password_symbols) ** self.password_length == len(cracked_list):
                return '\nIncorrect data!'
            cracked_list.append(self.not_accepted_password)
            self.not_accepted_password = ''
