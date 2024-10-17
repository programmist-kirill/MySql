import rename
import os
import sys
import clear_cashe

sys.path.append('7zip/')
import core_zip

class main:
    def delete_file(name_element , name_basedata):
        
        with open('directory_to_program','r') as file:
            directory_to_program = file.read().strip('\n')

        rename.main.preparation_database_and_file_out_db_in_zip_linux(name_basedata)
        print('\n\n\n\nrename.edit.file')

        directory_to_archive = name_basedata + '.zip'
        directory_to_extract = directory_to_program
        directory_create_is_script = 'abc'
        core_zip.extract.write_no_password(directory_to_archive , directory_to_extract , directory_create_is_script)
        print('core_zip.extract')

        rename.main.preparation_and_start_script_linux()


        directory_for_delete = name_basedata + '/' + name_element
        os.remove(directory_for_delete)
        print('os.remove')

        os.remove(name_basedata + '.zip')

        what_is_name_archive = name_basedata + '.zip'
        directory_to_file_or_folder = name_basedata + '/'
        compression_ratio = '1'
        directory_create_is_script = 'abc'
        core_zip.archiving.write_no_password(what_is_name_archive , directory_to_file_or_folder , compression_ratio , directory_create_is_script)
        print('core_zip.archiving')

        rename.main.preparation_and_start_script_linux()
        rename.main.preparation_database_and_file_out_zip_in_db_linux(name_basedata)

        clear_cashe.main(name_basedata)