class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        result = []
        n = len(candidates)
        
        def dfs(i, current, sub):
            if current == target:
                result.append(sub.copy())
                return
            
            if i >= n or current > target:
                return 
            
            sub.append(candidates[i])
            dfs(i, current + candidates[i], sub)
            sub.pop()
            dfs(i+1, current, sub)
            
        
        dfs(0, 0, [])
        
        return result