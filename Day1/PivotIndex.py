'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of
all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Ex. 1:
Input: nums = [1,7,3,6,5,6]
Output: 3

Ex.2
Input: nums = [1,2,3]
Output: -1

Ex.3
Input: nums = [2,1,-1]
Output: 0

Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''


class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        left, rigth = None, None
        for i in range(len(nums)):
            if i == 0:
                left = 0
                rigth = sum(nums[i+1:])
            elif i == len(nums) - 1:
                left = sum(nums[:i])
                rigth = 0
            else:
                left = sum(nums[0:i])
                rigth = sum(nums[i+1:])
            if left == rigth:
                return i
        return -1