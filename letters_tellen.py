# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019


def initialize_dictionary_with_characters():
    # A is positioned at 65 in the ASCII table, i.e. ord(A) = 65.
    return {chr(char): 0 for char in range(65, 65 + 26)}


def is_uppercase_character(char):
    return 65 <= ord(char) < 65 + 26


def next_uppercase_character(text):
    for char in text:
        if is_uppercase_character(char):
            yield char


def count_characters(text):
    """
    Counts all the letters in a text and returns them in a dictionary.
    :param text: Text to count the letters in.
    :return: Dictionary with the letter count.
    """
    counted_characters = initialize_dictionary_with_characters()
    for char in next_uppercase_character(text.upper()):
        counted_characters[char] += 1
    return counted_characters


def read_text_from_file(file_path):
    """
    Reads all the text from a text file, and returns this as a single
    string.
    :param file_path: The path to the file.
    :return: All the text in the file as a string.
    """
    with open(file_path) as file:
        # Read all the lines from the file, and concatenate them.
        return ''.join([line for line in file])
