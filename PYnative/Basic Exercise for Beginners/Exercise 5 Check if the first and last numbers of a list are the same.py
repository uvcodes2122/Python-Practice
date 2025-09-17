# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# # output True

# numbers_y = [75, 65, 35, 75, 30]
# # Output False


def check_first_last():

    list1 = [10, 20, 30, 40, 10]
    first_num = list1[0]
    last_num = list1[-1]

    if first_num == last_num:
        return True
    else:
        return False

print(check_first_last())