import unittest

from program_2 import *


class TestLabrary(unittest.TestCase):

    def setUp(self):
        self.labrary =  Library()
    
    def test_add_book(self):
        self.labrary.add_book('1984')

        self.assertIn('1984', self.labrary.list_books())
    
    def test_remove_book(self):
        self.labrary.add_book('new')
        self.labrary.remove_book('new')

        self.assertNotIn('new', self.labrary.list_books())

    def test_BookNotFoundError(self):
        with self.assertRaises(BookNotFoundError):
            self.labrary.remove_book('Nex')


if __name__ == '__main__':
    unittest.main()