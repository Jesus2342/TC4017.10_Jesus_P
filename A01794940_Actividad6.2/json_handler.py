""" Handling json files """
import json
import os


def load_json(filename):
    """ Handling missing files"""
    if not os.path.exists(filename):
        return {}
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)


def save_json(filename, data):
    """ Save json file"""
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)
