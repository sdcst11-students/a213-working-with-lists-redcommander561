#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)
name1 = input("Please enter a name from the list to remove: ")
x = str(people[name1])
people.remove(name1)
name2 = input("enter a name to replace the name removed: ")
people.append(name2[x])
print(people)