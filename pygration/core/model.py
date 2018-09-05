from .sql_predef import SQLPredef


class Model(object):
    def __init__(self, table):
        self._table_name = table
        self.__sql_migration = SQLPredef.get_default_sql_top()

    def up(self):
        pass

    def get_columns(self):
        columns = self.up()
        col_formated = []
        for column in columns:
            col_formated.append(column.get_column_sql())

        return ',\n'.join(col_formated)

    def get_sql(self):
        columns = self.get_columns()
        # Build top of model
        sql = self.__sql_migration.format(
            self._table_name,
            # self._table_name,
            columns
        )

        return sql
