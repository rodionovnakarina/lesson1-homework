class StringUtils:
    def capitalize(self, string: str) -> str:
        """Делает первую букву заглавной"""
        if not string:
            return ""
        return string[0].upper() + string[1:]

    def trim(self, string: str) -> str:
        """Удаляет пробелы в начале и в конце строки"""
        if not string:
            return ""
        return string.strip()

    def to_list(self, string: str, delimeter: str = ",") -> list:
        """Преобразует строку в список по разделителю"""
        if not string:
            return []
        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        """Проверяет, есть ли символ в строке"""
        if not string or not symbol:
            return False
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """Удаляет указанный символ из строки"""
        if not string or not symbol:
            return string
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        """Проверяет, начинается ли строка с символа"""
        if not string or not symbol:
            return False
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """Проверяет, заканчивается ли строка символом"""
        if not string or not symbol:
            return False
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """Проверяет, пустая ли строка"""
        if string == "" or string is None:
            return True
        return False

    def list_to_string(self, lst: list, joiner: str = ",") -> str:
        """Объединяет список в строку с разделителем"""
        if not lst:
            return ""
        return joiner.join(lst)



