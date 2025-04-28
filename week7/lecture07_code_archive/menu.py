from database_utils import DatabaseUtils

class Menu:
    def main(self):
        with DatabaseUtils() as db:
            db.create_person_table()
        self.run_menu()

    def run_menu(self):
        while(True):
            print()
            print("1. List People")
            print("2. Insert Person")
            print("3. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                self.list_people()
            elif(selection == "2"):
                self.insert_person()
            elif(selection == "3"):
                print("Goodbye!")
                break
            else:
                print("Invalid input - please try again.")

    def list_people(self):
        print("--- People ---")
        print("{:<15} {}".format("Person ID", "Name"))
        with DatabaseUtils() as db:
            for person in db.get_people():
                print("{:<15} {}".format(person[0], person[1]))

    def insert_person(self):
        print("--- Insert Person ---")
        name = input("Enter the person's name: ")
        with DatabaseUtils() as db:
            if(db.insert_person(name)):
                print("{} inserted successfully.".format(name))
            else:
                print("{} failed to be inserted.".format(name))

if __name__ == "__main__":
    Menu().main()
