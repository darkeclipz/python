# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019


def initialize_dictionary_with_characters():
    return {chr(char): 0 for char in range(65, 65 + 26)}


def is_uppercase_character(char):
    return 65 <= ord(char) < 65 + 26


def filter_characters(text):
    return [char for char in text.upper() if is_uppercase_character(char)]


def count_characters(text):
    """
    Counts all the letters in a text and returns them in a dictionary.
    :param text: Text to count the letters in.
    :return: Dictionary with the letter count.
    """
    counted_characters = initialize_dictionary_with_characters()
    for char in filter_characters(text):
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
        return ''.join([line for line in file])
