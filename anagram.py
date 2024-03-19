'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
import string

def isAnagram(s, t):
    # Initialize 2 dicts with the alphabet as keys and 0 as values
    alphabet = string.ascii_lowercase
    dict1 = {x : 0 for x in alphabet}
    dict2 = {x : 0 for x in alphabet}
    
    for x in s:
        dict1[x] += 1
    for x in t:
        dict2[x] += 1
        
    return dict1 == dict2

def isAnagramOptimized(s, t):
    if len(s) != len(t):
        return False

    dict = {x: 0 for x in string.ascii_lowercase}

    for x in s:
        dict[x] += 1

    for x in t:
        dict[x] -= 1
        if dict[x] < 0:
            return False

    return True

# Some Test cases
if __name__ == "__main__":
    
    # Examples
    input = [
        ('anagram', 'nagaram', True),
        ('rat', 'car', False)
    ]

    for idx, (s, t, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", s, " ", t)
        print("Output:", isAnagram(s, t))
        print("Expected:", expected)