
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
        }

# поиск человека по имени документа
def ducoment_name():
    print('Введите номер документа: ')
    number_document = input()
    for document in documents:
        if document ['number'] == number_document:
            print(document)
            break
    else:
        print('Такого номера документа нет в базе')
    return

# выводит список документов
def document_list():
    for document in documents:
        print(document)
    return

# возвращает на какой полке лежит конкретный документ
def document_shelf():
    number = input ('Введите номер документа\n>> ')
    check_flag = False
    for shelf in directories.keys():
        if number in directories[shelf]:
            print ('Документ лежит на полке номер %s' %(shelf))
            check_flag = True
    if check_flag == False:
        print ('Неверный номер документа')

# добавляем новый документ
def document_new():
    new_documents = []
    new_number_document = input('Введите номер документа: ')
    new_type_document = input('Введите тип документа: ')
    new_name_document = input('Введите ФИО: ')
    shelf_directories = input('Введите номер полки для документа: ')
    documents.append({'type': new_type_document, 'number': new_number_document, 'name': new_name_document})

    if shelf_directories not in directories:
        directories[shelf_directories] = []
    directories[shelf_directories].append(new_number_document)

    print('Данные успешно добавлены!')
    return document_new


def menu():
    while True:
        print('Введите данные, которые Вам необходимо найти')
        print('''
        p - поиск по номеру документа
        l - список всех документов
        s - номер полки для конкретного документа
        a - добавить новый документ
        e - выход''')
        input_menu = input()
        if input_menu == 'p':
            ducoment_name()
        elif input_menu == 'l':
            document_list()
        elif input_menu == 's':
            document_shelf()
        elif input_menu == 'a':
            document_new()
        elif input_menu == 'e':
            break
        else:
            print('Введите правильную команду.')

menu()
