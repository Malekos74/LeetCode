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
    
    '''
      # Loop through the List[str] and group them 2 by 2
    # for i in range (len(strs)):
    #     for j in range (i + 1, len(strs)):
    #         if isAnagram(strs[i], strs[j]):
    #             exists = False
                
    #             for k in range(len(tmp)):
    #                 if [strs[i], strs[j]] in tmp[k]:
    #                     exists = True
    #                     break
    #                 elif strs[i] in tmp[k]:
    #                     tmp[k].append(strs[j])
    #                     exists = True
    #                     break
    #                 elif strs[j] in tmp[k]:
    #                     tmp[k].append(strs[i])
    #                     exists = True
    #                     break
                    
    #             if not exists: tmp.append([strs[i], strs[j]])
                
    #         else:
    #             exists = False
                
    #             for k in range(len(tmp)): 
    #                 if strs[i] in tmp[k]:
    #                     exists = True
    #                     break
                
    #             if not exists: tmp.append([strs[i]])
    '''
    tmp = []
    
    # If input contains only one string, then return that string ina List[List[str]]
    if len(strs) == 1:
        return [[strs[0]]]
    
    # Loop through the List[str] and group them
    for i in range(len(strs)):
        found = False
        for group in tmp:
            if isAnagram(strs[i], group[0]):
                group.append(strs[i])
                found = True
                break
        if not found:
            tmp.append([strs[i]])
    
    # If tmp is empty, return [['']]
    if len(tmp) == 0: return [['']]
    
    
    return tmp
    
def groupAnagramsOptimized(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
    
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        return list(anagrams.values())
                
def isAnagram(s, t):
    return sorted(s) == sorted(t)

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