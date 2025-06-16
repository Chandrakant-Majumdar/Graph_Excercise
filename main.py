from utils.Add import add
from utils.Multiply import multipilication
from utils.Division import division
import random


def main():
    """
    Main function to demonstrate the use of utility functions for addition, multiplication, and division.

    Logic:
    1. Continuously prompt the user to enter numbers until at least two numbers are collected.
    2. After two numbers, allow the user to enter more numbers or type 'done' to finish input.
    3. Calculate the sum of all numbers using the add() function.
       - If the sum is odd, append a random number (0-9) to the list and recalculate.
       - Repeat this process up to 3 times or until the sum becomes even.
    4. Calculate the product of all numbers using the multipilication() function.
       - If the product is odd, append a random number (0-9) to the list and recalculate.
       - Repeat this process up to 3 times or until the product becomes even.
    5. Perform division of the first number by the last number in the list using the division() function.
    6. Print all intermediate steps, including the state of the numbers list and results after each operation.
    """
    numbers = []  # List to store user input numbers

    # Collect at least two numbers from the user
    while True:
        try:
            if len(numbers) < 2:
                number = int(input("Enter a number (at least two numbers required): "))
                numbers.append(number)
            else:
                user_input = input("Enter a number (or type 'done' to finish): ")
                if user_input.lower() == 'done':
                    break
                try:
                    number = int(user_input)
                    numbers.append(number)
                except ValueError:
                    print("Invalid input. Please enter a valid number or 'done'.")
        except ValueError:
            break

    # Addition step
    sum_result = add(numbers)
    print(f"Initial numbers: {numbers}")
    print(f"Initial sum: {sum_result}")
    attempt = 0
    while sum_result & 1 == 1 and attempt < 3:
        print(f"The sum is odd ({attempt+1} attempt(s)). Adding a random number to the list and retrying.")
        attempt += 1
        rand_num = random.randint(0, 9)
        numbers.append(rand_num)
        print(f"Numbers after adding random number {rand_num}: {numbers}")
        sum_result = add(numbers)
        print(f"New sum: {sum_result}")

    # Multiplication step
    attempt = 0
    mul_result = multipilication(numbers)
    print(f"Numbers before multiplication: {numbers}")
    print(f"Initial multiplication: {mul_result}")
    while mul_result & 1 == 1 and attempt < 3:
        print(f"The multiplication is odd ({attempt+1} attempt(s)). Adding a random number to the list and retrying.")
        attempt += 1
        rand_num = random.randint(0, 9)
        numbers.append(rand_num)
        print(f"Numbers after adding random number {rand_num}: {numbers}")
        mul_result = multipilication(numbers)
        print(f"New multiplication: {mul_result}")

    # Division step
    print(f"Numbers before division: {numbers}")
    div_result = division(numbers)
    print(f"Division result (first number divided by last): {div_result}")


if __name__ == "__main__":
    main()