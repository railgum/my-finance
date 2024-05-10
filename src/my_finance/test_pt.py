import pytest
from menu import Menu
from actions import Action

from parse import parse_from_json


db_file = 'file.json'
data = parse_from_json(db_file)


@pytest.fixture
def test_data():
    menu = Menu()
    menu.run(data)
    return data


@pytest.fixture
def test_actions(data):
    return Action(data)


@pytest.fixture
def test_menu(actions):
    return Menu()


if __name__ == '__main__':
    pytest.main(['-v'])
