class BankAccount:
    def __init__(self):
        self.balance = 0
        self._private_key = 100

    def public_fn(self):
        print("Account")

    def deposit(self, amount):
        self.balance += amount


    def _withdraw(self, amount):
        self.balance -= amount

    def __get_balance(self):
        print("your Balance:", self.balance)

    def if_you_are_auth(self, flag):
        if flag == True:
            self.__get_balance()

        else:
            print("You are not authenticated")

    def if_you_are_BankManager(self,amount):
        self._withdraw(amount=amount)




bank = BankAccount()
bank.deposit(1000)
bank.if_you_are_BankManager(500)
bank.if_you_are_auth(True)








