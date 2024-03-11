# INHERITANCE
# sINGLE INHERITANCE

class Father:
    gold = 5
    __private_villa = "Goa"

    def Home(self):
        print("Luxury home in Delhi")

    def private_villas_access(self, is_my_son):
        if is_my_son:
            print(self.__private_villa)
        else:
            print("Not allowed its a private prroperty")


father = Father()

class Son(Father):
    pass


son = Son()
print(son.gold)
son.Home()
son.private_villas_access(False)


