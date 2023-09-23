from typing import Self

class Word:
    """Type used in UVsim VirtualMachine. Decimal value between -10_000 and +10_000"""

    def __init__(self, value: int) -> None:
        self.value = value

    @property
    def value(self) -> int:
        """The currently stored numerical value in Word.

        Returns:
            int: Value of Word between -10,000 and +10_000
        """
        return self.__value

    @value.setter
    def value(self, new_value: int) -> None:
        new_value = convert_to_int(new_value)
        # Removes excess digits outside of accepted range.
        self.__value = new_value % (-10_000 if new_value < 0 else 10_000)
        self.__sign = "-" if new_value < 0 else "+"

    def __add__(self, __other: object) -> Self:
        __other = Word(convert_to_int(__other))
        return Word(int(self) + int(__other))

    def __sub__(self, __other: object) -> Self:
        __other = convert_to_int(__other)
        return Word(int(self) - int(__other))

    def __mul__(self, __other: object) -> Self:
        __other = convert_to_int(__other)
        return Word(int(self) * int(__other))

    def __floordiv__(self, __other: object) -> Self:
        __other = convert_to_int(__other)
        return Word(int(self) / int(__other))

    def __truediv__(self, __other: object) -> Self:
        return self // __other

    def __lt__(self, __other: object) -> bool:
        __other = convert_to_int(__other)
        return int(self) < __other

    def __le__(self, __other: object) -> bool:
        __other = convert_to_int(__other)
        return int(self) <= __other

    def __eq__(self, __other: object) -> bool:
        __other = convert_to_int(__other)
        return int(self) == __other

    def __ge__(self, __other: object) -> bool:
        __other = convert_to_int(__other)
        return int(self) >= __other

    def __gt__(self, __other: object) -> bool:
        __other = convert_to_int(__other)
        return int(self) > __other

    def __hash__(self) -> int:
        return self.value

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return self.__sign + str(abs(self.value))

    def __repr__(self) -> str:
        return str(self)

def convert_to_int(thing: object) -> int:
    """Attempt to convert any type to an int. Only works on int, float, str, and Words

    Args:
        thing (object): Object to convert to an int

    Raises:
        TypeError: When input is not a type that can be converted to an int (ex: list)
        ValueError: When input is a string or float that cannot be converted

    Returns:
        int: Converted integer.
    """
    if not isinstance(thing, (int, float, str, Word)):
        raise TypeError(f"Object of type \"{type(thing)}\" can not be converted to int.")

    try:
        return int(thing)
    except:
        raise ValueError(f"Object with value \"{thing}\" could not be converted to int.")