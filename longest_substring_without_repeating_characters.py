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

# The brute force way
def lengthOfLongestSubstringBF(s):
    """
        :type s: str
        :rtype: int
    """
    max_len = 0
    tmp = 0
    reset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    
    usable = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    
    for x in s:
        try:
            usable.remove(x)
            tmp += 1
            if tmp > max_len: max_len = tmp

        except ValueError:
            tmp = 0
            usable = reset
            
    return max_len
# Some Test cases
if __name__ == "__main__":
    s = "abcabcbb"
    print("Example 1:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstringBF(s))
    print("Expected: 3\n")
    
    s = "bbbbb"
    print("Example 2:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstringBF(s))
    print("Expected: 1\n")
    
    s = "pwwkew"
    print("Example 3:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstringBF(s))
    print("Expected: 3\n")
    