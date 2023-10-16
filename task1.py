#!python3

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""



animals = ["cat", "fish", "dog", "bear", "turtle"]


for i in range(0,5):
    num = int(input("enter a number 0-4: "))
    if 0 <= num < len(animals):
        animal = animals[num]
        print(f"the animal is {animal}")

    else:
        print("the number is out of range")





