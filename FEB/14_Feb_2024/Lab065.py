# List
# It is collection of item with duplicayes allowed
# Some special functions used in List are below

my_list = [1, 2, 3]
my_list2 = [1, True, "NITESH", 12.34, False, 65, "Rahul"]

# Indexing
print("Element at the zero index",my_list[0])

# Changing an element
my_list[2] =30
print(my_list)

# Appending an element---in the end add this item
my_list.append(40)
print("New append list is", my_list)

# EXTEND
my_list.extend([50, 60, 70])
print("New extend list is", my_list)

# INSERT
my_list.insert(2, 'B')
print("New insert list is", my_list)

# Remove
my_list.remove('B')
print("New remove list is", my_list)

# Copy
new_list = my_list.copy()
print("New copy list is", new_list)

# clear
my_list.clear()
print("New clear list is", my_list)

print(new_list)

# Reverse and sort
new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)




