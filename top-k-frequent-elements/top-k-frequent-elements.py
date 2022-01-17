class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
            
        arr1 = []
        for i in d:
            temp =[d[i], i]        
            arr1.append(temp)
        
        heapq._heapify_max(arr1)

        ans = []
        for i in range(k):
            ans.append(heapq._heappop_max(arr1)[1])
            
        return ans
        