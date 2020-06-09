#!/usr/bin/python3

"""Module for Base Class"""


import json
import os
import csv


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converto to json string"""
        if list_dictionaries is None or list_dictionaries is {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """from_json_string Class
        writes an Object to a text file, using a JSON representation"""
        str = ""
        filename = cls.__name__
        if list_objs is None:
            res = []
        else:
            list_dict = []
            for i in list_objs:
                list_dict.append(i.to_dictionary())

            res = list_dict

        with open(filename + ".json", 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """convert from json string"""
        if json_string is None or json_string is "":
            data = []
        else:
            data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """create a copy of instance"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load json file"""
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
        """
        save to file CSV
        """
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        dicts = cls.to_json_string(lists)

        with open(cls.__name__ + ".csv", "w+") as my_file:
            my_file.write(dicts)

    @classmethod
    def load_from_file_csv(cls):
        """
        returns a list of instances
        """
        try:
            with open(cls.__name__ + ".csv", "r") as my_file:
                read = my_file.read()
                lists = Base.from_json_string(read)
                create = []
                for i in lists:
                    create.append(cls.create(**i))
                return create
        except IOError:
            return []
