'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 10^34
s consists of parentheses only '()[]{}'.
'''
import random

def generate_brackets_string():
    brackets = ['(', ')', '{', '}', '[', ']']
    num_brackets = random.randint(1, 20)  # You can adjust the range of the random number of brackets generated
    brackets_string = ''.join(random.choices(brackets, k=num_brackets))
    return brackets_string

# ([)})[])[
def isValid(s):
    """
        :type s: str
        :rtype: bool
    """
    stack = []
    
    for c in s:
        match c:
            case '(' | '[' | '{':
                stack.append(c)
            case ')':
                if len(stack) == 0 or stack[-1] != '(': return False
                else: stack.pop()
            case ']':
                if len(stack) == 0 or stack[-1] != '[': return False
                else: stack.pop()
            case '}':
                if len(stack) == 0 or stack[-1] != '{': return False
                else: stack.pop()
    
    return len(stack) == 0
    
# Some Test cases
if __name__ == "__main__":
    
    s = "()"
    print("\nExample 1:")
    print("Input:", s)
    print("Output:", isValid(s))
    print("Expected: True")

    s = "()[]{}"
    print("\nExample 2:")
    print("Input:", s)
    print("Output:", isValid(s))
    print("Expected: True")
    
    s = "(]"
    print("\nExample 3:")
    print("Input:", s)
    print("Output:", isValid(s))
    print("Expected: False")
    
    # Invalid examples
    invalid_strings = [
        ("({})[", False),  
        ("[(])", False),   
        ("{[}", False),    
        ("{[()]}", True), 
        ("([{}))", False), 
        ("{[()]", False),  
    ]

    for idx, (s, expected) in enumerate(invalid_strings, start=3):
        print("\nExample", idx, ":")
        print("Input:", s)
        print("Output:", isValid(s))
        print("Expected:", expected)