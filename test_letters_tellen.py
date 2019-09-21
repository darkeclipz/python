# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
import unittest
from letters_tellen import count_characters, read_text_from_file
import os

class MyTestCase(unittest.TestCase):
    def test_count_characters(self):
        d = count_characters('AAA{}#%$#@$BBBbbb')
        assert d['A'] == 3, 'A should occur 3 times'
        assert d['B'] == 6, 'B should occur 6 times'

    def test_read_file(self):
        file_name = 'text.txt'
        example_text = 'Some text'
        with open(file_name, 'w') as f:
            f.write(example_text)
        text = read_text_from_file(file_name)
        os.remove(file_name)
        assert example_text in text, 'Example text should be in the text'

    def test_count_characters_in_file(self):
        file_name = 'text.txt'
        example_text = 'AAABBBbbb'
        with open(file_name, 'w') as f:
            f.write(example_text)
        text = read_text_from_file(file_name)
        os.remove(file_name)
        d = count_characters(text)
        assert d['A'] == 3, 'A should occur 3 times'
        assert d['B'] == 6, 'B should occur 6 times'

    def test_read_file_validate_txt(self):
        try:
            read_text_from_file('file.dll')
            assert False, 'Exception not raised'
        except ValueError:
            pass


if __name__ == '__main__':
    unittest.main()
