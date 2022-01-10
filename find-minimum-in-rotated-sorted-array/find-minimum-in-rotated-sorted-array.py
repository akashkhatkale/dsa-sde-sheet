class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0 
        right = len(nums) - 1
        
        
        while left < right:
            mid = left + (right-left)//2
            
            if nums[mid] >= nums[right]:
                left = mid + 1
                
            elif nums[mid] <= nums[right]:
                right = mid
            
        return nums[right]
    

    
    