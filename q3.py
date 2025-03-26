def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists in the dictionary
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")

    # Update or add the key-value pair
    dct[key] = value
    return dct

# Task 2: Invoke the function with different scenarios
print(update_dictionary({}, "name", "Alice"))  # Expected: {'name': 'Alice'}
print(update_dictionary({"age": 25}, "age", 26))  # Expected: {'age': 26}, and prints "Original value for 'age': 25"
