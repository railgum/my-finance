import datetime
from parse import parse_to_json


categories = ['Доход', 'Расход']
description_incom = ['Зарплата', 'Инвестиции',
                     'Продажа имущества', 'Подработка', 'Подарок', 'Дотация']

description_consumption = ['Продукты', 'Дом', 'Кафе', 'Авто',
                           'Налоги', 'Транспорт', 'Хозтовары', 'Спорт']


class Action:
    def __init__(self, data):
        self.data = data

    @property
    def show_balance(self):
        if not self.data:
            return 'Нет данных'
        else:
            amount_income = 0
            amount_consumption = 0
            for item in self.data:
                # for key, value in item.items():
                #     print(item.get('Сумма'))
                if item.get('Категория') == 'Доход':
                    amount_income += item.get('Сумма')
                elif item.get('Категория') == 'Расход':
                    amount_consumption += item.get('Сумма')
                else:
                    continue
                    # if key == "Доход":
                    #     print(item.get('Сумма'))
                    #     amount_income += item.get('Сумма')
                    #     break
                    # elif key == "Расход":
                    #     print(key)
                    #     amount_consumption += item.get('Сумма')
                    #     break
                    # else:
                    #     continue

            return f'Доход - {amount_income}\nРасход - {amount_consumption}\nБаланс - {amount_income - amount_consumption}'

    @property
    def add_operation(self):
        if not self.data:
            id = 1
            self.data = []
        else:
            id = len(self.data) + 1

        print('Выберите категорию')
        for number, cat in enumerate(categories, 1):
            print(f'{number} -> {cat}')
        while True:
            try:
                category = int(input('>'))
                if category < 1 or category > 2:
                    raise ValueError
                break
            except ValueError:
                print('Некорректное значение')
        print('Введите сумму')
        while True:
            try:
                amount = int(input('>'))
                break
            except ValueError:
                print('Некорректное значение')
        print('Введите описание')
        if category == 1:
            for number, desc in enumerate(description_incom, 1):
                print(f'{number} -> {desc}')
            while True:
                try:
                    description = int(input('>'))
                    if 1 > description >= len(description_incom):
                        raise ValueError
                    break
                except ValueError:
                    print('Некорректное значение')
            self.data.append({'ID': id,
                              'Категория': 'Доход',
                              'Сумма': amount,
                              'Описание': description_incom[description-1],
                              'Дата': datetime.datetime.now().strftime('%d-%m-%Y %H:%M')})
        else:
            for number, desc in enumerate(description_consumption, 1):
                print(f'{number} -> {desc}')
            while True:
                try:
                    description = int(input('>'))
                    if 1 > description >= len(description_consumption):
                        raise ValueError
                    break
                except ValueError:
                    print('Некорректное значение')
            self.data.append({'ID': id,
                              'Категория': 'Расход',
                              'Сумма': amount,
                              'Описание': description_consumption[description-1],
                              'Дата': datetime.datetime.now().strftime('%d-%m-%Y %H:%M')})

        save_note = input(
            'Сохранить запись? 1 - да, 0 - нет\n')
        if save_note == '1':
            parse_to_json(self.data)

        return self.data
