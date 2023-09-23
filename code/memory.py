from typing import Union
from word import Word

class Memory:
    def __init__(self, contents: list = None, size: int = None) -> None:
        if (contents is None) and (size is None):
            size = 100
        elif size is None:
            size = len(contents)
        
        # Initialize as empty memory if no contents are given.
        if contents is None:
            self.__memory_list = [Word(0) for _ in range(size)]
            return

        # Check if the size of contents is larger than the provided size.
        if len(contents) > size:
            raise ValueError("Initial Memory contents cannot exceed the size of Memory.")
        # Check if any element of contents is not a Word.
        if any(not isinstance(item, Word) for item in contents):
            raise TypeError("Initial memory can only contain items of type \"Word\".")
        
        self.__memory_list = contents + [Word(0) for _ in range(size - len(contents))]

    def write(self, value: Word, location: int) -> None:
        """Write a value into a location in Memory.

        Args:
            value (Word): Value to be written
            location (int): Location to be written to.
        """
        if not isinstance(value, Word):
            raise TypeError(f"Only values of type \"Word\" can be written into Memory.")
    
        self.__memory_list[location] = value
    
    def read(self, location: int) -> Word:
        """Return Word from given location in memory."""
        return self.__memory_list[location]
    
    def __getitem__(self, key: object) -> Union[Word, list[Word]]:
        return self.__memory_list[key]
    
    def __str__(self) -> str:
        joined = ""
        for index, word in enumerate(self.__memory_list):
            joined += f"{index}: {word}\n"
        
        return joined.strip("\n")
    
    def __repr__(self) -> str:
        return f"Memory({self.__memory_list})"
        
def main():
    a = Memory()
    b = [i for i in range(100)]
    print(a)

if __name__ == "__main__":
    main()
