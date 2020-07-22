from book import *

class AdminChoice():
    def create_book(self, choice, title):# 1.Создание книги 
        if choice == 1:
            books = Book(title)

    def create_part(self, choice, title, part_name):# 2.Добавление главы 
        if choice == 2:
            books = Book(title)
            books.add_part(title, part_name)

    def add_in_part(self, choice, title, part_name, text):# 3.Дополнение главы 
        if choice == 3:
            books = Book(title)
            books.add_in_part(title, part_name, text)

    def delite_part(self, choice, title, part_name):# 4.Удаление главы 
        if choice == 4:
            books = Book(title)
            books.delite_part(title, part_name)
        
    def delite_book(self, choice, title):# Удаление 5.книги 5 
        if choice == 5:
            books = Book(title)
            books.delite_book(title)
   

        