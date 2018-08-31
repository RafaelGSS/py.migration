from migrations.base.fields import Field


class FieldChar(Field):
    def __init__(self, name, lenght):
        super().__init__(lenght)
        self._type = 'CHAR'
        self._name = name
