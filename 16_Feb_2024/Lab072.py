# MAP FUNCTION
# 1. Takes each iteams from the list
# 2. executes the function on it.
# 3. Return same no of elements(list)

def sq_of_number(num):
    return num ** 2


List = [1, 2, 3, 4, 5]

# In map(it takes one arguments as function name and second parameter will be the lis
# where it has to be run.

sq_nos = list(map(sq_of_number, List))
print(sq_nos)
