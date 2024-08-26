class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heap = []
        for n in nums:
            heapq.heappush(heap, n)

        max_n = 1
        n = heapq.heappop(heap)
        curr_n = [n]

        while heap:
            n = heapq.heappop(heap)
            if len(curr_n) == 0:
                curr_n.append(n)
            else:
                if curr_n[-1] == n:
                    pass
                elif curr_n[-1]+1 == n:
                    curr_n.append(n)
                    if len(curr_n) > max_n:
                        max_n = len(curr_n)
                else:
                    curr_n = [n]

        return max_n