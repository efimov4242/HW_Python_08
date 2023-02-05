db_dict = {}
subject = ''
path = ''

def set_class(class_path: str):
    global path
    path = class_path + '.txt'

def set_subject(our_subject: str):
    global subject
    subject = our_subject

def read_db():
    with open(path, 'r', encoding='UTF-8') as file:
        db_list = file.readlines()
        for line in db_list:
            if line.split(';')[0] == subject:
                for student in line.split(';')[1].strip().split(','):
                    db_dict[student.split(':')[0]] = list(map(int, student.split(':')[1].split()))

def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for line in file:
        if line.split(';')[0] != subject:
            new_file.append(line.strip())
    item = []
    for student, marks in db_dict.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def student_mark(student: str, mark: int):
    marks = db_dict.get(student)
    marks.append(mark)
    db_dict[student] = marks


def get_db_dict():
    return db_dict
            