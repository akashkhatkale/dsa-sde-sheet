class Solution(object):
    def largestNumber(self, nums):        
        for i in range(len(nums)):
            j = i + 1
            
            while i < len(nums) and j < len(nums):
                ij = str(nums[i]) + str(nums[j])
                ji = str(nums[j]) + str(nums[i])
                
                if int(ij) < int(ji):
                    nums[j], nums[i] = nums[i], nums[j]
                
                j += 1 
                
        res = "".join(map(str, nums))
        
        return "0" if int(res) == 0 else res