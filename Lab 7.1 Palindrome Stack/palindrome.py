"""
File: palindrome.py
"""

import string
from arraystack import ArrayStack

def strip(startString):
    """
    Removes all common punctuation and spaces from the given string
    and returns the resulting string.
    """

    for char in startString:
        if not char.isalpha():
            startString = startString.replace(char, '')

    return startString

def isPalindrome(startString):          
    """Returns True if string is a palindrome
    or False otherwise."""

    palindrome = True

    startString = strip(startString)
    startString = startString.lower()

    b1 = ArrayStack()

    for char in startString:
        b1.push(char)

    for i in range(len(b1)):
        if (b1.pop() != startString[i]):
            palindrome = False

    return palindrome


def main():
    while True:

        startString = input("Enter a string or Return to quit: ")
        if startString == "":
            break
        elif isPalindrome(startString):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")
            

if __name__ == '__main__': 
    main()
