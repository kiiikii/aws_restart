myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

print()
first = "water"
second = "fall"
third = first+second
print(third)

print()

name = input("what is your name: ")
print(name)

print()

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))