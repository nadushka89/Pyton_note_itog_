import datetime
from controller.controller import Controller
from model.modelJSON import ModelJSON
from model.note import Note
from view.view import View

def run():
    c = Controller(ModelJSON("./data/notes.json"), View)
    while True:

        main_menu: str = """
                    Главное меню:
                    1. Добавление заметки
                    2. Поиск заметки по ID
                    3. Изменение заметки
                    4. Удаление заметки
                    5. Удаление всех заметок
                    6. Отображение всех заметок
                    7. Поиск заметки по дате
                    0. Выход
                     """
        print (main_menu)
        command = input('Выберите необходимый пункт меню: ')
        if command == '0':
            break
        if command == '1':
            print('\nДобавление заметки:')
            c.create_note(get_note_data())
        elif command == '2':
            print('\nПоиск заметки:')
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif command == '7':
            print('\nПоиск заметки:')
            if c.notes_exist():
                c.show_note_date(get_notes_data())
        elif command == '3':
            if c.notes_exist():
                print('\nИзменение заметки:')
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())
        elif command == '4':
            if c.notes_exist():
                print('\nУдаление заметки:')
                delete_id = int(get_number())
            if c.note_id_exist(delete_id):
                c.delete_note(delete_id)
        elif command == '5':
            if c.notes_exist():
                print('\nУдаление всех заметок:')
                if input('Вы действительно хотите удалить все заметки? (Y/N): ').capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif command == '6':
            if c.notes_exist():
                print('\nОтображение всех заметок:')
                c.show_notes()
        else:
            print('Команда не найдена')


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок: ')
    text = input('Введите текст заметки: ')
    return Note(note_id, title, text, date)

def get_notes_data():
    while True:
        get_choice = input('Введите дату заметки: ')
        if get_choice.format("00-00-0000"):
            return get_choice
        else:
            print('Введите корректную дату')

def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print('Введите целое положительное число!')





