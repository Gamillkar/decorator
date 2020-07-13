import datetime
import csv

def log_path(path):
    def decorator(foo):
        def insert_foo( *args,**kwargs):
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
            print(path)
            with open(path, 'w', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(log_list)
            return log_list
        return insert_foo
    return decorator



@log_path('data/log_filesss.csv')
def log_file(*args, **kwargs):

    result = ''.join(args * 2), kwargs
    return result



log_file('4333',el='values kwarg')
