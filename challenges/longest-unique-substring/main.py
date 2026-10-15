text = input("Enter a word or phrase: ")

start = 0
last_seen = {}
max_length = 0

for i, char in enumerate(text):
    if char in last_seen and last_seen[char] >= start:
        start = last_seen[char] + 1

    last_seen[char] = i
    max_length = max(max_length,i - start + 1)

print(max_length)