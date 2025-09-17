# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

previous_number = 0
for i in range(10):
    print(f"Current Number: {i}  Previous Number: {previous_number}  Sum: {i + previous_number}")
    previous_number = i
