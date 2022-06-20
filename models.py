import json


class Library:
    def __init__(self):
        try:
            with open("books.json", "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def all(self):
        for book in self.books:
            if book['read'] == False:
                book['read'] = "Nie"
            if book['read'] == True:
                book['read'] = "Tak"

        self.books = sorted(self.books, key=lambda k:k['read'])

        return self.books

    def get(self, id):
        return self.books[id]


    def create(self, data):
        self.books.append(data)
        self.save_all()

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.books[id] = data
        self.save_all()

    def delete(self, id):
        book = self.get(id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False

    def update(self, id, data):
        book = self.get(id)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False


books = Library()

