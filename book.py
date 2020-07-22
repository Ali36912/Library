# -*- coding: utf8 -*-
import uuid
import os
from shutil import rmtree

library = {}
# 1.Создание книги 
class Book():
    def __init__(self, title):
        if title not in library:
            self.title = title
            self.id = uuid.uuid1()
            self.quantity_part = 0       
            os.mkdir(self.title)
            
            file_name = open(title + '/info.txt', 'w', encoding='utf-8')
            file_name.write(title + '\nid книги: ' + str(self.id) + '\nКолличество глав: ' + str(self.quantity_part))
            file_name.close()

            library.update({title:self.quantity_part})
        else:
            self.title = title
            self.id = uuid.uuid1()
            for book, part in library.items():
                self.quantity_part = part
                pass
# 2.Добавление главы
    def add_part(self, book, part):
        self.part = part                   
        file_name = open(book + '/' + part + '.txt', 'w', encoding='utf-8' )
        file_name.write(part)
        file_name.close()
        self.quantity_part += 1
        library.update({book:self.quantity_part})

        file_name = open(self.title + '/info.txt', 'w', encoding='utf-8')
        file_name.write(self.title + '\nid книги: ' + str(self.id) + '\nКолличество глав: ' + str(self.quantity_part))
        file_name.close()            
# 3.Дополнение главы
    def add_in_part(self, book, part, text):               
        chek_file = os.path.exists(book + '/' + part + '.txt')
        if chek_file == True:
            file_name = open(self.title + '/' + part + '.txt', 'a', encoding='utf-8' )
            file_name.write('\n' + text)
            file_name.close()
        else:
            print('Такой главы не существует')
# 4.Удаление главы 
    def delite_part(self, book, part):        
        chek_file = os.path.exists(book + '/' + part + '.txt')
        if chek_file == True:
            os.remove(self.title + '/' + part + '.txt')
            self.quantity_part -= 1
            library.update({book:self.quantity_part})
        else:
            print('Главы ' + part + ' не существует.')
# 5.Удаление книги 
    def delite_book(self, book):        
        rmtree(book)
        library.pop(book, self.quantity_part)

        




                    

    

        
        




