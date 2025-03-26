def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Swap the values and print them
    x, y = y, x
    print(f"Swapped values: x = {x}, y = {y}")
    return

# Task 2: Invoke the function with different scenarios
swap("Apple", 10)  # Expected: -1 because "Apple" is not numeric
swap(9, 17)         # Expected: Swapped values: x = 17, y = 9
