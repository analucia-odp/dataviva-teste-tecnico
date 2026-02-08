def get_special_print(num):
    """ This function returns "Fizz" if the number is a multiple of 3,
    "Buzz" if it's a multiple of 5, and "FizzBuzz" if it's a multiple of both 3 and 5.
    If it's not a multiple of either, it returns an empty string."""
    
    is_multiple_of_3 = (num % 3 == 0)
    is_multiple_of_5 = (num % 5 == 0)
    
    if is_multiple_of_3 and is_multiple_of_5:
        return "FizzBuzz"
    
    if is_multiple_of_3:
        return "Fizz"
    if is_multiple_of_5:
        return "Buzz"
    
    return ""

def fizz_buzz():
    for i in range(1, 101):
        special_print = get_special_print(i)
        if special_print:
            print(special_print)
        else:
            print(i)
            
fizz_buzz()