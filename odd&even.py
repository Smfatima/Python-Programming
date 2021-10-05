number = int(input("What number are you thinking?\n"))
remainder = number % 2

if (remainder == 0):
    print("the number is an even")
else:
    print("That's an odd number! Have another?")