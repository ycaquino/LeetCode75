'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Ex. 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Ex.2
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Ex.3
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''


class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        if nums:
            result = [nums[0]]
            for i in range(1, len(nums)):
                result.append(result[i-1] + nums[i])
            return result
        else:
            return None