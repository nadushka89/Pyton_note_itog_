class View(object):
    @staticmethod
    def main_menu():
        """         Главное меню:

                    1. Добавление заметки
                    2. Поиск заметки
                    3. Изменение заметки
                    4. Удаление заметки
                    5. Удаление всех заметок
                    6. Отображение всех заметок
                    0. Выход
                     """

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            f"""------------------------------------------------------------
            {print(note)}
            ------------------------------------------------------------"""
    @staticmethod
    def show_note(note):
        f"""------------------------------------------------------------
            {print(note)}
            ------------------------------------------------------------"""

    @staticmethod
    def show_empty_list_message():
        f"""------------------------------------------------------------
            Список заметок пустой.
            ------------------------------------------------------------"""

    @staticmethod
    def display_note_id_not_exist(note_id):
        f"""------------------------------------------------------------
            {print('Заметка с id: {} не найдена!'.format(note_id))}
            ------------------------------------------------------------"""
    @staticmethod
    def display_note_date_not_exist(date):
        f"""------------------------------------------------------------
            {print('Заметка с такой датой {} не найдена!'.format(date))}
            ------------------------------------------------------------"""

    @staticmethod
    def display_note_id_exist(note_id):
        f"""------------------------------------------------------------
            {print('Заметка с id: {} уже есть!'.format(note_id))}
            ------------------------------------------------------------"""

    @staticmethod
    def display_note_stored():
        f"""------------------------------------------------------------
            Заметка успешно добавлена.
            ------------------------------------------------------------"""

    @staticmethod
    def display_note_updated(note_id):
        f"""------------------------------------------------------------
            {print('Заметка с id:{} обновлена.'.format(note_id))}
            ------------------------------------------------------------"""

    @staticmethod
    def display_note_deletion(note_id):
        f"""------------------------------------------------------------
            {print('Заметка с id: {} удалена.'.format(note_id))}
            ------------------------------------------------------------"""

    @staticmethod
    def display_all_notes_deletion():
        f"""------------------------------------------------------------
            Все заметки успешно удалены.
            ------------------------------------------------------------"""

