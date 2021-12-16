class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)   
        
        # first iteration
        left = 0 
        right = len(nums) - 1 
        while left < right:
            self.swap(left,right,nums)
            left += 1
            right -= 1 
            
        # second iteration
        left = 0 
        right = k - 1 
        while left < right:
            self.swap(left, right, nums)
            left += 1
            right -= 1 
            
        # third iteration
        left = k 
        right = len(nums) - 1 
        while left < right:
            self.swap(left, right, nums)
            left += 1 
            right -= 1 
            
            
    def swap(self, left, right, nums):
        nums[left], nums[right] = nums[right], nums[left]
        
        
            