from menu import Menu
from parse import parse_from_json

if __name__ == '__main__':
    db_file = 'file.json'
    data = parse_from_json(db_file)
    menu = Menu()
    menu.run(data)
