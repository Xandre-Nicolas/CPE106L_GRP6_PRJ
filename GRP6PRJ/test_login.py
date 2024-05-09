import unittest
from tkinter import Tk
from unittest.mock import patch, MagicMock
from login import LoginClass

class TestLoginClass(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.login = LoginClass(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_login_success(self):
        with patch('login.messagebox.showinfo') as mock_showinfo:
            self.login.entry_username.insert(0, "test_username")
            self.login.entry_password.insert(0, "test_password")
            self.login.login()
            mock_showinfo.assert_not_called()  # Ensure showinfo is not called

    def test_login_failure(self):
        with patch('login.messagebox.showinfo') as mock_showinfo:
            self.login.entry_username.insert(0, "invalid_username")
            self.login.entry_password.insert(0, "invalid_password")
            self.login.login()
            mock_showinfo.assert_called_once_with("Error", "Invalid username or password")

if __name__ == "__main__":
    unittest.main()
