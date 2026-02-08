def find_duplicates():
    """
    This function prompts the user to enter a list of numbers separated by spaces,
    and then identifies and prints the duplicate numbers from the list.
    """
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    duplicates = []
    for num in numbers:
        # Check if the number is a duplicate and not already in the duplicates list
        if numbers.count(num) > 1 and num not in duplicates: 
            duplicates.append(num)
    print("Duplicates found:", duplicates)

find_duplicates()