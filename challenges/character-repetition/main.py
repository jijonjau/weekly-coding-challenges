text = input("Enter a word or a phrase: ")
count = int(input("Enter the number of character repetition: "))
result = ""

if count <= 0:
    print("Repetition count must be greater than zero.")
else:
    result = ""
    for char in text:
        result += char * count
    print(result)