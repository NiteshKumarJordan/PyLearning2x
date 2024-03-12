
class read_file:
    def __init__(self):
        self.f = open("file.txt", "r")
        self.data = self.f.read()
        self.f.close()
        print(self.data)
    print(" all data extracted")



class UtilsDB:
    def read_db_mysql(self):
        print("reading my sql database")


def read_from_db_inside():
    print("reading from db")

