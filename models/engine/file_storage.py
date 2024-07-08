#!/usr/bin/python3
"""Serialization and Deserialization of instances"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serialze instances to a JSON file
    Deserializing JSON file to instances
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Return __object dictionary by <class name>.id
        """
        return self.__objects

    def new(self, obj):
        """
        Add object to __object
        key -> <obj class name>.id
        value -> objvalue.to_dict()

        Args:
            obj -> object to write
        """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes__objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as save_file:
            json.dump({key: value.to_dict() \
                for key, value in self.__objects.items()}, save_file)

    def reload(self):
        """
        Deserializes the JSON file to  __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as load_file:
                d = json.load(load_file)
                for value in d.values():
                    """
                    Alternative method:
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
                    """
                    m = BaseModel(**value)
                    self.new(m)

        except Exception:
            pass
