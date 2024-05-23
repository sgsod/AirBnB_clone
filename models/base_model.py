#!/usr/bin/python3
import uuid
from datetime import datetime

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

    def __init__(self):
        """Public instance initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return dictionary with all keys/values of __dict__
        key "__class__" is added
        created_at and updated_at are converted with "isofformat()"
        """
        dict_obj = self.__dict__
        dict_obj["created_at"] = created_at.isoformat()
        dict_obj["updated_at"] = updated_at.isoformat()
        dict_obj["__class__"] = self.__class__.__name__
