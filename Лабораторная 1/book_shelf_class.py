from book_class import Book


class BookShelf:
    def __init__(self, books: list):
        """
        Инициализация экземпляра класса "BookShelf".

        :param books: Список книг на полке (может быть пустым)

        >>> shelf = BookShelf([])
        >>> str(shelf)
        'BookShelf: '
        >>> book1 = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book2 = Book("Л. Н. Толстой", "Война и мир", 1225, 8.5)
        >>> shelf = BookShelf([book1, book2])
        >>> str(shelf)
        'BookShelf: Книга: "Капитанская дочка" (Автор: А. С. Пушкин, Страницы: 320, Рейтинг: 9) Книга: "Война и мир" (Автор: Л. Н. Толстой, Страницы: 1225, Рейтинг: 8.5)'
        """
        for book in books:
            if not isinstance(book, Book):
                raise TypeError("All elements in the 'books' list must be instances of the 'Book' class.")
        self.__books = books

    def add_book(self, book: Book):
        """
        Добавляет книгу на полку.

        :param book: Экземпляр класса Book

        >>> shelf = BookShelf([])
        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> shelf.add_book(book)
        >>> str(shelf)
        'BookShelf: Книга: "Капитанская дочка" (Автор: А. С. Пушкин, Страницы: 320, Рейтинг: 9)'
        """
        if not isinstance(book, Book):
            raise TypeError("The 'book' parameter must be an instance of the 'Book' class.")
        self.__books.append(book)

    def remove_book_by_title(self, title: str):
        """
        Удаляет книгу с полки по её названию.

        :param title: Название книги (строка)

        >>> shelf = BookShelf([])
        >>> book1 = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book2 = Book("Л. Н. Толстой", "Война и мир", 1225, 8.5)
        >>> shelf.add_book(book1)
        >>> shelf.add_book(book2)
        >>> shelf.remove_book_by_title("Капитанская дочка")
        >>> str(shelf)
        'BookShelf: Книга: "Война и мир" (Автор: Л. Н. Толстой, Страницы: 1225, Рейтинг: 8.5)'
        """
        if not isinstance(title, str):
            raise TypeError("The 'title' parameter must be a string.")

        for book in self.__books:
            if book.title == title:
                self.__books.remove(book)
                return

        raise ValueError(f"No book with the title '{title}' found on the shelf.")

    def get_book_count(self):
        """
        Возвращает количество книг на полке.

        :return: Целое число, представляющее количество книг на полке.

        >>> shelf = BookShelf([])
        >>> shelf.get_book_count()
        0
        >>> book1 = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book2 = Book("Л. Н. Толстой", "Война и мир", 1225, 8.5)
        >>> shelf.add_book(book1)
        >>> shelf.add_book(book2)
        >>> shelf.get_book_count()
        2
        """
        return len(self.__books)

    @property
    def books(self):
        """
        Геттер для приватного поля books.

        >>> book1 = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book2 = Book("Л. Н. Толстой", "Война и мир", 1225, 8.5)
        >>> shelf = BookShelf([book1, book2])
        >>> for i in shelf.books:
        ...     print(i)
        Книга: "Капитанская дочка" (Автор: А. С. Пушкин, Страницы: 320, Рейтинг: 9)
        Книга: "Война и мир" (Автор: Л. Н. Толстой, Страницы: 1225, Рейтинг: 8.5)
        """
        return self.__books

    def __str__(self):
        """
        Возвращает отформатированную строку с информацией о полке книг.

        >>> book1 = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book2 = Book("Л. Н. Толстой", "Война и мир", 1225, 8.5)
        >>> shelf = BookShelf([book1, book2])
        >>> str(shelf)
        'BookShelf: Книга: "Капитанская дочка" (Автор: А. С. Пушкин, Страницы: 320, Рейтинг: 9) Книга: "Война и мир" (Автор: Л. Н. Толстой, Страницы: 1225, Рейтинг: 8.5)'
        """
        return f'BookShelf: {" ".join(str(book) for book in self.books)}'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
