from pygration import Pygration
from pygration.example import migrations
from pymysql_wrapper import Session


class MigrationManager(object):
    def __init__(self):
        self.__conn = Session(host='127.0.0.1', database='example', user='example',
                              password='example', port=3306, autocommit=False)
        self.__migration = Pygration(self.__conn, migrations)

    def run(self):
        out = self.__migration.migrate()
        out.show()


app = MigrationManager()
app.run()
