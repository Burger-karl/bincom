import random

def generate_random_binary():
    binary_number = ''.join(random.choice('01') for _ in range(4))
    return binary_number

def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

# Generate a random 4-digit binary number
random_binary = generate_random_binary()

# Convert the binary number to decimal
decimal_number = binary_to_decimal(random_binary)

print(f"Generated binary number: {random_binary}")
print(f"Equivalent decimal number: {decimal_number}")
