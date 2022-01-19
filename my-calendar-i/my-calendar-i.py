class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end 
        self.left = None
        self.right = None
        
    
    def insert(self, node):
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True 
            else:
                return self.left.insert(node)
        elif node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        else:
            return False 
            
            
class MyCalendar:
    def __init__(self):
        self.bookings = None

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings = TreeNode(start, end)
            return True
        else:
            return self.bookings.insert(TreeNode(start, end))
            
        