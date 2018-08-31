from migrations import migrations
from migrations.base import Migration
from database.database import PySession
from env import DB_MIGRATION_DATABASE, DB_MIGRATION_PASSWORD, DB_MIGRATION_HOST, DB_MIGRATION_USER, DB_MIGRATION_PORT


class MigrationManager(object):
    def __init__(self):
        self.__conn = PySession(host=DB_MIGRATION_HOST, database=DB_MIGRATION_DATABASE, user=DB_MIGRATION_USER,
                                password=DB_MIGRATION_PASSWORD, port=DB_MIGRATION_PORT, autocommit=False)
        self.__migration = Migration(self.__conn, migrations)

    def run(self):
        out = self.__migration.migrate()
        out.show()


app = MigrationManager()
app.run()
