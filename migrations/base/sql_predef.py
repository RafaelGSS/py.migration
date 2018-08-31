class SQLPredef(object):
    drop_table_if_exist = 'DROP TABLE IF EXISTS `{}`;\n'
    create_table = 'CREATE TABLE `{}` (\n{}\n)'
    column_standard = '`{}` {}({}) {}'
    column_without_lenght = '`{}` {} {}'

    @staticmethod
    def get_default_sql_top():
        return SQLPredef.drop_table_if_exist + SQLPredef.create_table

    @staticmethod
    def get_column_standard(name_column, type_column, length, args):
        args_col = ' '.join(args)
        return SQLPredef.column_standard.format(name_column, type_column, length, args_col)

    @staticmethod
    def get_column_without_length(name_column, type_column, args):
        args_col = ' '.join(args)
        return SQLPredef.column_without_lenght.format(name_column, type_column, args_col)
