#!/usr/bin/python3
"""unittest for Base classses and methods"""


import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testBaseClass(unittest.TestCase):
    """For testing the class"""

    def testBaseWithId(self):
        """For testing a base class with an id"""
        myBase = Base(17)
        self.assertEqual(myBase.id, 17)

    def testBaseWithoutId(self):
        """For testing a base class without an id"""
        Base._Base__nb_objects = 0
        b_obj = Base()
        self.assertEqual(b_obj.id, 1)

    def testBaseWithNone(self):
        """For testing a base class without an id"""
        Base._Base__nb_objects = 0
        b_obj = Base(None)
        self.assertEqual(b_obj.id, 1)

    def testBaseIdEquality(self):
        """For testing if a base class has an unique id"""
        myBase1 = Base()
        myBase2 = Base()
        self.assertNotEqual(myBase1.id, myBase2.id)

    def testIsinstance(self):
        """Test for the class instance"""
        base_obj = Base()
        self.assertIs(type(base_obj), Base)

    def testToJsonString(self):
        list_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Doe'}]
        expected_result = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Doe"}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_result)

    def testToJsonStringEmptyList(self):
        list_dicts = []
        self.assertEqual(Base.to_json_string(list_dicts), '[]')

    def testToJsonStringNoneList(self):
        list_dicts = None
        self.assertEqual(Base.to_json_string(list_dicts), '[]')

    def testSaveToFile(self):
        class TestObj:
            def to_dictionary(self):
                return {'id': 1, 'name': 'Test'}



if __name__ == '__main__':
    unittest.main()
