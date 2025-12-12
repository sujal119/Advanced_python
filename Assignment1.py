# Create a variable my_age and assign your age to it. Print a message using this variable.
my_age=21
print("My age is ",my_age)

# Ask the user to enter their favorite food and print a message incorporating this input.
favorite_food = input("Enter your favorite food: ")
print("IT'S GREAT! I LIKE ", favorite_food)

# Convert the string "42" to an integer and print the result.
num = int("42")
print("Converted integer:", num)

# Convert the floating-point number 3.14159 to a string and print the result.
pi_str = str(3.14159)
print("Converted string:", pi_str)


# Concatenate the strings "Hello" and "World!" and print the result.
concat="Hello, " + "world!"
print(concat)


# Use string indexing to extract the third character from the string "Python".
string="Python"
print("Third character:", string[2])

# Take a sentence as input and print only the first five words.
sentence = input("Enter a sentence: ")
words = sentence.split()           
first_five = words[:5]            
print("First five words:", " ".join(first_five))