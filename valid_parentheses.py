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

# The brute force way
# Runtime Complexity: O(n²)
# Space Complexity: O(1)
def isValid(s):
    """
        :type s: str
        :rtype: bool
    """
    return False
    
# Some Test cases
if __name__ == "__main__":
    s = "()"
    print("\nExample 1:")
    print("Input:", s)
    print("Output:", isValid(s))
    print("Expected: true")

    s = "()[]{}"
    print("\nExample 2:")
    print("Input:", s)
    print("Output:", isValid(s))
    print("Expected: true")
    
    s = "(]"
    print("\nExample 3:")
    print("Input:", s)
    print("Output:", isValid(s))
    print("Expected: false")
    