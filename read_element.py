import rename
import os
import sys

sys.path.append('7zip/')
import core_zip

class main:
    def read_file(name_element,name_basedata):
        with open('directory_to_program','r') as file:
            directory_to_program = file.read()

        rename.main.preparation_database_and_file_out_db_in_zip_linux(name_basedata)

        directory_to_archive = name_basedata + '.zip'
        directory_to_extract = directory_to_program
        directory_creaet_is_script = 'abc'
        core_zip.extract.write_no_password(directory_to_archive , directory_to_extract , directory_creaet_is_script)

        rename.main.preparation_and_start_script_linux()

        if os.path.exists(name_basedata + '/' + name_element):
            with open(name_basedata + '/' + name_element, 'r') as file:
                return file.read()
        else:
            return '\n\n\n\n--------------------------------------------------\nfile not found\n--------------------------------------------------'
