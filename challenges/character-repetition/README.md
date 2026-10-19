# Repeat Each Character

A Python exercise that repeats every character in a word or phrase a specified number of times while preserving the original order.

## Example

**Input:**
```text
Enter a word or a phrase: abc
Enter the number of character repetition: 3
```

**Output:**
```text
aaabbbccc
```

## Key Concepts Learned

- **String iteration:** Using a `for` loop to process each character individually.
- **String multiplication (`*`):** Repeating a character a specified number of times.
- **String concatenation (`+=`):** Appending each repeated character to the result.
- **User input:** Accepting text and a repetition count dynamically.

## Key Takeaway

Use `char * count` to repeat a character and `result +=` to accumulate the output without overwriting previous characters.

**Time complexity:** \(O(n \times k)\), where \(n\) is the input length and \(k\) is the repetition count.