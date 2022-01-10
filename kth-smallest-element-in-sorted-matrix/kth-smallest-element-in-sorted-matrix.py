class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:    
        heap = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heap.append(matrix[row][col])
                
        heapq.heapify(heap)
        
        i = 1
        
        while 1:
            elem = heapq.heappop(heap)
            if i == k:
                return elem
            i += 1
        
        