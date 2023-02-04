import unittest
import os.path

from src.files_helper import FileHelper


class TestFileDialog(unittest.TestCase):
    resource_path = os.path.join(os.path.split(__file__)[0], "resource")

    def test_dialog_closed(self):
        file_name = ''
        file_helper = FileHelper();
        file_name_not_selected = file_helper.show_dir_chooser()
        self.assertEqual(file_name, file_name_not_selected)

    def test_dialog_select_dir(self):
        file_name = ''
        file_helper = FileHelper()
        file_name_selected = file_helper.show_dir_chooser()
        self.assertNotEqual(file_name, file_name_selected)

    def test_correct_extension(self):
        file_name = os.path.join(self.resource_path, 'test_extension.txt')
        file_helper = FileHelper()
        is_file_text = file_helper._FileHelper__is_text_file(file_name)
        self.assertEqual(is_file_text, True)

    def test_incorrect_extension(self):
        file_name = os.path.join(self.resource_path, 'test_incorrect_extension.csv')
        file_helper = FileHelper()
        is_file_text = file_helper._FileHelper__is_text_file(file_name)
        self.assertNotEqual(is_file_text, True)


if __name__ == '__main__':
    unittest.main()
