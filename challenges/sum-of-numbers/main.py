n = int(input("How many numbers will you enter? "))
result = 0

for i in range(n):
    result += int(input())

print(f"Sum: {result}")