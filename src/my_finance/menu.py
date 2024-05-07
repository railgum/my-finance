import os
import json


class Menu():
    db_file = 'file.json'

    menu = ('Добро пожаловать в программу "Моя бухгалтерия"\n\n'
            'Доступные действия:\n'
            '1 - Баланс\n'
            '2 - Добавить запись\n'
            '3 - Редактировать запись\n'
            '4 - Найти запись\n'
            '0 - Выход')
    print(menu)

    if os.path.exists(db_file):
        with open(db_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = {}
