# Reference: https://docs.python.org/2/library/unittest.html
import unittest
import mysql.connector

from database_utils import DatabaseUtils

class TestDatabaseUtils(unittest.TestCase):
    HOST = "localhost"
    PORT = "3306"
    USER = "root"
    PASSWORD = "abc@123$"
    DATABASE = "People"

    def setUp(self):
        connection = mysql.connector.connect(
                 host=DatabaseUtils.HOST,
                 user=DatabaseUtils.USER,
                 password=DatabaseUtils.PASSWORD,
                 database= DatabaseUtils.DATABASE
             )
        self.connection = connection
        
        with self.connection.cursor() as cursor:
            cursor.execute("drop table if exists Person")
            cursor.execute("""
                create table if not exists Person (
                    PersonID int not null auto_increment,
                    Name text not null,
                    constraint PK_Person primary key (PersonID)
                )""")
            cursor.execute("insert into Person (Name) values ('Matthew')")
            cursor.execute("insert into Person (Name) values ('Shekhar')")
            cursor.execute("insert into Person (Name) values ('Rodney')")
        self.connection.commit()

    def tearDown(self):
        try:
            self.connection.close()
        except:
            pass
        finally:
            self.connection = None

    def count_people(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Person")
            return cursor.fetchone()[0]

    def person_exists(self, person_id):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Person where PersonID = %s", (person_id,))
            return cursor.fetchone()[0] == 1

    def test_insert_person(self):
        with DatabaseUtils(self.connection) as db:
            count = self.count_people()
            self.assertTrue(db.insert_person("Helen"))
            self.assertTrue(count + 1 == self.count_people())
            self.assertTrue(db.insert_person("Ke"))
            self.assertTrue(count + 2 == self.count_people())

    def test_get_people(self):
        with DatabaseUtils(self.connection) as db:
            self.assertTrue(self.count_people() == len(db.get_people()))

    def test_delete_person(self):
        with DatabaseUtils(self.connection) as db:
            count = self.count_people()
            person_id = 1

            self.assertTrue(self.person_exists(person_id))

            db.delete_person(person_id)

            self.assertFalse(self.person_exists(person_id))
            self.assertTrue(count - 1 == self.count_people())

if __name__ == "__main__":
    unittest.main()
