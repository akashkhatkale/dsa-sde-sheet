class Solution(object):
    def pivotIndex(self, nums):
        sum_left = 0
        sum_right = sum(nums)
        
        for i in range(len(nums)):
            sum_left += nums[i]
            if sum_left == sum_right:
                return i 
            sum_right -= nums[i]
            
            
        return -1 