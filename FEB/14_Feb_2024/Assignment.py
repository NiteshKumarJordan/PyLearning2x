# palindrome using function(reverse a function)

def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


original_str = input("enter a number for pallindrome")
original_str = original_str.lower()
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("palindrome")
else:
    print("not palindrome")
