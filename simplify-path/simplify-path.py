class Solution(object):
    def simplifyPath(self, path):       
        ans = []
        cur = ""
        
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if ans:
                        ans.pop()
                elif cur != "" and cur != ".":
                    ans.append(cur)
                cur = ""
            else:
                cur += c 
                
        return "/" + "/".join(ans)
        
                
        
        
