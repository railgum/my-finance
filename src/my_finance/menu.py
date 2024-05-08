from actions import Action
from parse import parse_from_json, parse_to_json


class Menu:

    def run(self, data=None):
        menu = ('Добро пожаловать в программу "Моя бухгалтерия"\n\n'
                'Доступные действия:\n'
                '1 - Баланс\n'
                '2 - Добавить запись\n'
                '3 - Редактировать запись\n'
                '4 - Найти запись\n'
                '0 - Выход')
        print(menu)

        attempts_number = 5
        while attempts_number > 0:
            answer = int(input('Введите нужный пункт меню: >'))
            if not 0 < answer < 4:
                print('Некорректный ввод')
                attempts_number -= 1
                continue
            else:
                notes = Action(data)
                match answer:
                    case 1:
                        print(notes.show_balance)
                    case 2:
                        add_note = notes.add_operation
                        print(add_note)
                        save_note = input(
                            'Сохранить запись? 1 - да, 0 - нет\n')
                        if save_note == '1':
                            parse_to_json(add_note)
                    case 3:
                        pass
