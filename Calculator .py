 # simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

num_1 = int(input("Enter first number: "))
Num_2 = int(input("Enter second number: "))

if select == 1:
    print(num_1, "+", Num_2, "=",
                    add(num_1, Num_2))

elif select == 2:
    print(num_1, "-", Num_2, "=",
                    subtract(num_1, Num_2))

elif select == 3:
    print(num_1, "*", Num_2, "=",
                    multiply(num_1, Num_2))

elif select == 4:
    print(num_1, "/", Num_2, "=",
                    divide(num_1, Num_2))
else:
    print("Invalid input")
