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
        """
        Return __object dictionary by <class name>.id
        """
        return self.__objects

    def new(self, obj):
        """
        Add object to __object
        key -> <obj class name>.id
        value -> obj

        Args:
            obj -> object to write
        """

        self.__objects[obj.__class__ + '.' + obj.id] = obj

    def save(self):
        """
        Serializes__objects to the JSON file
        """
        with open(self.__file_path, 'w+') as save_file:
            json.dump({key: value.to_dict() \
                    for key, value in self.__objects.items()}, save_file)

    def reload(self):
        """
        Deserializes the JSON file to  __objects
        """
        try:
        with open(self.__file_path, 'r') as load_file:
            dict = json.loads(load.read())
            for value in dict.values():
                className = value["__class__"]
                self.new(eval(className)(**value))
        except Exception:
            pass
