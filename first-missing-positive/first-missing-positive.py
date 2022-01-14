class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                
        
        for i in range(len(nums)):
            index = abs(nums[i])
            if index >= 1 and index <= len(nums):
                if nums[index-1] > 0:
                    nums[index-1] *= -1 
                elif nums[index-1] == 0:
                    nums[index-1] = -1 * (len(nums)+1)            
        
        for i in range(1, len(nums)+1):
            index = i - 1 
            if nums[index] >= 0:
                return i
            
        return len(nums)+1