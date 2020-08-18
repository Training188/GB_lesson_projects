'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''

seasons_list = ['winter', 'spring', 'summer', 'fall']
seasons_dict = {
    'winter':  ('December', 'January', 'February'),
    'sprint':  ('March', 'April', 'May'),
    'summer':  ('June', 'July', 'August'),
    'fall':  ('September', 'October', 'November')
}
month = None
while True:
    month = int(input("Enter month number: "))
    if month <= 0 or month > 12:
        print("Month value error!")
    elif month == 99:
        print("Bye!")
        break
    else:
        seasons_idx = month // 3 % 4
        print(seasons_list[seasons_idx])

month_name = input("Enter month name: ")
for key, value in seasons_dict.items():
    if month_name in value:
        print(key)
        break
