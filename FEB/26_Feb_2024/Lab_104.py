# Real time example of constructor

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Pass123":
            print("You are allowed to login")

        else:
            print("You are not allowed to login")


login = VWOLoginPage("nitesh.com", "Pass1234")
login.loginconfirm()
