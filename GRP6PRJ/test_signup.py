import unittest
from tkinter import Tk
from unittest.mock import patch
from signup import SignupClass

class TestSignupClass(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.signup = SignupClass(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('signup.messagebox.showinfo')
    @patch('signup.messagebox.showerror')
    @patch('signup.Tk.destroy')
    @patch('signup.Tk.focus_force')
    @patch('signup.Tk.mainloop')
    def test_signup_success(self, mock_mainloop, mock_focus_force, mock_destroy, mock_showerror, mock_showinfo):
   
        self.signup.entry_nameID.insert(0, "Test Name")
        self.signup.entry_username.insert(0, "test_username")
        self.signup.entry_password.insert(0, "test_password")
        self.signup.entry_email.insert(0, "test@example.com")
        self.signup.entry_contact.insert(0, "12345678901")  
        self.signup.signup()

        mock_showinfo.assert_called_once_with("Success", "User registered successfully!")
        mock_destroy.assert_called_once()

    @patch('signup.messagebox.showinfo')
    @patch('signup.messagebox.showerror')
    def test_signup_failure(self, mock_showerror, mock_showinfo):

        self.signup.signup()

        mock_showerror.assert_called_once_with("Error", "All fields are required!")

if __name__ == "__main__":
    unittest.main()
