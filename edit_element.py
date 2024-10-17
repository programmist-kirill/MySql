import rename
import os
import clear_cashe
import sys

sys.path.append('7zip/')
import core_zip

class main:
    def edit_file(name_element, value_element , name_basedata):
        
        with open('system','r') as file:
            system = file.read().strip('\n')

        if system == 'Windows':
            rename.main.preparation_database_and_file_out_db_in_zip_windows(name_basedata)
        
        if system == 'Linux':
            rename.main.preparation_database_and_file_out_db_in_zip_linux(name_basedata)

        with open('directory_to_program','r') as file:
            directory_to_program = file.read().strip('\n')

        directory_to_archive = name_basedata + '.zip'
        directory_to_extract = directory_to_program + "/"
        directory_create_is_script = 'abc'

        core_zip.extract.write_no_password(directory_to_archive, directory_to_extract, directory_create_is_script)

        rename.main.preparation_and_start_script_linux()

        if os.path.exists(name_basedata + '/' + name_element):
            with open(name_basedata + '/' + name_element, 'w') as fp:
                fp.write(value_element)

            os.system('rm -rf user.zip')

            directory_to_file_or_folder = name_basedata
            what_is_name_archive = directory_to_program + "/" + name_basedata
            compression_ratio = '1'
            directory_create_is_script = 'abc'
            core_zip.archiving.write_no_password(directory_to_file_or_folder , what_is_name_archive , compression_ratio , directory_create_is_script)

            rename.main.preparation_and_start_script_linux()
            rename.main.preparation_database_and_file_out_zip_in_db_linux(name_basedata)
        else:
            print('\n\n\n----------------------------------------------------')
            print(f'Запись {name_element} не найдена в базе данных.')
            print('----------------------------------------------------')
        
        clear_cashe.main(name_basedata)