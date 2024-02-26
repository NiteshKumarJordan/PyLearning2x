my_dict = {'a': 2, 'b': 3, 'c': 4, 'd': 5}
for k, v in my_dict.items():
    if k == 'a':
        print("A is found")
    else:
        print("Nothing is found")


op = 'b' in my_dict and 'c' in my_dict
print(op)

