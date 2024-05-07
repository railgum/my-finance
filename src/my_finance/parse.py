import os
import json


def parse_from_json(db_file):
    if os.path.exists(db_file):
        with open(db_file, 'r', encoding='utf-8') as db_file:
            data = json.load(db_file)
    else:
        data = {}
    return data


def parse_to_json(data):
    pass
