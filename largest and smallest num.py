#Write a program to find the largest and smallest numbers in a list without using built-in functions like max() or min()

numbers = [10, 5, 20, 2, 8]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
