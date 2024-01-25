#   a114_divisible.py

# loop while the numbers are not divisible (the remainder is 0)

remainder = -1
while remainder != 0:
    # get two numbers from user

    num1 = input("Please enter a number: ")
    num2 = input("Please enter another number: ")
    remainder = int(num1) % int(num2)
    # inform user of result
    if remainder != 0:
        print(f"Number {num1} is not divisible by number {num2}.")

# inform user of result
print(f"Number {num1} is divisible by number {num2}.")
