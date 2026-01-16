#Write a Python program to remove duplicate elements from a list.

lst = [1,2,2,3,4,5,5,6]
unique_list = []

for item in lst:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)