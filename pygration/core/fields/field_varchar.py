from pygration import Field


class FieldVarchar(Field):
    def __init__(self, name, lenght=255):
        super().__init__(lenght)
        self._type = 'VARCHAR'
        self._name = name
