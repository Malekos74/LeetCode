'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
'''

# The brute force way
# Runtime Complexity: O(n³)
# Space Complexity: O(1)
def threeSumBF(nums):
    """
        :type nums: List[int]
        :rtype: List[List[int]]
    """
    result = []
    for i in range (0, len(nums)):
        for j in range (i + 1, len(nums)):
            for k in range (j + 1, len(nums)):
                if i != j and i != k and k != j and nums[i] + nums[j] + nums[k] == 0 : 
                    result.append([nums[i], nums[j], nums[k]])
    
    # Convert list of lists to set of tuples to remove duplicates
    new_result = set(tuple(sorted(sublist)) for sublist in result)
    # Convert set of tuples back to list of lists
    new_result = [list(sublist) for sublist in new_result]
    return new_result
    
# Some Test cases
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print("Example 1:")
    print("Input:", nums)
    print("Output:", threeSumBF(nums))
    print("Expected: [[-1,-1,2],[-1,0,1]]")

    nums = [0,1,1]
    print("Example 2:")
    print("Input:", nums)
    print("Output:", threeSumBF(nums))
    print("Expected: []")

    nums = [0,0,0]
    print("Example 3:")
    print("Input:", nums)
    print("Output:", threeSumBF(nums))
    print("Expected: [0,0,0]")
    
    nums = [0,0,0,0]
    print("Example 4:")
    print("Input:", nums)
    print("Output:", threeSumBF(nums))
    print("Expected: [0,0,0]")
    