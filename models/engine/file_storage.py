#!/usr/bin/python3
"""Serialization and Deserialization of instances"""

import json

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
        value -> obj

        Args:
            obj -> object to write
        """

        self.__objects[obj.id] = obj

    def save(self):
        """
        Serializes__objects to the JSON file
        """
        with open(self.__file_path, "w") as save_file:
            for key, value in self.__objects.items():
                json.dump({key: value.to_dict()}, save_file, indent=2)

    def reload(self):
        """
        Deserializes the JSON file to  __objects
        """
        try:
            with open(self.__file_path, "r") as load_file:
                for line in load_file:
                    d = json.load(line)
                    self.new(BaseModel(d.values()))
        except Exception:
            pass
