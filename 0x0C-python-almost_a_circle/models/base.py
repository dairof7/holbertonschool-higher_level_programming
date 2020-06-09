#!/usr/bin/python3
import json
import os
import csv

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries is {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """from_json_string Class
        writes an Object to a text file, using a JSON representation"""
        str = ""

        if list_objs is None:
            res = []
        else:
            filename = cls.__name__
            list_dict = []
            for i in list_objs:
                list_dict.append(i.to_dictionary())

            res = cls.to_json_string(list_dict)

        with open(filename + ".json", 'w', encoding='utf-8') as f:
            f.write(res)
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string is "":
            data = []
        else:
            data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__
        filename += ".json"
        listdict = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                filedata = f.read()
                fromjson = cls.from_json_string(filedata)
            for dictionary in fromjson:
                listdict.append(cls.create(**dictionary))
            return listdict
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__
        filename += ".csv"

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__
        filename += ".csv"
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                filedata = csv.read()
