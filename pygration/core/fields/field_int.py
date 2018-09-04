from .field import Field


class FieldInt(Field):
    def __init__(self, name, lenght=11):
        super().__init__(lenght)
        self._type = 'INT'
        self._name = name