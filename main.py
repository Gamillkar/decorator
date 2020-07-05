import datetime
import csv


def decorator(foo):

    def insert_foo( *args, path_way='log_file.csv',**kwargs):
        this_function_name = f'Function: {foo.__name__}'
        log_list = [datetime.datetime.utcnow(), this_function_name]
        result_foo = {f'Result function {foo.__name__}':foo(*args, **kwargs)}

        dirte_data_dict = {} # сохранение всех аргументов
        if args:
            dirte_data_dict['arg'] = args

        if kwargs:
            if 'path_way' == kwargs:
                print(kwargs)
            dirte_data_dict['kwarg'] = kwargs
        log_list.append(dirte_data_dict) #добавление аргументов
        log_list.append(result_foo) # добавление в конец лога результат функции
        print(path_way)
        with open(path_way, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(log_list)
        return log_list


    return insert_foo


