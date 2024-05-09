import unittest
import sqlite3
from tkinter import Tk
from lostitems import LostItemClass

class TestLostItemClass(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = LostItemClass(self.root)

    def tearDown(self):
        self.root.destroy()

    def count_items_in_database(self):
        con = sqlite3.connect(database="GRP6PRJ.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM lost_items")
        count = cur.fetchone()[0]
        cur.close()
        con.close()
        return count

    def test_initialization(self):
        self.assertEqual(self.root.title(), "Lost Item Tracker")

    def test_add_item(self):
        initial_item_count = self.count_items_in_database()

        self.app.var_TypeofItem.set("Electronics")
        self.app.var_BrandofItem.set("Sony")
        self.app.var_ColorofItem.set("Black")
        self.app.var_ModelofItem.set("ABC123")
        self.app.var_MaterialofItem.set("Plastic")
        self.app.var_OtherDescription.set("Test item")
        self.app.var_LastSeen.set("Home")
        self.app.var_DateLost.set("2024-05-10")
        self.app.add()

        final_item_count = self.count_items_in_database()
        self.assertEqual(final_item_count, initial_item_count + 1)

    def test_update_item(self):
        

     def test_delete_item(self):
        initial_item_count = self.count_items_in_database()

        final_item_count = self.count_items_in_database()
        self.assertEqual(final_item_count, initial_item_count - 1)

if __name__ == '__main__':
    unittest.main()
