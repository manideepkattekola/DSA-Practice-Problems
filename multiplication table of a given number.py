#Python program to generate the multiplication table of a given number

num = int(input("Enter num: "))

for i in range(1,11):
    print(num, "x", i, "=", num * i)