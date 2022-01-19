class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:   
        res = []
        
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)
            
            
        dfs(0, [])
        
        return (res)