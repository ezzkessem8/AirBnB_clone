import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertEqual(mock_stdout.getvalue(), "Documented commands (type help <topic>):\n========================================\nEOF  all  count  create  destroy  help  quit  show  update\n\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # UUID length
            self.assertIsInstance(BaseModel().id, str)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            self.console.onecmd("show BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            self.console.onecmd("destroy BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertTrue(len(f.getvalue().strip()) == 0)

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertEqual(f.getvalue().strip(), "0")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            self.console.onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            self.console.onecmd("update BaseModel 12345 name John")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            self.console.onecmd("update BaseModel 12345 name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_dict(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            self.console.onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            self.console.onecmd("update BaseModel 12345 {'name': 'John'}")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            self.console.onecmd("update BaseModel 12345 {'name': 'John', 'age': 30}")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

if __name__ == '__main__':
    unittest.main()
          
