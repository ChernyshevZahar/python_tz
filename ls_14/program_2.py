class BookNotFoundError(Exception):
    def __init__(self):
        super().__init__("Книга не найдена в библиотеке.")


class Library:

    def __init__(self):
        self.labrary = set()

    def add_book(self,title):
        self.labrary.add(title)
    def remove_book(self,title):
        if title not in  self.labrary:
            raise BookNotFoundError
        self.labrary.remove(title)
    def list_books(self):
        return list(self.labrary)