import model

def input_class():
    return input('С каким классом работаем? ').upper()

def input_subject():
    return input('Какой предмет? ').lower()

def who_answer():
    return input('Кто будет отвечать? ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_child(db_dict: dict):
    for i, child in enumerate(db_dict, 1):
        print(f'{i}. {child:20} {db_dict.get(child)}')