def is_palindrome(word):
    """ Check if the string 's' is a palindrome., 
    ignoring case differences. """
    cleaned_s = word.lower()  # Normalize for minuscule
    i = 0
    j = len(cleaned_s) - 1
    while i < j:
        if cleaned_s[i] != cleaned_s[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    while True:
        word = input("Enter a word to check if it's a palindrome (or 'quit' to exit): ")
        if word.lower() == "quit":
            break
        print(is_palindrome(word))

main()