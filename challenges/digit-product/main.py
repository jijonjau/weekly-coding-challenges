n = int(input("Enter a number: "))

# Multiply the digits and print the product
if n >= 0:
    result = 1
    if n == 0:
        result = 0
    else:
        while n > 0:
            digit = n % 10
            result *= digit
            n = n // 10 # Integer (floor) division
    print("The product of the individual digits is: ", result)
else:
    print("The number entered should not be less than 0")