class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]
            
        left = 1 
        right = len(nums) - 2
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid % 2 == 1:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1 
                else:
                    right = mid - 1 
                    
            else:
                if nums[mid] == nums[mid+1]:
                    left = mid + 1 
                else:
                    right = mid - 1
        
        return nums[left]
            
        