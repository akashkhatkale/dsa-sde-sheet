class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0 
        index = 0 
        result = 0 
        
        while index < len(nums):
            if count == 0:
                nums[result] = nums[index]
                result += 1
            
            if index < len(nums) - 1 and nums[index] == nums[index+1]:
                count += 1 
                
            if index < len(nums) - 1 and nums[index] != nums[index+1]:
                count = 0 
                
            index += 1 
            
        return result
            
        