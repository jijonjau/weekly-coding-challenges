# Factorial

## Problem

Read a number from input and calculate its factorial.

The factorial of `N` is the product of all positive integers from `1` to `N`.

For example:

```text id="q8j9yo"
5! = 1 × 2 × 3 × 4 × 5 = 120
```

The factorial of `0` is `1`.

## Approach

1. Create a `factorial()` function that accepts a number.
2. Start the result at `1`.
3. Loop from `1` to `N`.
4. Multiply the current result by each number.
5. Return the result after the loop finishes.
6. Print the factorial in the required format.

## Key Concepts

- Functions
- `for` loops
- `range()`
- Multiplication
- `return`
- Handling `0!`

## Run

From this folder:

```bash
python main.py
```

If that doesn't work:

```bash
python3 main.py
```

### Example

```text
Input:
5

Output:
5! = 120
```
