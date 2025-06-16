# Graph Exercise

This project demonstrates the use of utility functions for addition, multiplication, and division on a list of user-provided numbers. The logic is implemented in `main.py` and uses helper functions from the `utils` package.

## Features
- Prompts the user to input at least two numbers (enforced by input loop).
- Calculates the sum of all numbers using `add()` from `utils/Add.py`.
  - If the sum is odd, a random number (0-9) is appended to the list and the sum is recalculated (up to 3 times or until even).
- Calculates the product of all numbers using `multipilication()` from `utils/Multiply.py`.
  - If the product is odd, a random number (0-9) is appended to the list and the product is recalculated (up to 3 times or until even).
- Divides the first number by the last using `division()` from `utils/Division.py`.
  - Handles division by zero and raises a clear error if the last number is zero.
- Prints all intermediate steps and results, including the state of the numbers list after each operation.

## File Structure
- `main.py`: Main script to run the logic and interact with the user.
- `utils/Add.py`: Contains the `add(nums)` function for summing a list.
- `utils/Multiply.py`: Contains the `multipilication(nums)` function for multiplying a list.
- `utils/Division.py`: Contains the `division(nums)` function for dividing the first by the last number in a list, with division by zero handling.

## How to Run
1. Make sure you have Python 3 installed.
2. (Optional) Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```
4. Run the program:
   ```sh
   python main.py
   ```

## Example Usage
```
Enter a number (at least two numbers required): 5
Enter a number (at least two numbers required): 3
Enter a number (or type 'done' to finish): done
Initial numbers: [5, 3]
Initial sum: 8
Numbers before multiplication: [5, 3]
Initial multiplication: 15
The multiplication is odd (1 attempt(s)). Adding a random number to the list and retrying.
Numbers after adding random number 7: [5, 3, 7]
New multiplication: 105
...
Numbers before division: [5, 3, 7, ...]
Division result (first number divided by last): ...
```

## Notes
- The program handles invalid input gracefully and enforces at least two numbers before proceeding.
- Odd/even checks for sum and multiplication are capped at 3 attempts, with random numbers (0-9) appended each time if needed.
- Division by zero is handled with a clear error message if attempted.

