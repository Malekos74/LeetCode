'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

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
from two_sum import twoSumHM
# The brute force way
# Runtime Complexity: O(n³)
# Space Complexity: O(3n)
def threeSumBF(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if i != j and i != k and k != j and nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    # Convert set of tuples to list of lists
    new_result = [list(sublist) for sublist in result]
    return new_result

# Faster than bruteforce
def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: Set[Tuple[int]]
    """
    result = set()
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            result.add((nums[num_dict[complement]], nums[i]))
        num_dict[num] = i
    
    return result
          
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = set()
    for i in range(len(nums)):
        # Create a copy of nums without the i'th element
        tmp_nums = nums[:]
        tmp_nums.pop(i)
        
        target = -nums[i]
        
        two_sum = twoSum(tmp_nums, target)
        
        for j, k in two_sum:
            result.add(tuple(sorted([nums[i], j, k])))

    # Convert set of tuples to list of lists
    new_result = [list(sublist) for sublist in result]
    return new_result


# Some Test cases
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print("\nExample 1:")
    print("Input:", nums)
    print("Output:", threeSum(nums))
    print("Expected: [[-1,-1,2],[-1,0,1]]")

    nums = [0,1,1]
    print("\nExample 2:")
    print("Input:", nums)
    print("Output:", threeSum(nums))
    print("Expected: []")

    nums = [0,0,0]
    print("\nExample 3:")
    print("Input:", nums)
    print("Output:", threeSum(nums))
    print("Expected: [0,0,0]")
    
    nums = [0,0,0,0]
    print("\nExample 4:")
    print("Input:", nums)
    print("Output:", threeSum(nums))
    print("Expected: [0,0,0]")
    