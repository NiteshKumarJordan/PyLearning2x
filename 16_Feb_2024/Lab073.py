
# using map

def cube_of_no(num):
    return num ** 3


my_list = [1, 2, 3, 4, 5]


cubes = map(cube_of_no, my_list)
print(list(cubes))
