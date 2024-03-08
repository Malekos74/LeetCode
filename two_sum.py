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

'''


def twoSumBF(nums, target):
    for i in range (len(nums)):
        for k in range(i + 1, len(nums)):
            tmp = nums[i] + nums[k]
            if tmp == target: return [i, k]    


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Example 1:")
    print("Input:", nums1, target1)
    print("Output:", twoSumBF(nums1, target1))

    nums2 = [3, 2, 4]
    target2 = 6
    print("\nExample 2:")
    print("Input:", nums2, target2)
    print("Output:", twoSumBF(nums2, target2))

    nums3 = [3, 3]
    target3 = 6
    print("\nExample 3:")
    print("Input:", nums3, target3)
    print("Output:", twoSumBF(nums3, target3))
    