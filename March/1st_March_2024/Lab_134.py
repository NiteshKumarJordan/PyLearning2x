# Exception = Custom exception

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

balance = 100
withdraw_amount = int(input("enter the amount for drawing"))
if withdraw_amount > balance:
    raise CustomException("insufficient balance")
else:
    balance -= withdraw_amount
    print("your balance:", balance)
    print("your withdrawal amount:", withdraw_amount)
    print("your new balance:", balance)

