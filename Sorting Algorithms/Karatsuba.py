def karatsuba(x, y):
    # Base case for recursion: if the numbers are small, multiply them directly
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the size of the numbers (number of digits)
    n = max(len(str(x)), len(str(y)))
    half_n = n // 2

    # Split x and y into high and low parts
    high_x = x // 10**half_n
    low_x = x % 10**half_n
    high_y = y // 10**half_n
    low_y = y % 10**half_n

    # Recursively calculate the three products
    P1 = karatsuba(high_x, high_y)              # High parts
    P2 = karatsuba(low_x, low_y)                # Low parts
    P3 = karatsuba(high_x + low_x, high_y + low_y) - P1 - P2 # Sum of parts

    # Combine the results using the Karatsuba formula
    return P1 * 10**(2 * half_n) + (P3 ) * 10**half_n + P2

# Example usage
x = 1256
y = 5678
result = karatsuba(x, y)
print(f"Karatsuba result of {x} * {y} = {result}")
