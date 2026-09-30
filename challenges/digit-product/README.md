# Digit Product

## Problem

Read a non-negative integer and multiply all of its digits together.

For example:

Input: 234
Output: 24

Because:

2 × 3 × 4 = 24

## Requirements

- Read a non-negative integer from the user.
- Do not convert the number to a string.
- Use arithmetic operations to extract the digits.
- Multiply the digits together.
- Print the result.

## Approach

1. Get the number from the user.
2. Use `% 10` to extract the last digit.
3. Multiply the digit with the current result.
4. Use `// 10` to remove the last digit.
5. Repeat until the number becomes `0`.
6. Print the result.

## Run

From this folder:

python main.py

If that doesn't work, use:

python3 main.py

Example:

Enter a number: 234
The product of digits of the number is: 24
