# Graph Exercise

This project demonstrates the use of utility functions for addition, multiplication, and division on a list of user-provided numbers. The logic is implemented in `main.py` and uses helper functions from the `utils` package.

## Features
- Collects at least two numbers from the user, with the option to add more.
- Calculates the sum of all numbers using `add()` from `utils/Add.py`.
  - If the sum is odd, it is appended to the list and recalculated (up to 3 times or until even).
- Calculates the product of all numbers using `multipilication()` from `utils/Multiply.py`.
  - If the product is odd, it is appended to the list and recalculated (up to 3 times or until even).
- Divides the first number by the last using `division()` from `utils/Division.py`.
- Prints all intermediate steps and results.

## File Structure
- `main.py`: Main script to run the logic and interact with the user.
- `utils/Add.py`: Contains the `add(nums)` function for summing a list.
- `utils/Multiply.py`: Contains the `multipilication(nums)` function for multiplying a list.
- `utils/Division.py`: Contains the `division(nums)` function for dividing the first by the last number in a list.

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

## Example Input and Output

**Example Input:**
```
Enter a number: 1
Enter a number: 3
Enter a number (or type 'done' to finish): 5
Enter a number (or type 'done' to finish): done
```

**Example Output:**
```
Initial numbers: [1, 3, 5]
Initial sum: 9
The sum is odd (1 attempt(s)). Adding sum to the list and retrying.
Numbers after adding sum: [1, 3, 5, 9]
New sum: 18
Numbers before multiplication: [1, 3, 5, 9]
Initial multiplication: 135
The multiplication is odd (1 attempt(s)). Adding multiplication to the list and retrying.
Numbers after adding multiplication: [1, 3, 5, 9, 135]
New multiplication: 18225
The multiplication is odd (2 attempt(s)). Adding multiplication to the list and retrying.
Numbers after adding multiplication: [1, 3, 5, 9, 135, 18225]
New multiplication: 3320625
The multiplication is odd (3 attempt(s)). Adding multiplication to the list and retrying.
Numbers after adding multiplication: [1, 3, 5, 9, 135, 18225, 3320625]
New multiplication: 11068706250
Numbers before division: [1, 3, 5, 9, 135, 18225, 3320625]
Division result (first number divided by last): 3.032961229293477e-07
```

## Notes
- The program handles invalid input gracefully.
- The logic for odd/even checks and retries is capped at 3 attempts for both sum and multiplication.
