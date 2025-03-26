def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Reverse the string using slicing
    return s[::-1]

# Task 2: Invoke the function with different scenarios
print(string_reverse("Hello World"))  # Expected: "dlroW olleH"
print(string_reverse("Python"))  # Expected: "nohtyP"
