class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        
        for i, ch in enumerate(s):
            if ch not in chars:
                chars[ch] =  i
            else:
                chars[ch] = -1
                        
        mini = float("inf")
        for d in chars.values():
            if d != -1:
                mini = min(mini, d)

        return -1 if mini == float("inf") else mini