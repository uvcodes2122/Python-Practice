# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:

# result list: [25, 35, 40, 60, 90]


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

newlist = []
for l1 in list1:
    if l1%2!=0:
        newlist.append(l1)

for l2 in list2:
    if l2%2==0:
        newlist.append(l2)

print("New list is: ", newlist)

# list1.extend(list2)
# print(list1)