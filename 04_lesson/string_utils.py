class StringUtils:

    def capitalize(self, string):
        """
        Делает первую букву заглавной
        """
        return string.capitalize()

    def trim(self, string):
        """
        Убирает пробелы в начале строки
        """
        return string.lstrip()

    def to_list(self, string, delimiter=","):
        """
        Превращает строку в список по разделителю
        """
        return string.split(delimiter)


