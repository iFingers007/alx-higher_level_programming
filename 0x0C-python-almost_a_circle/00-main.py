#!/usr/bin/python3

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

    R1 = Rectangle(1, 2, True, 2)
    print(R1)

    R1.update(89)
    print(R1)

    R1.update(89, 2)
    print(R1)

    R1.update(89, 2, 3)
    print(R1)

    R1.update(89, 2, 3, 4)
    print(R1)

    R1.update(89, 2, 3, True, 5)
    print(R1)

    

    

