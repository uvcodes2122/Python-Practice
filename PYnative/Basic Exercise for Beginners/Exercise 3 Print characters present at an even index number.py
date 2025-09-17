# Write a Python code to accept a string from the user and display characters present at an even index number.
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.



input_str = input("Enter a string: ")

print ("Characters present at an even index number:")
for i in range(0, len(input_str), 2):
    print(input_str[i])



# using list slicing

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)



# method 3: 

# word = input("Enter a string: ")
# print("Characters at even index:", word[::2])
