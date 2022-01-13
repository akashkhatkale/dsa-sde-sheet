class TrieNode:
    def __init__(self):
        self.children = {}
        self.endsWith = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
            
        cur.endsWith = True 
     
    

    def search(self, word: str) -> bool:
        cur = self.root
        
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False 
            
        return cur.endsWith 
        
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for w in prefix:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False 
            
        return True 
        