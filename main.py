import sys
sys.path.append('.')
from src.files_helper import *

if __name__ == '__main__':
    files_helper = FileHelper()
    path = files_helper.show_dir_chooser()
    files_helper.loop_iterarively_dir(path)