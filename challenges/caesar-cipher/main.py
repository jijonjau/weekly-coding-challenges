text = input("Enter a string or a phrase: ").strip()
shift_key = int(input("Enter the shift key: "))

encrypted_string = ''

for char in text:
    position = (ord(char) - ord('a') + shift_key) % 26
    encrypted_string += chr(position + ord('a'))

print(encrypted_string)