import datetime
from pprint import pprint

from parse import parse_to_json


categories = ['Доход', 'Расход']
description_incom = ['Зарплата', 'Инвестиции',
                     'Продажа имущества', 'Подработка', 'Подарок', 'Дотация']

description_consumption = ['Продукты', 'Дом', 'Кафе', 'Авто',
                           'Налоги', 'Транспорт', 'Хозтовары', 'Спорт']


def save_note(data):
    """Метод сохранения изменений в JSON-файл"""

    answer = input('Сохранить запись? 1 - да, 0 - нет\n')
    if answer == '1':
        parse_to_json(data)  # Внешняя функция записи в JSON


class Action:
    """Класс для осуществления различных действий с содержимым JSON-файла

    Атрибуты
    ---------
    data : list
        список словарей из JSON-файла

    Методы-свойства
    --------
    show_balance()
        проходит по списку словарей и выводит сумму расходов и доходов

    add_operation()
        добавление операции

    edit_operation()
        редактирование записи

    find_operation()
        поиск записей по различным критериям

    """

    def __init__(self, data):
        self.data = data

    @property
    def show_balance(self):
        """Свойство, показывающее текущее состояние счета

        Если файл отсутствует, возвращает сообщение
        """

        if not self.data:
            return 'Нет данных'
        else:
            amount_income = 0
            amount_consumption = 0
            for item in self.data:
                if item.get('Категория') == 'Доход':
                    amount_income += item.get('Сумма')
                elif item.get('Категория') == 'Расход':
                    amount_consumption += item.get('Сумма')
                else:
                    continue
        return f'Доход - {amount_income}\nРасход - {amount_consumption}\nБаланс - {amount_income - amount_consumption}'

    @property
    def add_operation(self):
        """Свойство добавления операции

        Предлагает выбирать из предложенных списков действий.
        При неверном выборе вызывается исключение.

        При окончании ввода операции предлагает сохранение записи
        """

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
                              'Дата': datetime.datetime.now().strftime('%d-%m-%Y')})
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
                              'Дата': datetime.datetime.now().strftime('%d-%m-%Y')})

        save_note(self.data)
        return 'Запись добавлена'

    @property
    def edit_operation(self):
        """Свойство редактирования записи

        Редактируемая запись определяется по её ID
        """

        edit_note = input('Введите ID записи для редактирования\n')
        while True:
            for item in self.data:
                if item.get('ID') == int(edit_note):
                    print('Выберите поле для редактирования\n')
                    print('1 - Категория\n'
                          '2 - Сумма\n'
                          '3 - Описание\n'
                          '4 - Дата\n'
                          '0 - Выход\n')
                    while True:
                        try:
                            field = int(input('>'))
                            if field < 0 or field > 4:
                                raise ValueError
                            break
                        except ValueError:
                            print('Некорректное значение')
                    if field == 1:
                        print('Выберите категорию')
                        print('Прежнее значение: ', item.get('Категория'))
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
                        item['Категория'] = categories[category-1]
                    elif field == 2:
                        print('Введите сумму')
                        print('Прежнее значение: ', item.get('Сумма'))
                        while True:
                            try:
                                amount = int(input('>'))
                                break
                            except ValueError:
                                print('Некорректное значение')
                        item['Сумма'] = amount
                    elif field == 3:
                        print('Выберите описание')
                        print('Прежнее значение: ', item.get('Описание'))
                        if item.get('Категория') == 'Доход':
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
                            item['Описание'] = description_incom[description-1]
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
                            item['Описание'] = description_consumption[description-1]
                    elif field == 4:
                        print('Введите дату')
                        print('Прежнее значение: ', item.get('Дата'))
                        item['Дата'] = input('>')
                    elif field == 0:
                        save_note(self.data)
                        return 'Запись отредактирована'

    @property
    def find_operation(self):
        """Свойство поиска записи по различным критериям"""

        while True:
            print('Введите номер поля для поиска')
            print('1 - Категория\n'
                  '2 - Сумма\n'
                  '3 - Описание\n'
                  '4 - Дата\n'
                  '0 - Выход\n')
            while True:
                try:
                    field = int(input('>'))
                    if field < 0 or field > 4:
                        raise ValueError
                    break
                except ValueError:
                    print('Некорректное значение')
            if field == 1:
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
                for item in self.data:
                    if item.get('Категория') == categories[category-1]:
                        pprint(item)
            elif field == 2:
                print('Введите сумму')
                while True:
                    try:
                        amount = int(input('>'))
                        break
                    except ValueError:
                        print('Некорректное значение')
                for item in self.data:
                    if item.get('Сумма') == amount:
                        pprint(item)
            elif field == 3:
                print('Выберите описание')
                if item.get('Категория') == 'Доход':
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
                    for item in self.data:
                        if item.get('Описание') == description_incom[description-1]:
                            pprint(item)
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
                    for item in self.data:
                        if item.get('Описание') == description_consumption[description-1]:
                            pprint(item)
            elif field == 4:
                print('Введите дату')
                while True:
                    try:
                        date = input('>')
                        break
                    except ValueError:
                        print('Некорректное значение')
                for item in self.data:
                    if item.get('Дата') == date:
                        pprint(item)
            elif field == 0:
                return 'Поиск завершен'
