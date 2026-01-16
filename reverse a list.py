#Write a program to reverse a list without using built-in reverse methods.

lst = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])

print(reversed_list)
