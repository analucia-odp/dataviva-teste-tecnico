PARENTHESES_EXPECTED_CLOSING = {
    '(': ')',
    '{': '}',
    '[': ']'
}

PARENTHESES_EXPECTED_OPENING = {
    ')': '(',
    '}': '{',
    ']': '['
}

def validate_closing_parentheses(s, char):
    expected_closing = PARENTHESES_EXPECTED_CLOSING.get(char)
    if expected_closing and expected_closing not in s:
        return False
    return True

def validate_opening_parentheses(s, char):
    expected_open = PARENTHESES_EXPECTED_CLOSING.get(char)
    if expected_open and expected_open not in s:
        return False
    return True
    
def validate_parentheses(s):
    """This function validates if the parentheses in the input string are correctly matched and nested."""
    tam = len(s) - 1
    
    for char in s:
        
        # First - If there is an opening parenthesis, there must be a corresponding closing parenthesis.
        if not validate_closing_parentheses(s, char):
            return "Invalid"
        
        # Second - If there is a closing parenthesis, there must be a corresponding opening parenthesis.
        if not validate_opening_parentheses(s, char):
            return "Invalid"
        
        #Last - If there is an opening parenthesis, and there is a closing parenthesis, 
        # it must appear after the opening parenthesis in the correct position.
        index = s.index(char)
        validate = s[tam - index]
        expected_closing = PARENTHESES_EXPECTED_CLOSING.get(char)
        if expected_closing and validate != expected_closing:
            return "Invalid"
    
    return "Valid"

# Test cases
def test_validate_parentheses():
    assert validate_parentheses('{[()]}') == "Valid"
    
def test_invalid_order_parentheses():
    assert validate_parentheses('{[(])}') == "Invalid"

def test_missing_closing_parentheses():
    assert validate_parentheses('{{[[(]]}}') == "Invalid"

def main_tests():
    print("Running tests...")
    print(f"Test 1: Valid parentheses '{[()]}'")
    test_validate_parentheses()  # Expected output: Valid
    print(f"Test 2: Invalid order parentheses '{{[(])}}'")
    test_invalid_order_parentheses()  # Expected output: Invalid
    print(f"Test 3: Missing closing parentheses '{{[[(]]}}'")
    test_missing_closing_parentheses()  # Expected output: Invalid
    
    print("All tests passed.")
    
main_tests()