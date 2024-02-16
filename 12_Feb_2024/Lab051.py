# Match
# match is similar to switch case
# VBreak is not needed in case of match and case

numbers = int(input("Enter a number between 1-6\n"))
match numbers:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case _:
        print("Not a number between 1 and 6")
