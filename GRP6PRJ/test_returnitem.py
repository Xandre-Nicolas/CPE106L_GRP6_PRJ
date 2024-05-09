import unittest
from tkinter import Tk
from unittest.mock import Mock, patch
import sys
sys.path.append('C:/Users/markj/Desktop/GRP6PRJ')  # Adjust the path as per your project structure
from returnitem import ReturnItemClass

class TestReturnItemClass(unittest.TestCase):
    def setUp(self):
        self.mock_root = Tk()
        self.return_item_class = ReturnItemClass(self.mock_root)

    def test_get_data(self):
        # Test implementation...

        def test_show_message(self):
            pass  # Placeholder for the test_show_message method

    def test_returnitem(self):
        # Test implementation...

        @patch('returnitem.sqlite3.connect')
        def test_show(self, mock_connect):
        # Mock database connection and cursor
            mock_cursor = mock_connect.return_value.cursor.return_value
            mock_cursor.fetchall.return_value = [("1", "Type1", "Brand1", "Color1", "Model1", "Material1", "Description1", "LastSeen1", "DateLost1")]

        # Call the method under test (show method)
            self.return_item_class.show()

        # Check if the Treeview is populated with the correct data
            expected_values = mock_cursor.fetchall.return_value[0]
            actual_values = self.return_item_class.ItemTable.item(self.return_item_class.ItemTable.focus())["values"]
            self.assertEqual(actual_values, expected_values)

if __name__ == '__main__':
    unittest.main()
