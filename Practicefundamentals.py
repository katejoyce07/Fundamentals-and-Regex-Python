print('Hello World')

# this prints some text
print("Rachel Smells")

# variables
red_bucket = input("What do you want to put in the bucket? ")
print(red_bucket)

Thomas_Age = 5
Age_at_Playschool = 5

if Thomas_Age < Age_at_Playschool
    print("Thomas should be in playschool")
elif Thomas_Age == Age_at_Playschool:
    print("Enjoy playschool")
else:
    print("Thomas should be in another class")


# functions
def print_kate():
    text = "Kate is great"
    print(text)
    print(text)
    print(text)


print_kate()


def print_kate(text):
    print(text)
    print(text)
    print(text)


print_kate("Kate is Great")


def school_age_calculator(age, name):
    if age < 5:
        print("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print("Enjoy playschool", name)
    else:
        print("they grow up so fast!")


school_age_calculator(3, "Thomas")






# loops - while
x = 0
while x < 5:
    print(x)
    x = x + 1

# for
for x in range(5, 10):
    print(x)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


for d in days:
    if d == "Thu":
        continue
    print(d)


import math

print("pi is", math.pi)

# beginner practice
my_list = [5, 6, 7, 8, 9]

my_list.append(10)
print(my_list)


def add(x, y):
    return x + y


result = add(3, 5)
print(result)

# slicing
message = "Hello, World!"

for i in range(len(message)):
    print(message[i : i + 2])  # message[start,stop,step]

# Default slicing values
message = "Hello, World!"
print(message[::-1])

# user input
a = int(input("Please enter a number between 5 and 10: "))

print(type(a))


# Python exercises - Q1

num1=8
print(num1)
num2=10
print(num2)

def multipication_or_sum(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2


# first q
result = multipication_or_sum(20, 30)
print("The result is", result)

# second q
result = multipication_or_sum(40, 30)
print("The result is", result)

# Q2
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i

# Q3
# accept input string from a user
word = input("Enter word ")
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


# Google dev practice
s = "Hi"
print(s[1])
print(len(s))
print(s + " there")

pi = 3.14
text = "The value of pi is " + str(pi)

# string Methods

s = "hi"
s.lower()
s.upper()
s.strip()
s.isalpha()
s.startswith("other")

# string formatting
# F strings

value = 2.791514
print(f"approximate value = {value:.2f}")

car = {"tires": 4, "doors": 2}
print(f"car = {car}")

address_book = [
    {"name": "N.X.", "addr": "15 Jones St", "bonus": 70},
    {"name": "J.P.", "addr": "1005 5th St", "bonus": 400},
    {"name": "A.A.", "addr": "200001 Bdwy", "bonus": 5},
]

for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')

# % operator
text = (
    "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down."
    % (3, "huff", "puff", "house")
)

# adding parantheses
# Add parentheses to make the long line work:
text = (
    "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down."
    % (3, "huff", "puff", "house")
)

# If statements
# this is the formatt in Python
time_hour = 5
mood = "sleepy"

if time_hour >= 0 and time_hour <= 24:
    print("Suggesting a drink option...")
    if mood == "sleepy" and time_hour < 10:
        print("coffee")
    elif mood == "thirsty" or time_hour < 2:
        print("lemonade")
    else:
        print("water")

# Python Lists

colors = ["red", "blue", "green"]
print(colors[2])

# for and in

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)

list = ["larry", "curly", "moe"]
if "curly" in list:
    print("yay")


list = ["larry", "curly", "moe"]
list.append("shemp")  ## append elem at end
list.insert(0, "xxx")  ## insert elem at index 0
list.extend(["yyy", "zzz"])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index("curly"))  ## 2

list.remove("curly")  ## search and remove that element
list.pop(1)  ## removes and returns 'larry'
print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

# Python sorting

a = [5, 1, 4, 3]
print(sorted(a))
print(a)

strs = ["aa", "BB", "zz", "CC"]
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs, reverse=True))  ## ['zz', 'aa', 'CC', 'BB']

# Customing sorting with key
strs = ["ccc", "aaaa", "d", "bb"]
print(sorted(strs, key=len))

# Tuples

tuple = (1, 2, "hi")
print(len(tuple))
print(tuple[2])

tuple = (1, 2, "bye")

# Upper list

strs = ["hello", "and", "goodbye"]
shouting = [s.upper() + "!!!" for s in strs]
print(shouting)

# adding test elements
# Select values <= 2

nums = [2, 8, 1, 6]
small = [n for n in nums if n <= 2]
print(small)

# Select fruits containing 'a', change to upper case
fruits = ["apple", "cherry", "banana", "lemon"]
afruits = [s.upper() for s in fruits if "a" in s]
print(afruits)


# Dict hash table

dict = {}
dict["a"] = "alpha"
dict["g"] = "gamma"
dict["o"] = "omega"
print(dict)

print(dict["a"])
dict["a"] = 6
"a" in dict

if "z" in dict:
    print(dict["z"])

print(dict.get("z"))

# follwing prints A G O
for key in dict:
    print(key)

for key in dict.keys():
    print(key)

# Get the .keys() list:
print(dict.keys())

print(dict.values())

# common case of looping over the keys
for key in sorted(dict.keys()):
    print(key, dict[key])


# Dict Formatting
h = {}
h["word"] = "garfield"
h["count"] = 42
s = "I want %(count)d copies of %(word)s" % h
print(s)

s = "I want {count:d} copies of {word}".format(h)
print(s)

# Del
var = 6
del var

list = ["a", "b", "c", "d"]
del list[0]
del list[-2:]
print(list)

#Python Regular Expression - find word
import re
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
if match:
    print('found', match.group())
else:
print('did not find')


