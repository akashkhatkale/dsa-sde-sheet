class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums) - 1 
        left = 0 
        right = len(nums) - 1 
        while left <= right:
            m = max(abs(nums[left]), abs(nums[right]))
            if m == abs(nums[right]):
                res = [nums[right] * nums[right]] + res
                right -= 1 
            else:
                res = [nums[left] * nums[left]] + res
                left += 1
            
        return res