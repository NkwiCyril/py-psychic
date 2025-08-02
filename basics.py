#####################################
# COMMENTS
#####################################
# Here is a single line comment

# Comments can be used to explain Python code.
# Comments can be used to make the code more readable.
# Comments can be used to prevent execution when testing code.

"""
This is a comment written in more than just one line.
According to Py docs this will not display in the code output
I hope it does not 😂
"""
#####################################
# Now let me get a bit on VARIABLES
#####################################


import random
a = 3
b = 5
c = "Nkwi Cyril, SWE"

print("variable A: ", a)
print("variable B: ", b)
print("variable C: ", c)

# CASTING: specifying the datatype of a variable

d = str(3)  # '3'
e = float(3)  # 3.0
f = int(3)  # 3

# In order to get the type of a variable, use type() function

model = "elixir"
parameters = "117 billions params"
year_of_creation = 2023

print("")
print("Printing the types...")
print(type(model))
print(type(parameters))
print(type(year_of_creation))


# Assigning multiple values
fruit_1, fruit_2, fruit_3 = "Orange", "Mango", "Banana"

print("")
print("Printing all fruits...")
print(fruit_1)
print(fruit_2)
print(fruit_3)

# One value to multiple variables
greet_1 = greet_2 = greet_3 = "Good morning"

print("")
print("Printing all greetings...")
print(greet_1)
print(greet_2)
print(greet_3)

# the `global` keyword


def newfuncion():
    global global_var
    global_var = "nice"


newfuncion()  # the function has to be called first before the var x us available outside the scope

print("")

x = 'awesome'


def myfunc():
    x = 'fantastic'


myfunc()
print('Python is ' + x)

print(global_var)

# DATATYPES

# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType

print("")
print("A random number: ", random.randrange(1, 10))

# Working with STRINGS in Python

print("")
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

my_string = "Go hard or go home free" + "expensive"

# find the existence of a specific string in another
print("expensive" in my_string)

wave = "Hello, World!"
print(wave[2:5])

# String Modification

upper = "uppercase string".upper()
lower = "lowercase string".lower()
capitalize = "camel case".capitalize()
remove_whitespace = "  here   is the code for the system override".strip()
replace_string = wave.replace("Hello", "Hi")
# split the string into substrings if any instance of the separator is found
split_string = wave.split(" ")

print("")
print("Manipulating the string...")
print(upper)
print(lower)
print(capitalize)
print(remove_whitespace)
print(replace_string)
print(split_string)

# String Concatenation

string_a = "Hello,"
string_b = "World"

conc_string = string_a + " " + string_b

print("")
print("Concatenating the strings...")
print(conc_string)

# Format Strings

print("")
age = 22
txt = f"My name is Nkwi Cyril and I am {11 * 2} years old"
txt_2 = f"My name is Nkwi Cyril and I am {age:.2f} years old"

print(txt)
print(txt_2)

# PYTHON COLLECTION DATATYPES
# 1. LIST
# 2. TUPLE
# 3. SET
# 4. DICTIONARY

# LISTS: store multuple items in a single variable

cart = ["apple", "milk", "fan", "guava", "clothing", "orange"]
fruits = ["apple", "mango", "grape", "guava", "orange", "banana"]

print("")
print("Shopping cart: ")
for item in cart:
    print("\t", item)

print("Number of items: ", len(cart))  # get the number of items in the list
print("Datatype of cart: ", type(cart))  # <class 'list'>

# Access list items

print(cart[0])  # first item in the list; first
print(cart[len(cart) - 1])  # last item in the list; clothing
print(cart[-1])  # last item in the list; clothing
print(cart[-2])  # second to the last item in the list; detergents
# returns items from the beginning to the index (exclusive) specified; ["apples", "milk"]
print(cart[:2])

# returns items from index specified (exclusive) to the last item
print(cart[2:])
# returns the fourth to the last item to the last but one element
print(cart[-4:-1])

# check if all items in cart are fruits, comparing with the fruits list

for item in cart:
    if item in fruits:
        print("Item is a fruit")
    else:
        print("Item is not a fruit")


# change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "apple"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# insert an item to cart; specific index
cart.insert(2, "Palm nut")

# insert item to the end of a list
cart.append("PS5")

# extend the list to another list
print(cart.extend(thislist))

# clear the entire list, renders the list empty
# cart.clear()

# del the entire list
# del cart

# remove the first occurrence of an item in a list
# cart.remove(item)

# remove an item at a specific index or simple remove the last item of the list (when no index is specified as argument)

# cart.pop() # removes the last item in cart
# cart.pop(2) # removes item at index 2
# cart.pop(len(cart) - 1) # removes last item in cart

# LOOP lists
# Print all elements in thislist
print("")
print("Printing elements in thislist...")
for x in thislist:
    print(x)

print("")
for i in range(len(thislist)):
    print([i, thislist[i]])

k = 0

while k < len(thislist):
    print(thislist[k])
    k += 1

items_with_a = []

for item in cart:
    if "a" in str(item):
        print(f"{item} has the letter 'a'")
        items_with_a.append(item)

print("Items with letter 'a'", items_with_a)

# Sort lists
# Sort list in ascending alphabetical order
cart.sort(key=str.lower)

# Reverse list
cart.reverse()


#####################################
# PYTHON TUPLES
# Tuple is a collection which is ordered and unchangeable
#####################################

# packing a tuple
cars = ("bugatti", "ferrari", "lambo", "rolls royce",
        "pagani", "aston martin", "mercedes-benz")

print("")
print("Working on Cars Tuple...")
print("Datatype of a tuple: ", type(cars))
print(len(cars))

# since tuples are unchangeable, they will only have to be coverted to
# lists and tampered with before reverting back to a tuple
# e.g.

cars_list = list(cars)
print("list of cars: ", cars_list)

cars_list[0] = "maseratti"
cars_tuple = tuple(cars_list)

print("tuple of cars: ", cars_tuple)

