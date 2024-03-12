#!/usr/bin/python3
"""Base model for other classes"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Base class with public instance attributes and methods"""
    format_str = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """constructor method for public instance attrs"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                            BaseModel.format_str))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints string represenatation of instance"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
           with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
           __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for k, v in new_dict.items():
            if isinstance(v, datetime):
                new_dict[k] = v.strftime(BaseModel.format_str)
        return new_dict
