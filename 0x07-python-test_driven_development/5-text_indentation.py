#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be formatted

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in punctuation:
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

    print(result.strip(), end="")
