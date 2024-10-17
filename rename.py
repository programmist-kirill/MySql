import os

class main:

    def preparation_database_and_file_out_db_in_zip_windows(name_basedata):
        os.system('rename + ' + name_basedata + '.db' + ' ' + name_basedata + '.zip')

    def preparation_database_and_file_out_zip_in_db_windows(name_basedata):
        os.system('rename + ' + name_basedata + '.zip' + ' ' + name_basedata + '.db')


    def preparation_database_and_file_out_db_in_zip_linux(name_basedata):
        os.system('mv ' + name_basedata + '.db' + ' ' + name_basedata + '.zip')
    
    def preparation_database_and_file_out_zip_in_db_linux(name_basedata):
        os.system('mv ' + name_basedata + '.zip' + ' ' + name_basedata + '.db')


    def preparation_and_start_script_linux():
        os.system('xterm -e python start_script.py')

    def preparation_database_and_file_out_zip_in_db_windows(name_basedata):
        os.system('rename ' + name_basedata + '.zip' + ' ' + name_basedata + '.db')
        os.system('rmdir ' + name_basedata)
        os.system('delete script.sh')
    
    def preparation_database_and_file_out_db_in_zip_windows(name_basedata):
        os.system('rename ' + name_basedata + '.db' + ' ' + name_basedata + '.zip')
        os.system('rmdir ' + name_basedata)
        os.system('delete script.sh')
    
    def preparation_database_and_file_out_zip_in_db_linux(name_basedata):
        os.system('mv ' + name_basedata + '.zip' + ' ' + name_basedata + '.db')
        os.system('rm -rf ' + name_basedata)
        os.system('rm -rf script.sh')
