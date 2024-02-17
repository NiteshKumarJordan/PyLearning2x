# create a function that will show whether the given string is palindrome or not

def get_reverse(str):
    return str[::-1]


def user_input(str):
    return str


my_txt = get_reverse("NITESH")
my_input = user_input("NITESH")
if my_input == my_txt:
    print("palindrome")
else:
    print("not palindrome")


# Alternatively
# def is_pallindrome(s):
#     return s == s[::-1]
#
#
# s = "NITESH"
# my_result = is_pallindrome(s)
#
# if my_result:
#     print("palindrome")
# else:
#     print("not palindrome")
