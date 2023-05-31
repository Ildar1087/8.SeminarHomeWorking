def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt','r', encoding='utf 8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt','a', encoding='utf 8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt','r', encoding='utf 8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    data_to_find = input('Введите данные для поиска: ')
    print(search(data,data_to_find))


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return 'Совпадений не найдено'
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('--------------------')
        print('\n'.join(result))
        new_info = input('Введите данные для уточнения: ')
        return search(result,new_info)
    return 'Совпадений не найдено'
    
# with open('book.txt','r', encoding='utf 8') as file:
#    data = file.read()
# print(data)
# data_to_find = input('введите данные для поиска: ')
# data = data.split('\n')[1::] # берём первый элемент
# print(data)  

def change() -> None:
    """Изменение или удаление данных в справочнике"""
    with open('book.txt','r',encoding='utf 8') as file:
        data = file.read().split('\n') # читаем наш файл, данные в нём
    print('\n'.join(data))
    data_to_find = input("Введите данные для поиска: ") # спрашиваем пользователя, что надо найти
    data_to_find = search(data, data_to_find) # передаём в функцию search, что мы ищем
    mode = input('Что необходимо сделать: 1. Удалить, 2. Изменить?: ') # спрашиваем, чего хочет пользователь
    if mode == 1:
        data.remove(data_to_find) # удаляем нужный элемент с помощью метода remove
    elif mode == 2:
        data[data.index(data_to_find)] = enter_contact() # производим замену через метод index, посредствам передачи нового
# значения через функцию enter_contact
    with open('book.txt','w',encoding='utf 8') as file: # после перезаписываем файл, с новым значением фио | номер телефона
        file.write('\n'.join(data))

def enter_contact() -> str: # функция записи нового контакта
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    return f'{fio} | {phone}'