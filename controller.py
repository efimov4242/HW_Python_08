import view
import model

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.read_db()
    student = ''
    while True:
        db_dict = model.get_db_dict()
        view.list_of_child(db_dict)
        student = view.who_answer()
        if student == 'exit':
            break
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()