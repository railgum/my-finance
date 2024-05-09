import os
from actions import Action
from parse import parse_from_json, parse_to_json


class Menu:

    def run(self, data=None):
        self.menu = ('"Моя бухгалтерия"\n\n'
                     'Доступные действия:\n'
                     '1 - Баланс\n'
                     '2 - Добавить запись\n'
                     '3 - Редактировать запись\n'
                     '4 - Найти запись\n'
                     '0 - Выход')
        self.notes = Action(data)

        print(self.menu)
        attempts_number = 5
        while attempts_number > 0:
            answer = int(input('Введите нужный пункт меню: > '))
            if 0 < answer >= 5:
                print('Некорректный ввод')
                attempts_number -= 1
                continue
            else:
                match answer:
                    case 1:
                        os.system('cls||clear')
                        print(self.notes.show_balance)
                        print(self.menu)
                    case 2:
                        os.system('cls||clear')
                        print(self.notes.add_operation)
                        print(self.menu)

                    case 3:
                        os.system('cls||clear')
                        print(self.notes.edit_operation)
                        print(self.menu)
                    case 4:
                        os.system('cls||clear')
                        print(self.notes.find_operation)
                        print(self.menu)
                    case 0:
                        exit()
