# Write a Python code to remove characters from a string from 0 to n and return a new string.

# Given:

# def remove_chars(word, n):
#     # write your code

# print("Removing characters from a string")
# print(remove_chars("pynative", 4)) 
# # output 'tive' first four characters are removed

# print(remove_chars("pynative", 2)) 
# # output 'native'


def remove_chars(word, n):
    # write your code
    return word[n:]

print("Removing characters from a string")
num = int(input("Enter the number: "))
print(remove_chars("pynative", num)) 
# output: first n characters are removed

print(remove_chars("pynative", 2)) 
# output 'native' first two characters are removed 