class Password:
    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)

        else:
            print("not having any acess to view  password")

    def set_password(self, new_password):
        if len(new_password) >= 10:
            self.__password = new_password

        else:
            print("password must be at least 10 characters long")




pwd = Password("Jordan365")
print(pwd.public_var)
pwd.get_password(False)
pwd.set_password("Jordan32102")





