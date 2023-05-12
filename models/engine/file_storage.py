#!/usr/bin/python3

"""
The module to save files in the storage
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path


class FileStorage:
    """
    This class stores files in specified path
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        return: returns all the objects saved
        """
        return self.__objects

    def new(self, obj):
        """
        Args:
            obj: adds new object to objects
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        This method saves the objects as a json file
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        This method reloads from json format to dictionary format
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
