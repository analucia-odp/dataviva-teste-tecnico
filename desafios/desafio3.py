def count_occurrences(lst, item):
    """
    This function counts how many times 'item' appears in the list 'lst'.
    """
    count = 0
    for element in lst:
        if count > 1:
            return count
        if element == item:
            count += 1
    return count

def find_duplicates():
    """
    This function prompts the user to enter a list of numbers separated by spaces,
    and then identifies and prints the duplicate numbers from the list.
    """
    input_str = input("Enter a list of numbers separated by commas. Ex: [1, 2, 3]: ")
    clean_input = input_str.replace("[", "").replace("]", "")
    numbers = [int(i) for i in clean_input.split(",")]
    
    duplicates = []
    for num in numbers:
        # Check if the number is a duplicate and not already in the duplicates list
        if count_occurrences(numbers, num) > 1 and num not in duplicates: 
            duplicates.append(num)
    print("Duplicates found:", duplicates)

find_duplicates()