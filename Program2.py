# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.
name = input("What is your name?")
print(name)
print(name)
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.

name = input("What is your name?")
print("!" + name + "!" + name + "!")
## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
street_address = input("Enter your street address: ")
city_and_postal_code = input("Enter your city and postal code: ")

print("\nFirst name: " + first_name)
print("Last name: " + last_name)
print("Street address: " + street_address)
print("City and postal code: " + city_and_postal_code )
print()
print()


## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out


first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")
third_word = input("Enter the third word: ")


result = first_word + '-' + second_word + '-' + third_word
print("Concatenated result:", result)

## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.

# Collect user inputs
name = input("Please type in a name: ")
year = input("Please type in a year: ")

# Print the short story using the provided information
print("\n")
print(name + " is a valiant knight, born in the year " + year + "." " One morning " + name + " woke up to an awful racket a dragon was approaching the village."
" Only " + name + " could save the village's residents." )
