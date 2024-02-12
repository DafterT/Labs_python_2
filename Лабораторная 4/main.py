class ElectronicDevice:
    """
    Базовый класс для электронных устройств.
    """

    def __init__(self, brand: str, model: str, price: float):
        """
        Инициализация объекта ElectronicDevice.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param price: Цена устройства в долларах.
        """
        self.brand = brand
        self.model = model
        self.price = price

    def start_device(self) -> None:
        """
        Выполняет запуск электронного устройства
        """
        pass

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"{self.brand!r} {self.model!r} - ${self.price:.2f!r}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальное строковое представление объекта.
        """
        return f"{self.__class__.__name__!r}(brand={self.brand!r}, model={self.model!r}, price={self.price!r})"


class Smartphone(ElectronicDevice):
    """
    Дочерний класс для смартфонов.
    """

    def __init__(self, brand: str, model: str, price: float, os: str, camera_resolution: int):
        """
        Инициализация объекта Smartphone.

        :param brand: Бренд смартфона.
        :param model: Модель смартфона.
        :param price: Цена смартфона в долларах.
        :param os: Операционная система смартфона.
        :param camera_resolution: Разрешение камеры в мегапикселях.
        """
        super().__init__(brand, model, price)
        self.os = os
        self.camera_resolution = camera_resolution

    def start_device(self) -> None:
        """
        Выполняет запуск электронного устройства

        Перегрузка необходима т.к. в смартфоне иной способ запуска, нежели в другом электронном устройстве
        """
        pass

    def make_call(self, contact: str) -> None:
        """
        Вызывает указанный контакт.

        :param contact: Имя или номер контакта.
        """
        # Реализация вызова
        pass

    def take_photo(self) -> None:
        """
        Сделать фотографию смартфоном.
        """
        # Реализация съемки
        pass

    def __repr__(self) -> str:
        """
        Перегруженный метод для формального строкового представления смартфона.

        :return: Формальное строковое представление смартфона.
        """
        return f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, price={self.price}, " \
               f"os={self.os}, camera_resolution={self.camera_resolution})"


class Laptop(ElectronicDevice):
    """
    Дочерний класс для ноутбуков.
    """

    def __init__(self, brand: str, model: str, price: float, screen_size: float, storage_capacity: int):
        """
        Инициализация объекта Laptop.

        :param brand: Бренд ноутбука.
        :param model: Модель ноутбука.
        :param price: Цена ноутбука в долларах.
        :param screen_size: Размер экрана в дюймах.
        :param storage_capacity: Объем накопителя в гигабайтах.
        """
        super().__init__(brand, model, price)
        self.screen_size = screen_size
        self.storage_capacity = storage_capacity

    def start_device(self) -> None:
        """
        Выполняет запуск электронного устройства

        Перегрузка необходима т.к. в ноутбуке иной способ запуска, нежели в другом электронном устройстве
        """
        pass

    def run_program(self, program_name: str) -> None:
        """
        Запускает указанную программу на ноутбуке.

        :param program_name: Название программы.
        """
        # Реализация запуска программы
        pass

    def __repr__(self) -> str:
        """
        Перегруженный метод для формального строкового представления ноутбука.

        :return: Формальное строковое представление ноутбука.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, price={self.price!r}, " \
               f"screen_size={self.screen_size!r}, storage_capacity={self.storage_capacity!r})"
