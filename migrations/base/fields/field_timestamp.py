from migrations.base.fields import Field


class FieldTimestamp(Field):
    def __init__(self, name, lenght=255):
        super().__init__(lenght)
        self._type = 'TIMESTAMP'
        self._name = name
