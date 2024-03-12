#!/usr/bin/python3
"""File storage engine"""
import json
from pathlib import Path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON
    file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dicti = {}
        for k, v in FileStorage.__objects.items():
            dicti[k] = v.to_dict()
        with open(FileStorage.__file_path, mode="w") as file0:
            json.dump(dicti, file0)

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = {"BaseModel": BaseModel, "User": User,
        "Place": Place, "State": State, "City": City,
        "Amenity": Amenity, "Review": Review
        }
        file_path = Path(FileStorage.__file_path)
        if file_path.is_file():
            with open(FileStorage.__file_path, mode="r") as file1:
                FileStorage.__objects = {}
                data = json.load(file1)
                for k, v in data.items():
                    class_name = v.get("__class__")
                    if class_name in classes:
                        cls = classes[class_name]
                        FileStorage.__objects[k] = cls(**v)
