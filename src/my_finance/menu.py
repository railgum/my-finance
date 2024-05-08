from actions import Action
from parse import parse_from_json, parse_to_json


class Menu:

    def run(self, data=None):
        self.menu = ('Добро пожаловать в программу "Моя бухгалтерия"\n\n'
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
            answer = int(input('Введите нужный пункт меню: >'))
            if 0 < answer >= 5:
                print('Некорректный ввод')
                attempts_number -= 1
                continue
            else:
                match answer:
                    case 1:
                        print(self.notes.show_balance)
                        print(self.menu)
                    case 2:
                        print(self.notes.add_operation)
                        print(self.menu)

                    case 3:
                        pass
                    case 4:
                        pass
                    case 0:
                        exit()
