# Moore's Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1 
        
        for i in nums:
            if i == majority:
                count += 1 
            else:
                count -= 1
                
            if count == 0:
                majority = i 
                count = 1 
                
                
        return majority 