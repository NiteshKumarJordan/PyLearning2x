# FILTER
# It can filter out the list based on the logic.
# return less no of items

def even_no(num):
    return num % 2 == 0

List = [1,2,3,4,5,6,7,8,9,10]

even_numbers = filter(even_no, List)
print(list(even_numbers))
