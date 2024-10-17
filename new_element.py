import os
import shutil
import rename
import sys
import clear_cashe
import create_database

sys.path.append('7zip/')
import core_zip

class main:
    def rewriting_elements_in_database(name_element,value_element,name_basedata):
        with open('directory_to_program','r') as file:
            directory_to_program = file.read().strip('\n')

        def clear(name_basedata, directory_to_program):
            path = directory_to_program + 'cashe'
            if os.listdir(path):
                shutil.rmtree(path)
                os.makedirs(path + '/' + name_basedata)
            else:
                os.makedirs(path + '/' + name_basedata)
        clear(name_basedata,directory_to_program)

        if os.path.exists('system'):

            with open('cashe/' + name_basedata + '/' + name_element , 'w') as fp:
                fp.write(value_element)
            
            rename.main.preparation_database_and_file_out_db_in_zip_linux(name_basedata)

            directory_to_archive = name_basedata + '.zip'
            directory_to_extract = directory_to_program + '/cashe/'
            directory_create_is_script = 'abc'
            core_zip.extract.write_no_password(directory_to_archive , directory_to_extract , directory_create_is_script)

            rename.main.preparation_and_start_script_linux()

            directory_to_archive = name_basedata + '.zip'
            directory_to_file_or_folder = directory_to_extract + name_basedata
            compression_ratio = '1'
            directory_create_is_script = 'abc'
            core_zip.archiving.write_no_password(directory_to_archive , directory_to_file_or_folder , compression_ratio , directory_create_is_script)

            rename.main.preparation_and_start_script_linux()
            rename.main.preparation_database_and_file_out_zip_in_db_linux(name_basedata)
            print('2 rename')

            clear_cashe.main(name_basedata)

            sys.exit()

    def new_file(name_element, value_element, name_basedata):

        with open('system','r') as file:
            system = file.read().strip('\n')

        if os.path.exists(name_basedata + '.db'):
            main.rewriting_elements_in_database(name_element , value_element , name_basedata)
        else:
            create_database.main(name_basedata)

        with open(name_basedata + "/" + name_element, 'w') as fp:
            fp.write(value_element)

        #архивация базы данных с элементом
        core_zip.archiving.write_no_password(name_basedata + '.zip' , name_basedata + "/" + name_element , '1', 'abc')
        rename.main.preparation_and_start_script_linux()

        if system == 'Windows':
            rename.main.preparation_database_and_file_out_zip_in_db_windows(name_basedata)
        
        elif system == 'Linux':
            rename.main.preparation_database_and_file_out_zip_in_db_linux(name_basedata)

        clear_cashe.main(name_basedata)
