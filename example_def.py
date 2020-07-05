from main import decorator

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

@decorator # применение декоратора
def people():
    '''команда, которая спросит номер документа и выведет имя человека, которому он принадлежит'''
    x = 0
    for doc in documents:
        if number_doc == doc['number']:
            doc_name = doc['name']
        else:
            x += 1
            if x == len(documents):
                doc_name = 'Номер документа введен неверно'
    print(doc_name)
    return doc_name

def shelf():
    '''команда, которая спросит номер документа и выведет номер полки, на которой он находится'''
    x = 0
    for doc in documents:
        if shelf_doc == doc['number']:
            for key, value in directories.items():
                if shelf_doc in value:
                    shelf_doc_ = key
        else:
            x += 1
            if x == len(documents):
                shelf_doc_ = 'Введен несуществующий номер документа'
    print(shelf_doc_)
    return shelf_doc_

def lists():
    '''команда, которая выведет список всех документов '''
    all_list = []
    adds = []
    for all in documents:
        list_ = (f' {all["type"]} "{all["number"]}" "{all["name"]}"')
        print(list_)
    return list_

def add():
    ''' команда, которая добавит новый документ в каталог и в перечень полок,
    спросив его номер, тип, имя владельца и номер полки,
    на котором он будет храниться.
    '''
    a = input('Введите данные ч/з запятую порядке:type, number, name ')
    b = int(input('Введите в номер директории где необходимо разместить номер '))
    if b > 3:
        print('Директории не существует. Доступные: 1, 2, 3')
        b = int(input('Введите в номер директории где необходимо разместить номер '))
    a = a.split(',')
    doc_all = {'type': a[0], 'number': a[1], 'name': a[2]}
    documents.append(doc_all)

    for num, doc in directories.items():
        if str(b) == num:
            doc.append(int(a[1]))
    print(directories)
    return directories

while True:
    numbers = input('Нажмите "p"/"s"/"l"/"a" для заупуска команды. Для завершения нажмите "q" ')
    if 'q' in numbers:
        break

    elif 'p' in numbers:
        number_doc = input('Введите номер документа для вывода имени человека ')
        people()
    elif 'l' in numbers:
        lists()

    elif 's' in numbers:
        shelf_doc = input('Введите номер документа для вывода номера полки ')
        shelf()

    elif 'a' in numbers:
        add()