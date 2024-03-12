# file handling using With open file

with open ("Textdata.txt", "r") as f:
    data = f.read()
    print(data)
    f.close()