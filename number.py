class Number:
    def is_number(self, number):
        return number.isdigit

class NumberInterface:
    def __init__(self, class_number):
        self.number = class_number

    def get_print_info(self, user_number):
        if self.number.is_number(user_number):
            print('это число!')
        else:
            print('Это не число')