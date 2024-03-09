'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''

# The brute force way
# Runtime Complexity: O(n²)
# Space Complexity: O(1)
def twoSumBF(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    for i in range (len(nums)):
        for k in range(i + 1, len(nums)):
            tmp = nums[i] + nums[k]
            if tmp == target: return [i, k]    
            
# The hashmap way
# Runtime Complexity: O(n)
# Space Complexity: O(n)
def twoSumHM(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    

# Some Test cases
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Example 1:")
    print("Input:", nums, target)
    print("Output:", twoSumBF(nums, target))
    print("Expected: [0, 1]")

    nums = [3, 2, 4]
    target = 6
    print("\nExample 2:")
    print("Input:", nums, target)
    print("Output:", twoSumBF(nums, target))
    print("Expected: [1, 2]")

    nums = [3, 3]
    target = 6
    print("\nExample 3:")
    print("Input:", nums, target)
    print("Output:", twoSumBF(nums, target))
    print("Expected: [0, 1]")
    