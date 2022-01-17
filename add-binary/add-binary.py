class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) < len(b):
            a, b = b, a
            
        n = len(a)
        b = "0" * (n - len(b)) + b
        
        res = ""
        carry = 0
        for i in range(n - 1, -1, -1):
            d1, d2 = int(a[i]), int(b[i])
            s = d1 + d2 + carry
            q, r = divmod(s, 2)
            res = str(r) + res
            carry = q
        if carry == 1:
            res = "1" + res
        return res