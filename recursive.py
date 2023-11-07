def recursive_search(lst, target):
    if not lst:
        return False
    
    if lst[0] == target:
        return True
    
    return recursive_search(lst[1:], target)

# Example usage:
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target_number = int(input("Enter the number you want to search for: "))

result = recursive_search(numbers, target_number)

if result:
    print(f"{target_number} is found in the list.")
else:
    print(f"{target_number} is not found in the list.")
