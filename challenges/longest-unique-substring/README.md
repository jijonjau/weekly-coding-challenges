# Longest Unique Substring

Find the length of the longest substring that contains no repeated characters.

## Example

**Input:**

```text
pwwkew
```

**Output:**

```text
3
```

**Explanation:** The longest substrings without repeating characters include `wke` and `kew`, each with a length of 3.

## Solution

```python
text = input()

start = 0
last_seen = {}
max_length = 0

for i, char in enumerate(text):
    if char in last_seen and last_seen[char] >= start:
        start = last_seen[char] + 1

    last_seen[char] = i
    max_length = max(max_length, i - start + 1)

print(max_length)
```

## Key Concepts Learned

- **Substring:** A continuous sequence of neighbouring characters in a string.
- **Sliding window:** A range of characters that expands or moves forward as we process the string.
- **`enumerate()`:** Returns both the index and character when iterating over a string.
- **Dictionary (`last_seen`):** Records the last index at which each character appeared.
- **Window adjustment:** When a repeated character occurs inside the current window, move `start` past its previous occurrence.
- **`max()`:** Keeps track of the largest valid window length found so far.

## Important Takeaways

1. A repeated character only matters if its previous occurrence is **inside the current window**.
2. When a repetition occurs, move the window's starting position instead of restarting the loop.
3. Continue processing the remaining characters after detecting a repetition.
4. Use `i - start + 1` to calculate the current window length because string indexes start at zero.

**Time complexity:** \(O(n)\), where \(n\) is the length of the string. Each character is processed once.

**Space complexity:** \(O(k)\), where \(k\) is the number of distinct characters stored in the dictionary.
