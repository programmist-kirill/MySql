import rename
import os
import sys

sys.path.append('7zip/')
import core_zip


class main:
    def chech_file(name_element, name_basedata):
        with open('directory_to_program','r') as file:
            directory_to_program = file.read()

        rename.main.preparation_database_and_file_out_db_in_zip_linux(name_basedata)

        directory_to_archive = name_basedata + '.zip'
        directory_to_extract = directory_to_program
        directory_creaet_is_script = 'abc'
        core_zip.extract.write_no_password(directory_to_archive , directory_to_extract , directory_creaet_is_script)

        rename.main.preparation_and_start_script_linux()


        directory_to_check = name_basedata + "/" + name_element
        if os.path.exists(directory_to_check):
            return True
        elif not os.path.exists(directory_to_check):
            return False