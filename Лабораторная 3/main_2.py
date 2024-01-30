class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    def __str__(self):
        return f"{self.name} by {self.author}"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Pages must be an integer.")
        if value <= 0:
            raise ValueError("Pages must be a positive integer.")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Duration must be a number.")
        if value <= 0:
            raise ValueError("Duration must be a positive number.")
        self._duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == '__main__':
    # Создание объекта класса Book
    book = Book(name="The Great Gatsby", author="F. Scott Fitzgerald")
    print(book)
    print(repr(book))

    # Создание объекта класса PaperBook
    paper_book = PaperBook(name="To Kill a Mockingbird", author="Harper Lee", pages=281)
    print(paper_book)
    print(repr(paper_book))

    # Изменение количества страниц бумажной книги
    paper_book.pages = 320
    print(paper_book)
    print(repr(paper_book))

    # Создание объекта класса AudioBook
    audio_book = AudioBook(name="1984", author="George Orwell", duration=8.5)
    print(audio_book)
    print(repr(audio_book))

    # Изменение продолжительности аудиокниги
    audio_book.duration = 10.2
    print(audio_book)
    print(repr(audio_book))
