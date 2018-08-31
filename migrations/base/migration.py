from migrations.base import Output


class Migration(object):
    def __init__(self, connection, migrations):
        self.__migrations = migrations
        self.__connection = connection

    def migrate(self):
        out = Output()
        for model in self.__migrations:
            md = model()
            try:
                row = self.__connection.execute_many(md.get_sql().split(';'))
                self.__connection.commit()
                out.append_success(type(md).__name__)
            except Exception as e:
                out.append_error(type(md).__name__, str(e))
                self.__connection.rollback()

        return out
