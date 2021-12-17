class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1 
            elif count > 0 :
                self.swap(i - count, i, nums)
    
        
    def swap(self,a,b,nums):
        nums[a], nums[b] = nums[b], nums[a]