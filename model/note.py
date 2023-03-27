from datetime import datetime as dtime, datetime


class Note(object):

    def __init__(self, note_id, title, text,date=datetime.today().strftime('%d.%m.%Y')):
        self.note_id = note_id
        self.date = date
        self.title = title
        self.text = text

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def note_id(self):
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        self._note_id = note_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    def __str__(self):
        return f'\n{self._note_id}. Дата создания(редактирования):' \
               f' {self._date}\nЗаголовок заметки: {self._title}\nТекст заметки: {self._text}\n '
