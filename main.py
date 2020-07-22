from admin import *
from admin_choice import *
from book import *

# Вывод апиветствия
menu = Admin() 
# Вывод меню и выбор позиции
loop = True
while loop:       
    menu.print_menu()
    choice = int(input())
# 1.Создание книги 
    if choice == 1:
        choice_1 = AdminChoice()
        title = input('Введите название книги:\n')
        choice_1.create_book(choice, title)
# 2.Добавление главы 
    elif choice == 2:
        choice_2 = AdminChoice()
        title = input('Введите название книги:\n')
        part = input('Введите название главы:\n')
        choice_2.create_part(choice, title, part)
# 3.Дополнение главы 
    elif choice == 3:
        choice_3 = AdminChoice()
        title = input('Введите название книги:\n')
        part = input('Введите название главы:\n')
        text = input('Введите то, чем хотите дополнить:\n')
        choice_3.add_in_part(choice, title, part, text)
# 4.Удаление главы 
    elif choice == 4:
        choice_4 = AdminChoice()
        title = input('Введите название книги:\n')
        part = input('Введите название главы которую хотите удалить:\n')
        choice_4.delite_part(choice, title, part)
# 5.Удаление книги 
    elif choice == 5:
        choice_5 = AdminChoice()
        title = input('Введите название книги, которую хотите удалить:\n')
        choice_5.delite_book(choice, title)
# 6.Вывод всех книг
    elif choice == 6:
        for name, part in library.items():
            print(name, part)
    else:
        loop == False
        print('Выход из программы, всего доброго.')


        
        
    