### Python Basics Solutions

# 1. Strings
## Solution 1: String Manipulation
# Program to reverse the string "hello world".
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello world"))

## Solution 2: String Slicing
# Extract the word "world" from the string "hello world".
def extract_world(s):
    return s[6:]

print(extract_world("hello world"))

## Solution 3: String Formatting
# Function to return formatted string.
def format_intro(name, age):
    return f"My name is {name} and I am {age} years old."

print(format_intro("Alice", 25))

# 2. Lists
## Solution 1: List Manipulation
# Replace the first element in a list with 99.
def replace_first(lst):
    lst[0] = 99
    return lst

print(replace_first([1, 2, 3, 4, 5]))

## Solution 2: List Slicing
# Get the first three elements of a list.
def get_first_three(lst):
    return lst[:3]

print(get_first_three([10, 20, 30, 40, 50]))

# ## Solution 3: List Comprehension
# # Create a new list with squares of all numbers in a given list.
# def square_numbers(lst):
#     '''Create a new list with squares of all numbers in a given list.'''
#     return [x**2 for x in lst]

# print(square_numbers([1, 2, 3, 4, 5]))

# 3. Loops
## Solution 1: For Loop
# Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

## Solution 2: While Loop
# Calculate the sum of numbers from 1 to 10.
def sum_while():
    total, i = 0, 1
    while i <= 10:
        total += i
        i += 1
    return total

print(sum_while())

## Solution 3: Nested Loops
# Print a 3x3 grid of "*" characters.
def print_grid():
    for _ in range(3):
        for _ in range(3):
            print("*", end=" ")
        print()

print_grid()

# 4. Functions
## Solution 1: Basic Function
# Function to return the sum of two numbers.
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

## Solution 2: Default Arguments
# Function to greet a user, defaulting to "Guest".
def greet(name="Guest"):
    '''Function to greet a user, defaulting to "Guest".'''
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))
