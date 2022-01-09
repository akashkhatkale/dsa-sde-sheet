class Solution:
    def canPartition(self, nums: List[int]) -> bool:     
        s = sum(nums)
        if s % 2 == 1:
            return False 
        
        dp = [-1] * (s//2 + 1)
        
        def dfs(i, sum):
            if sum < 0:
                return False
            
            if i == len(nums):
                return sum == 0
            
            if dp[sum] != -1:
                return dp[sum]
            
            # pick
            pick = dfs(i+1, sum - nums[i])
            
            # non pick
            noPick = dfs(i+1, sum)
                      
            dp[sum] = pick or noPick
            
            return pick or noPick
        
        
        return dfs(0, s//2)
            
            