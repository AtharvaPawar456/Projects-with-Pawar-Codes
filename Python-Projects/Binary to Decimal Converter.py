# Binary to Decimal Converter

def binary_to_decimal(binary):
    decimal = 0
    power = 0

    # Iterate over each digit in reverse order
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal

# Test the binary to decimal converter
binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)
print("Decimal equivalent:", decimal_number)


'''
=================================
Test Case:
=================================

Enter a binary number: 101010
Decimal equivalent: 42
'''