from balance import ShowBalance
from parse import parse_from_json, parse_to_json


class Menu():
    db_file = 'file.json'
    data = parse_from_json(db_file=None)
    attempts_number = 5

    menu = ('Добро пожаловать в программу "Моя бухгалтерия"\n\n'
            'Доступные действия:\n'
            '1 - Баланс\n'
            '2 - Добавить запись\n'
            '3 - Редактировать запись\n'
            '4 - Найти запись\n'
            '0 - Выход')
    print(menu)

    while attempts_number > 0:
        answer = input('Введите нужный пункт меню')
        if (not answer.isdigit) or (0 < answer < 4):
            print('Некорректный ввод')
            attempts_number -= 1
            continue
        else:
            match answer:
                case 1:
                    balance = ShowBalance(data)
                    print(balance.show_amount)
