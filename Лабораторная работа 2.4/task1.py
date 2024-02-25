import doctest


class Stringinstrument:
    """ Базовый класс струнных иснтрументов. """

    def __init__(self, name: str, company: str, string_type: str, string_number: int):
        """
        Создание и подготовка к работе объекта "Струнный инструмент"
        :param name: Название инструмента, которое не изменяется
        :param company: Компания производитель, которая не изменяется
        :param string_type: Тип струнн
        :param string_number: Количество струнн

        Примеры:
        >>> instr = Stringinstrument('Гитара', 'Gibson', 'Нейлоновые', 6)
        """
        self._name = name
        self._company = company
        self.string_type = string_type
        self.string_number = string_number

    @property
    def string_number(self) -> int:
        return self._string_number

    @string_number.setter
    def string_number(self, new_string_number: int) -> None:
        if not isinstance(new_string_number, int):
            raise TypeError("Количество струн должно быть типа int")
        if not new_string_number > 0:
            raise TypeError("Количество струн должно быть больше 0")
        self._string_number = new_string_number

    def average_cost(self) -> float:
        """
        Фукнция определяет среднюю стоимость струнного инструмента заданной компании
        :return: Средняя стоимость инструмента
        """

    def chord_notes(self, chord: str) -> str:
        """
        Функция определяет какие ноты нужны для образования аккорда
        :param chord: Аккорд
        :return: Необходимые ноты для аккорда
        """

    def __str__(self):
        return f"Иснтрумент {self._name}. Производитель {self._company}. Тип струнн {self.string_type}. " \
               f"Количество струнн {self._string_number}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, company={self._company!r})," \
               f" string_type={self.string_type!r}, string_number={self._string_number!r}"


class Guitar(Stringinstrument):
    def __init__(self, name: str, company: str, string_type: str, string_number: int, guitar_type: str):
        """
        Создание и подготовка к работе объекта "Укулеле"
        :param guitar_type:
        Примеры:
        >>> instr = Ukulele('Гитара', 'Gibson', 'Нейлоновые', 6, 'Акустическая')
        """
        super().__init__(name, company, string_type, string_number)
        self.guitar_type = guitar_type

    @property
    def guitar_type(self) -> str:
        return self._guitar_type

    @guitar_type.setter
    def guitar_type(self, new_guitar_type: str) -> None:
        if not isinstance(new_guitar_type, str):
            raise TypeError("Тип гитары должен быть типа str")

        self._guitar_type = new_guitar_type

    def average_cost(self) -> float:
        """
        Фукнция определяет среднюю стоимость гитары заданной компании, которая отличается от средней стомости всех
        струнных инструментов этой компании
        :return: Средняя стоимость гитары
        """

    def note_string(self, chord: str):
        """
        Функция определяет то, какие струны и лады отвечают за ноты, необходимые для создания аккорда
        :param chord:
        :return: Струны и лады
        """
        super().chord_notes(chord)

    def __str__(self):
        return f"Иснтрумент {self._name}. Производитель {self._company}. Тип струнн {self.string_type}. " \
               f"Количество струнн {self._string_number}. Тип гитары {self.guitar_type}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, company={self._company!r})," \
               f" string_type={self.string_type!r}, string_number={self._string_number!r}, " \
               f"guitar_type={self.guitar_type}"


class Ukulele(Stringinstrument):
    def __init__(self, name: str, company: str, string_type: str, string_number: int, material: str):
        """
        Создание и подготовка к работе объекта "Укулеле"
        :param material: Материал укулеле
        Примеры:
        >>> instr = Ukulele('Укулеле', 'Gibson', 'Нейлоновые', 4, 'Пластик')
        """
        super().__init__(name, company, string_type, string_number)
        self.material = material

    def average_cost(self) -> float:
        """
        Фукнция определяет среднюю стоимость укулеле заданной компании, которая отличается от средней стомости всех
        струнных инструментов этой компании
        :return: Средняя стоимость укулеле
        """

    def note_string(self, chord: str):
        """
        Функция определяет то, какие струны и лады отвечают за ноты, необходимые для создания аккорда
        :param chord:
        :return: Струны и лады
        """
        super().chord_notes(chord)

    def __str__(self):
        return f"Иснтрумент {self._name}. Производитель {self._company}. Тип струнн {self.string_type}. " \
               f"Количество струнн {self._string_number}. Материал укулеле {self.material}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, company={self._company!r})," \
               f" string_type={self.string_type!r}, string_number={self._string_number!r}, " \
               f"material={self.material}"


if __name__ == "__main__":
    doctest.testmod()
    pass
