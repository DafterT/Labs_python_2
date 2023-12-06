class Lightbulb:
    def __init__(self, condition: int = 100):
        """
        Инициализация экземпляра класса Lightbulb.

        :param condition: Начальное состояние лампочки (по умолчанию 0, должно быть целым числом).
        >>> bulb = Lightbulb(50)
        >>> bulb.state
        50
        """

        if not isinstance(condition, int):
            raise TypeError("Initial state must be an integer.")
        if not (0 <= condition <= 100):
            raise ValueError("Initial state must be an integer between 0 and 100.")
        self.__condition = condition
        self.__is_on = False

    @property
    def is_on(self):
        """
        Проверяет, включена ли лампочка.

        :return: True, если лампочка включена, False в противном случае.
        >>> bulb = Lightbulb(50)
        >>> bulb.turn_on()
        Lightbulb is now ON.
        >>> bulb.is_on
        True
        """

        return self.__is_on

    @property
    def state(self):
        """
        Возвращает текущее состояние лампочки.

        :return: Текущее состояние лампочки (целое число от 0 до 100).
        >>> bulb = Lightbulb(75)
        >>> bulb.state
        75
        """

        return self.__condition

    def decrease_state(self, amount: int):
        """
        Уменьшает текущее состояние лампочки на указанное количество.

        :param amount: Количество, на которое уменьшается состояние лампочки.
        >>> bulb = Lightbulb(50)
        >>> bulb.decrease_state(20)
        >>> bulb.state
        30
        """

        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer.")
        if amount < 0:
            raise ValueError("Amount must be a non-negative integer.")
        self.__condition = max(0, self.__condition - amount)
        if self.__condition == 0 and self.__is_on:
            self.turn_off()

    def turn_on(self):
        """
        Включает лампочку, если её текущее состояние не равно нулю.
        >>> bulb = Lightbulb(50)
        >>> bulb.turn_on()
        Lightbulb is now ON.
        >>> bulb.turn_off()
        Lightbulb is now OFF.
        """

        if self.__condition > 0:
            self.__is_on = True
            print("Lightbulb is now ON.")
        else:
            print("Cannot turn on. Lightbulb is broken.")

    def turn_off(self):
        """
        Выключает лампочку
        >>> bulb = Lightbulb(50)
        >>> bulb.turn_on()
        Lightbulb is now ON.
        >>> bulb.turn_off()
        Lightbulb is now OFF.
        >>> bulb.is_on
        False
        """

        self.__is_on = False
        print("Lightbulb is now OFF.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
