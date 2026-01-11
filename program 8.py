string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is palindrome")
else:
    print("The string is NOT palindrome")