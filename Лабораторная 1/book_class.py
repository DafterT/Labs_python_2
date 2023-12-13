class Book:
    def __init__(self, author: str, title: str, pages: int, rating: [int, float]):
        """
        Инициализация экземпляра класса.

        :param author: Автор произведения
        :param title: Заголовок произведения
        :param pages: Количество страниц в книге
        :param rating: Рейтинг книги

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        """

        self.author = author
        self.title = title
        self.pages = pages
        self.rating = rating

    @property
    def author(self):
        """
        Геттер для поля author

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.author
        'А. С. Пушкин'
        """
        return self.__author

    @author.setter
    def author(self, author: str):
        """
        Сеттер для поля author

        :param author: Новый автор произведения

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.author = 'Пушкин А. С.'
        >>> book.author
        'Пушкин А. С.'
        """
        if not isinstance(author, str):
            raise TypeError("Author must be str.")
        if len(author) == 0:
            raise ValueError("Author must be not empty.")
        self.__author = author

    @property
    def title(self):
        """
        Геттер для поля title

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.title
        'Капитанская дочка'
        """
        return self.__title

    @title.setter
    def title(self, title: str):
        """
        Сеттер для поля title

        :param title: Новый заголовок произведения

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.title = 'Новый заголовок'
        >>> book.title
        'Новый заголовок'
        """
        if not isinstance(title, str):
            raise TypeError("Title must be str.")
        if len(title) == 0:
            raise ValueError("Title must be not empty.")
        self.__title = title

    @property
    def pages(self):
        """
        Геттер для поля pages

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.pages
        320
        """
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        """
        Сеттер для поля pages

        :param pages: Новое количество страниц в книге

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.pages = 400
        >>> book.pages
        400
        """
        if not isinstance(pages, int):
            raise TypeError("Pages must be int.")
        if pages <= 0:
            raise ValueError("Pages must be more than 0.")
        self.__pages = pages

    @property
    def rating(self):
        """
        Геттер для поля rating

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.rating
        9
        """
        return self.__rating

    @rating.setter
    def rating(self, rating: [int, float]):
        """
        Сеттер для поля rating

        :param rating: Новый рейтинг книги

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> book.rating = 8.5
        >>> book.rating
        8.5
        """
        if not isinstance(rating, (int, float)):
            raise TypeError("Rating must be int or float.")
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be in [0; 10].")
        self.__rating = rating

    def __str__(self):
        """
        Возвращает отформатированную строку с информацией о книге.

        >>> book = Book("А. С. Пушкин", "Капитанская дочка", 320, 9)
        >>> str(book)
        'Книга: "Капитанская дочка" (Автор: А. С. Пушкин, Страницы: 320, Рейтинг: 9)'
        """
        return f'Книга: "{self.title}" (Автор: {self.author}, Страницы: {self.pages}, Рейтинг: {self.rating})'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
