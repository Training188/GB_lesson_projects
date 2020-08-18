'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.'''

'''my_list = []
user_date = None
while user_date != '000':
    user_date = input('Enter any date: ')
    if user_date != '000':
        if user_date.isdigit():
            my_list.append(int(user_date))
    else:
        my_list.append(user_date)
        break
for el in my_list:
    print(type(el))'''

my_list = [1, 3.14, True, 'Hello', 5+6j, (1, 2, 3), [1, 2, 3]]
for i in my_list:
    print(type(i))