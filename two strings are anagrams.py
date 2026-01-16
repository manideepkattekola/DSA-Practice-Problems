#Write a program to check whether two strings are anagrams.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1)!=len(str2):
    print("Not anagram")
else:
    if sorted(str1) == sorted(str2):
        print("strings are anagrams")
    else:
        print("Not anagram")