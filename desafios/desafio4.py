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

def validate_closing_parentheses(stack, char):
    # Não pode fechar se não houve abertura
    if not stack:
        return False

    last_open = stack.pop()
    return PARENTHESES_EXPECTED_CLOSING[last_open] == char
    
def validate_parentheses(s):
    """This function validates if the parentheses in the input string are correctly matched and nested."""
    stack = []
    
    for char in s:
        
        # First - If there is an opening parenthesis, there must be a corresponding closing parenthesis.
         if char in PARENTHESES_EXPECTED_CLOSING:
            stack.append(char)
        
        # Second - If there is a closing parenthesis, there must be a corresponding opening parenthesis.
         elif char in PARENTHESES_EXPECTED_OPENING:
            if not validate_closing_parentheses(stack, char):
                return "Invalid"
        
        #Last - If there is an opening parenthesis, and there is a closing parenthesis, 
        # it must appear after the opening parenthesis in the correct position.
    
    return "Valid" if not stack else "Invalid"

# Test cases
def test_validate_parenthses_simple():
    assert validate_parentheses('[]()') == "Valid"
    
def test_validate_parentheses():
    assert validate_parentheses('{[()]}') == "Valid"
    
def test_invalid_order_parentheses():
    assert validate_parentheses('{[(])}') == "Invalid"

def test_missing_closing_parentheses():
    assert validate_parentheses('{{[[(]]}}') == "Invalid"

def main_tests():
    print("Running tests...")
    print(f"Test 1: Valid parentheses simple '[]()'")
    test_validate_parenthses_simple()  # Expected output: Valid
    
    print(f"Test 2: Valid parentheses '{[()]}'")
    test_validate_parentheses()  # Expected output: Valid
    
    print(f"Test 2: Invalid order parentheses '{{[(])}}'")
    test_invalid_order_parentheses()  # Expected output: Invalid
    
    print(f"Test 3: Missing closing parentheses '{{[[(]]}}'")
    test_missing_closing_parentheses()  # Expected output: Invalid
    
    print("All tests passed.")
    
main_tests()