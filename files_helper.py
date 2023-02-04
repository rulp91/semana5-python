import os
import mimetypes
from tkinter import *
from tkinter import filedialog


class FileHelper:

    def show_dir_chooser(self):
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        return folder_selected

    def loop_iterarively_dir(self, dir_path):
        for nombre_directorio, dirs, ficheros in os.walk(dir_path, topdown=False):
            # print(nombre_directorio)
            for nombre_fichero in ficheros:
                if self.__is_text_file(os.path.join(nombre_directorio, nombre_fichero)):
                    self.__process_text_file(nombre_directorio, nombre_fichero)

    def __process_text_file(self, path, filename):
        file = open(os.path.join(path, filename), 'r')
        Lines = file.readlines()
        dir_is_printed = False
        # Strips the newline character
        for line in Lines:
            if line.find("wax synthase") != -1:
                if not dir_is_printed:
                    print(path.replace("\\", "/"))
                    dir_is_printed = True
                print("\t" + line, end='')

    def __is_text_file(self, file):
        mime_type = mimetypes.guess_type(file)
        return "text/plain" == mime_type[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    files_helper = FileHelper()
    files_helper.show_dir_chooser()
