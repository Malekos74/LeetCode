'''
Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.

'''

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
    
    

# Some Test cases
if __name__ == "__main__":
    s = "abcabcbb"
    print("Example 1:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstring(s))
    print("Expected: 3")
    
    s = "bbbbb"
    print("Example 2:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstring(s))
    print("Expected: 1")
    
    s = "pwwkew"
    print("Example 3:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstring(s))
    print("Expected: 3")
    