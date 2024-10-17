import __init__
import rename
import clear_cashe
import new_element
import edit_element
import delete_element
import check_element
import read_element

class choise_action:
    def main():
        __init__.platform()
        __init__.directory_program()
        
        print('\n\n1 = новый элемент')
        print('2 = изменить элемент')
        print('3 = удалить запись')
        print('4 = проверить что файл существует')
        print('5 = прочитать файл')
        action = input('что вы хотите сделать - ')
        if action == '1':
            name_element = input('Введите название элемента - ')
            value_element = input('Введите значение или содержание записи - ')
            name_basedata = input('Введите название базы данных - ')
            
            new_element.main.new_file(name_element, value_element,name_basedata)
        
        elif action == '2':
            name_element = input('Введите название элемента - ')
            value_element = input('Введите новое значение или новое содержание записи - ')
            name_basedata = input('Введите название базы данных - ')
            edit_element.main.edit_file(name_element, value_element, name_basedata)
        
        elif action == '3':
            name_element = input('Введите название элемента - ')
            name_basedata = input('Введите название базы данных - ')
            delete_element.main.delete_file(name_element, name_basedata)

        elif action == '4':
            name_element = input('Введите название элемента - ')
            name_basedata = input('Введите название базы данных - ')
            a = check_element.main.chech_file(name_element,name_basedata)
            print(a)
            clear_cashe.main(name_basedata)
            rename.main.preparation_database_and_file_out_zip_in_db_linux(name_basedata)

        elif action == '5':
            name_element = input('Введите название элемента - ')
            name_basedata = input('Введите название базы данных - ')
            a = read_element.main.read_file(name_element,name_basedata)
            print(a)
            clear_cashe.main(name_basedata)
            rename.main.preparation_database_and_file_out_zip_in_db_linux(name_basedata)
            
        else:
            print('\n\n\n----------------------------------------------------')
            print('Неправильный ввод.')
            print('----------------------------------------------------')
choise_action.main()