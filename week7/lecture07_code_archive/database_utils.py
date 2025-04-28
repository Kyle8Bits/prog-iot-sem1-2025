#import MySQLdb
import mysql.connector

class DatabaseUtils:
    # HOST = "34.84.194.196"
    HOST="localhost"
    PORT = "2222"
    USER = "kyle"
    PASSWORD = "Notkyle2003@!"
    DATABASE = "lab-db"

    def __init__(self, connection=None):
        if(connection is None):
            # connection = MySQLdb.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
            #   DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
            # connection = mysql.connector.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
            #   DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
            connection = mysql.connector.connect(
                host=DatabaseUtils.HOST,
                user=DatabaseUtils.USER,
                password=DatabaseUtils.PASSWORD,
                database= DatabaseUtils.DATABASE
            )
        self.connection = connection
        print("Succeed")

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def create_person_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Person (
                    PersonID int not null auto_increment,
                    Name text not null,
                    constraint PK_Person primary key (PersonID)
                )""")
        self.connection.commit()

    def insert_person(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Person (Name) values (%s)", (name,))
        self.connection.commit()

        return cursor.rowcount == 1

    def get_people(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select PersonID, Name from Person")
            return cursor.fetchall()

    def delete_person(self, person_id):
        with self.connection.cursor() as cursor:
            # Note there is an intentionally placed bug here: != should be =
            cursor.execute("delete from Person where PersonID = %s", (person_id,))
        self.connection.commit()
