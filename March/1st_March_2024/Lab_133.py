# Class = exceptions

class XYZ:

    def f1(self):
        try:
            a = int(input("enter the first no"))

        except Exception as e:
            print("enter only integer")

        else:
            print(a)

        finally:
            print("finally")
c = XYZ()
c.f1()