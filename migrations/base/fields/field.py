from migrations.base import SQLPredef


class Field(object):
    def __init__(self, leng):
        self._name = ''
        self._type = ''
        self.__is_primary = False
        self.__auto_increment = False
        self.__nullable = True
        self.__length = leng
        self.__default = None

    def primary_key(self):
        self.__is_primary = True

        return self

    def auto_increment(self):
        self.primary_key()
        self.__auto_increment = True

        return self

    def not_null(self):
        self.__nullable = False

        return self

    def nullable(self):
        self.__nullable = True

        return self

    def get_args(self):
        args = []
        if self.__nullable and not self.__is_primary and not self.__auto_increment:
            args.append('NULL')
        else:
            args.append('NOT NULL')

        if self.__default and not self.__is_primary and not self.__auto_increment:
            args.append('DEFAULT ' + self.__default)

        if self.__auto_increment:
            args.append('AUTO_INCREMENT')

        if self.__is_primary:
            args.append('PRIMARY KEY')

        return args

    def default(self, value):
        self.__default = value

        return self

    def get_column_sql(self):
        if self._type not in ['TIMESTAMP', 'DATETIME']:
            return SQLPredef.get_column_standard(self._name, self._type, self.__length, self.get_args())
        return SQLPredef.get_column_without_length(self._name, self._type, self.get_args())
