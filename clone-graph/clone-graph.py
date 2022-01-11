class Solution(object):
    def cloneGraph(self, node):   
        if node == None:
            return None
        
        visited = {node: Node(node.val)}
        q = deque([node])
        
        while len(q) > 0:
            curr = q.popleft()
            
            for neigh in curr.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val)
                    q.append(neigh)
                
                visited[curr].neighbors.append(visited[neigh])
                
        return visited[node]

            
            