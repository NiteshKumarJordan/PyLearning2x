browser = input("enter a browser name")

match browser:
    case "chrome":
        print("I am using chrome")
    case "firefox":
        print("I am using firefox")
    case "safari":
        print("I am using safari")
    case "edge":
        print("I am using edge")
    case _:
        print("I am not using any browser")