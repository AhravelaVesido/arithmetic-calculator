# Calculator that computes arithmetic operations


#Declare calculate as custom function, set operation, num1, and num2 as parameters
def calculate(num1, num2, operation):
        if operation == "addition":
            return (num1 + num2)
        elif operation == "subtraction":
            return (num1 - num2)
        elif operation == "multiplication":
            return (num1 * num2)
        elif operation == "division":
            if num2 == 0:
                raise ValueError("Can't divide with zero")
            return (num1 / num2)


#Requires user input
# Set limit for while loop so it doesn't run infinitely
attempts = 0
limit = 5
# .lower() will transform the user input to lower case regardless of how they entered the value
operation = (input("Enter your operation (addition/subtraction/multiplication/division): ").lower())
while operation not in ["addition", "subtraction", "multiplication", "division"]:
    print("Operation is invalid! Try again")
    attempts += 1
    if attempts >= limit:
        print("No more attempts")
        exit()
    print(f"You have remaining {limit - attempts} attempts.")
    operation = (input("Enter your operation (addition/subtraction/multiplication/division): ").lower())

# Requires user input but integers only
num1 = int(input("Please enter your first number (1-100): "))
num2 = int(input("Please enter your second number (1-100): "))


#Print result based on user input
result = calculate(num1, num2, operation)
print(f"The answer is {result}")
print("All done!")

