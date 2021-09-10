import unittest
from tests.database_tests.sercices.IsTalbeExist import IsTableExist
from database.Database import Database
from database.tables.Users import Users
from database.tables.Resources import Resurces
from database.tables.UserResource import UsersResources

class TablesExistTest(unittest.TestCase):

    def test_is_users_table_exist(self):
        talbeName = Users.getTableName()

        result = IsTableExist(talbeName).start()

        self.assertEqual(result, True)

    def test_is_resources_table_exist(self):
        talbeName = Resurces.getTableName()

        result = IsTableExist(talbeName).start()

        self.assertEqual(result, True)

    def test_is_user_resource_table_exist(self):
        talbeName = UsersResources.getTableName()

        result = IsTableExist(talbeName).start()

        self.assertEqual(result, True)

if __name__ == "__main__":
    database = Database()
    database.up()

    unittest.main()
