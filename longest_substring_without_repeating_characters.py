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
def lengthOfLongestSubstring(s):
    max_len = 0
    tmp = 0
    # Dict with keys as the characters of s and values as the position in s
    used = {}
    # Tells us which characters we need in the dict
    start_index = 0
    
    for i in range(len(s)):
        if s[i] in used and used[s[i]] >= start_index:
            max_len = max(max_len, tmp)
            tmp = i - used[s[i]]
            start_index = used[s[i]] + 1
        else:
            tmp += 1
        
        used[s[i]] = i

    return max(max_len, tmp)


# Some Test cases
if __name__ == "__main__":
    s = "abcabcbb"
    print("Example 1:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstring(s))
    print("Expected: 3\n")
    
    s = "bbbbb"
    print("Example 2:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstring(s))
    print("Expected: 1\n")
    
    s = "pwwkew"
    print("Example 3:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstring(s))
    print("Expected: 3\n")
    
    s = "dvdf"
    print("Example 4:")
    print("Input:", s)
    print("Output:", lengthOfLongestSubstring(s))
    print("Expected: 3\n")
    