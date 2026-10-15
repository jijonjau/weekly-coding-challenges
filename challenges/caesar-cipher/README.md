# Caesar Cipher

A Python exercise that encrypts a lowercase string by shifting each letter forward through the alphabet.

## Example

**Input:**

```text
abc
3
```

**Output:**

```text
def
```

Each letter moves three positions forward: `a → d`, `b → e`, `c → f`.

## Solution

```python
text = input().strip()
shift = int(input())

encrypted = ""

for char in text:
    position = (ord(char) - ord('a') + shift) % 26
    encrypted += chr(position + ord('a'))

print(encrypted)
```

## Key Concepts Learned

- **`for` loop:** Processes each character individually.
- **`ord()`:** Converts a character into its numeric code.
- **`chr()`:** Converts a numeric code into a character.
- **Modulo (`%`):** Keeps the letter position within the range `0–25`, allowing wraparound from `z` to `a`.
- **String concatenation (`+=`):** Builds the encrypted string one character at a time.

## Important Takeaway

The Caesar cipher shifts each letter by a fixed amount. Subtracting `ord('a')` converts character codes into zero-based alphabet positions, while adding it back converts the result into a valid character code.

**Time complexity:** \(O(n)\), where \(n\) is the length of the input string.

## Caesar Cipher Formula

\[
E(x) = (x + s) \bmod 26
\]

Where:

- `x` = letter's zero-based position (a = 0, ..., z = 25)
- `s` = shift amount
- `26` = number of letters in the alphabet
- `E(x)` = encrypted letter's position
