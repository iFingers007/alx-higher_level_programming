#!/usr/bin/python3
import string
__import__('os').write(1, bytes([*map(ord, string.ascii_uppercase), 10]))
