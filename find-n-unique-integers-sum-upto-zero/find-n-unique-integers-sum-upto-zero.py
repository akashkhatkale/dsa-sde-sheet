class Solution(object):
    def sumZero(self, n):
        isEven = n % 2 == 0
        left = 0 
        num = -(n // 2) 
        res = []

        while left < n:
            res.append(num)
            if num == -1 and isEven:
                num += 2 
            else:
                num += 1 
            left += 1 

        return res  
        
        
        