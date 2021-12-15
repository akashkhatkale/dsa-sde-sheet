# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialise a dictionary
        seen = {}
        
        for index, item in enumerate(nums):
            # calculate the difference
            diff = target - item
            
            if diff in seen:
                # if the difference is in the seen, return it
                return [seen[diff], index]
            else:
                # if not, set it 
                seen[item] = index
                
        return []
    
    
