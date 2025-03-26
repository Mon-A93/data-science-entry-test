def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError("Both num and divisor must be numeric.")

    # Check divisibility using modulus
    return num % divisor == 0

# Task 2: Invoke the function with different scenarios
print(check_divisibility(10, 2))  # Expected: True
print(check_divisibility(7, 3))   # Expected: False
