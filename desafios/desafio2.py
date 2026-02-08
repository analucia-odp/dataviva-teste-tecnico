def is_palindrome(word):
    """ Check if the string 's' is a palindrome., 
    ignoring case differences. """
    cleaned_s = word.lower()  # Normalize for minuscule
    return cleaned_s == cleaned_s[::-1] 

def main():
    while True:
        word = input("Enter a word to check if it's a palindrome (or 'quit' to exit): ")
        if word.lower() == "quit":
            break
        print(is_palindrome(word))

main()