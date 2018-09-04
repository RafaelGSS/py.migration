from .core import Output


class Pygration(object):
    """
    Class that receive a connection and migration

    connection is a connection database
    migrations is a list of models
    """
    def __init__(self, connection, migrations):
        self.__migrations = migrations
        self.__connection = connection

    def migrate(self):
        out = Output()
        for model in self.__migrations:
            md = model()
            try:
                for sql in md.get_sql().split(';'):
                    row = self.__connection.execute(sql)
                self.__connection.commit()
                out.append_success(type(md).__name__)
            except Exception as e:
                out.append_error(type(md).__name__, str(e))
                self.__connection.rollback()

        return out
