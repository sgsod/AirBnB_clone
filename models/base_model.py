#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

"""defines BaseModel - for the whole projei"""


class BaseModel:
    """Defines all common attributes/methods of other classes

    Attributes:
        id: Universal Unique Identifier
        created_at: time object is created
        updated_at: time the object was modified

    Method:
        __str__: prints the class name, id and __dict__
        save(self): updates updated at to current time when called
        to_dict(self): returns a dictionary containing all
        keys/values of __dict__ of the instance

    """

    def __init__(self, *args, **kwargs):
        """
        Public instance initialization
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        Print string representation of BaseModel
        """
        
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Return dictionary with all keys/values of __dict__
        key "__class__" is added
        created_at and updated_at are converted with "isofformat()"
        """
        self.dict_obj = self.__dict__.copy()
        self.dict_obj["created_at"] = self.created_at.isoformat()
        self.dict_obj["updated_at"] = self.updated_at.isoformat()
        self.dict_obj["__class__"] = self.__class__.__name__
        return self.dict_obj
