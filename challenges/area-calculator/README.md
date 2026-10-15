# Python `math.prod()`

`math.prod()` is used to multiply **all numbers in an iterable**, such as a list or tuple.

## Example

```python
import math

numbers = [2, 3, 4]

result = math.prod(numbers)

print(result)
```

Output:

```text
24
```

Because:

```text
2 × 3 × 4 = 24
```

## Key Takeaway

Use `math.prod()` when you have **multiple values stored in an iterable**:

```python
math.prod([2, 3, 4])
```

For just two values, the normal multiplication operator is simpler:

```python
2 * 3
```

### Related

- `*` → multiplication
- `**` → power/exponentiation
- `math.pow()` → power as a math function
- `math.prod()` → product of multiple values in an iterable
