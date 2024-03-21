'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''
import string

def groupAnagrams(strs):
    """
        :type strs: List[str]
        :rtype: List[List[str]]
    """
    

def isAnagram(s, t):
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
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
        
    ]

    for idx, (strs, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", strs)
        print("Output:", groupAnagrams(strs))
        print("Expected:", expected)