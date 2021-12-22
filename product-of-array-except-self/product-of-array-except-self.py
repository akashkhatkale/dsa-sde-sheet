class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
	
        prefix = 1 
        for i in range(len(nums)):
            result[i] = prefix 
            prefix *= nums[i]
            
        postfix = 1 
        for i in reversed(range(len(nums))):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result