#!/usr/bin/python3
"""Serialization and Deserialization of instances"""

import json


class FileStorage:
    """
    Serialze instances to a JSON file
    Deserializing JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __object dictionary by <class name>.id"""
        return self.__objects

    def new(self, obj):
        """
        Add object to __object
        key -> <obj class name>.id
        value -> objvalue.to_dict()

        Args:
            obj -> object to write
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as save_file:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, save_file)

    def reload(self):
        """Deserializes the JSON file to  __objects"""

        from models.base_model import BaseModel

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
