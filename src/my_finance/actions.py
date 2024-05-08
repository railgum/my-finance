import datetime


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
        amount_income = 0
        amount_consumption = 0
        for item in self.data:
            for key, value in item.items():
                print(key, value)
                if key == "Доход":
                    amount_income += item.get('Сумма')
                else:
                    amount_consumption += item.get('Сумма')

        return f'Доход - {amount_income}\nРасход - {amount_consumption}\nБаланс - {amount_income - amount_consumption}'

    @property
    def add_operation(self):
        notes = []
        print('Введите категорию')
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
                    if 0 > description >= len(description_incom):
                        raise ValueError
                    break
                except ValueError:
                    print('Некорректное значение')
            notes.append({'Категория': 'Доход',
                          'Сумма': amount,
                          'Описание': description_incom[description],
                          'Дата': datetime.datetime.now().strftime('%d-%m-%Y %H:%M')})
        else:
            for number, desc in enumerate(description_consumption, 1):
                print(f'{number} -> {desc}')
            while True:
                try:
                    description = int(input('>'))
                    if 0 > description >= len(description_consumption):
                        raise ValueError
                    break
                except ValueError:
                    print('Некорректное значение')
            notes.append({'Категория': 'Расход',
                          'Сумма': amount,
                          'Описание': description_consumption[description],
                          'Дата': datetime.datetime.now().strftime('%d-%m-%Y %H:%M')})
        return notes
