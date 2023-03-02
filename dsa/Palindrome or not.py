string = input("Enter a string\n")

def palindrome(x):
    newString = x.replace(" ", "")

    newStringInverted = newString[::-1]

    if newString==newStringInverted:
        print(f"{x} is a palindrome")
    else:
        print(f"{x} is not a palindrome")

palindrome(string)