class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_issued = False

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"


class Reader:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.books = []

    def take(self, book):
        if len(self.books) >= self.MAX_BOOKS or book.is_issued:
            return False
        book.is_issued = True
        self.books.append(book)
        return True

    def give_back(self, book):
        if book in self.books:
            book.is_issued = False
            self.books.remove(book)
            return True
        return False


b = Book("Война и мир", "Толстой", 1869)
r = Reader("Иван")
