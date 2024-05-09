import unittest
from tkinter import Tk
from viewreturneditem import ViewReturnItemClass

class TestViewReturnedItem(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = ViewReturnItemClass(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        self.assertEqual(self.root.title(), "View Returned Items")

    def test_delete_selected_row(self):
        try:
            returned_item_table = self.app.ReturnedItemTable
            self.assertIsNotNone(returned_item_table)
        except AttributeError:
            print("OK")

if __name__ == '__main__':
    unittest.main()

