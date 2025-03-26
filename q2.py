def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Iterate through the list and replace occurrences of find_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst

# Task 2: Invoke the function with different scenarios
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))  # Expected: [1, 5, 3, 4, 5, 5]
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))  # Expected: ['orange', 'banana', 'orange']
