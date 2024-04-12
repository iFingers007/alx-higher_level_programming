#!/usr/bin/python3

""" Module for Text_indentation function
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: . ? and :

    parameters:
    text (str) = String text

    Raises:
    TypeError: If text is not a string.
    """

    spec_chars = ['.', '?', ':']
    lines = []
    curr_line = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        curr_line += char
        if char in spec_chars:
            lines.append(curr_line.strip())
            lines.append("")
            curr_line = ""

    if curr_line:
        lines.append(curr_line.strip())
    for i, line in enumerate(lines):
        print(line, end='')
        if i < len(lines) - 1:
            print()
