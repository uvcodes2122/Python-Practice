# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


int1 = 20
int2 = 30

product = int1 * int2
if product <= 1000:
    print("Product:", product)
else:
    print("Sum:", int1 + int2)


# while True:
#     int1 = int(input("Enter first integer: "))
#     int2 = int(input("Enter second integer: "))

#     # int1 = 20
#     # int2 = 30

#     product = int1 * int2
#     if product <= 1000:
#         print("Product:", product)
#     else:
#         print("Sum:", int1 + int2)

#         # ask user if they want to continue
#         choice = input("Do you want to continue? (yes/no): ").strip().lower()
#         if choice == "no":
#             print("Program stopped.")
#             break