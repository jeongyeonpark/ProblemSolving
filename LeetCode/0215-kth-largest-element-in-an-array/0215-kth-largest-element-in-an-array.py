class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)

        i = 0
        while len(nums)-k != i:
            heapq.heappop(heap)
            i+=1

        return heapq.heappop(heap)