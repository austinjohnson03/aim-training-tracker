from typing import List

class Menu:
    def __init__(self, main_title: str):
        self._title = main_title
        self._options = []
        self._width = len(main_title)

    @property
    def title(self) -> str:
        return self._title 

    @title.setter 
    def title(self, value: str) -> None:
        self._title = value 

    @property
    def options(self) -> List[str]:
        return self._options

    def add_menu_option(self, new_option: str) -> None:
        if isinstance(new_option, str):
            self._options.append(new_option)

        else:
            raise ValueError

    def _get_longest_menu_item(self) -> int:
        title_len = len(self._title)

        longest_option = 0

        for option in self._options:
            if len(option) > longest_option:
                longest_option = len(option)
        if longest_option > title_len:
            self._width = longest_option
        else:
            self._width = title_len

    def remove_option(self, index: int) -> None:
        if 0 <= index <= len(self._options):
            del self._options[index]

        else:
            raise IndexError

    def __str__(self):
        border = "=" * (self._width + 10)
        menu_content = "\n".join(f"{i + 1}. {option}" for i, option in enumerate(self._options))
        return f"{border}\n{self._title.center(self._width + 10)}\n{border}\n{menu_content}\n{border}"


if __name__ == "__main__":
    test = Menu("The Test Menu")
    test.add_menu_option("Start")
    test.add_menu_option("Select")
    test.add_menu_option("Exit")

    print(test)

