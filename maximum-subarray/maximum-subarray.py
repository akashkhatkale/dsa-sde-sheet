# https://leetcode.com/problems/maximum-subarray/
# Solve using Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # declare variable to hold maximum
        maximum = nums[0]
        
        # declare variable to hold current maximum
        current_max = maximum 
        
        for i in range(1, len(nums)):
            # set current max variable
            current_max = max(nums[i], current_max + nums[i])
            
            # set maximum variable
            maximum = max(maximum, current_max)
            
        return maximum
        