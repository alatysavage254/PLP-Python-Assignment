def power_greater_than_5000(base, exponent):
    result = base ** exponent  # Calculate base to the power of exponent
    if result > 5000:  # Check if result is greater than 5000
        return True
    return False  # Otherwise, return False

# Example usage:
print(power_greater_than_5000(100, 3))  # True (10^3 = 1000)
print(power_greater_than_5000(50, 5))   # True (5^5 = 3125)
print(power_greater_than_5000(2, 10))  # True (2^10 = 1024)
print(power_greater_than_5000(3, 4))   # False (3^4 = 81)
