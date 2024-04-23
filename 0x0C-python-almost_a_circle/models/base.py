#!/usr/bin/python3
"""Module for the Class Base


"""


import json
import csv

class Base:
    """Base class of the project

    Represents the Base class

    Attributes:
    __nb_objects(int) : The number of instance of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of the Base class

        Args:
        id (int): Identity

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON representation of a dictionary

        Args:
        list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes srtings representation to a file

        Args:
        list_objs (list): list of objects
        """
        if list_objs is None:
            list_objs = []
        fileName = cls.__name__ + ".json"
        dictList = []
        for obj in list_objs:
            dictList.append(obj.to_dictionary())
        with open(fileName, "w") as fileWrite:
            fileWrite.write(cls.to_json_string(dictList))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation

        Args:
        json_string (str): Json string

        Returns:
        json string or empty list
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
        dictionary (dict): key/value pair of class

        Returns:
        Instance of key/value
        """
        if cls.__name__ == "Rectangle":
            dummyInstance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummyInstance = cls(1)
        else:
            raise ValueError("Type not supported")
        dummyInstance.update(**dictionary)
        return dummyInstance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances

        Returns:
        list of instance
        """
        fileName = cls.__name__ + ".json"
        try:
            with open(fileName, "r") as fileRead:
                json_string = fileRead.read()
        except FileNotFoundError:
            return []
        dictList = cls.from_json_string(json_string)
        instList = []
        for diction in dictList:
            instList.append(cls.create(**diction))

        return instList

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to a csv file"""
        if list_objs is None:
            list_objs = []
        fileName = f"{cls.__name__}.csv"
        dictList = []
#s        for obj in list_objs:
#            dictList.append(obj.to_dictionary())
        with open(fileName, "w", newline='') as fileCsv:
            outputWriter = csv.writer(fileCsv)
            outputWriter.writerow(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialises a csv file"""
        csvRows = []
        fileName = f"{cls.__name__}.csv"
        with open(fileName) as readCsv:
            fileRead = csv.reader(readCsv)
            for row in fileRead:
                csvRows.append(row)
        return csvRows
