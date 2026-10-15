# Sum of Numbers

A simple Python practice exercise that demonstrates how to read a **count**, use it to control a loop, and then process multiple inputs.

## What I Learned

The first input can be used as a **count** rather than as part of the actual data.

For example:

```text
4
10
20
30
40
```

The `4` means:

> "There are 4 numbers coming next."

The numbers that should actually be summed are:

```text
10 + 20 + 30 + 40
```

## Key Concept

```python
n = int(input("How many numbers will you enter? "))

result = 0

for i in range(n):
    result += int(input())

print(f"Sum: {result}")
```

### How it works

1. Read the count: `n = 4`
2. Create an accumulator: `result = 0`
3. Loop `n` times using `range(n)`
4. Read one number on each iteration
5. Add each number to `result`
6. Print the final sum

### Important Takeaway

The first input is **not necessarily part of the data**.

It can be metadata that tells the program **how many values to expect**.

This pattern is common when processing a sequence of inputs.
