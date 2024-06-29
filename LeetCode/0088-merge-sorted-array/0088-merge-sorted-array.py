import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        N1 = nums1.copy()
        N2 = nums2.copy()

        while m!=0 and N1[-1] == 0:
            N1 = N1[:-1]
        if m == 0:
            N1 = []

        i = 0
        while len(N1)>0 or len(N2)>0:
            if m == 0 or len(N1) == 0:
                nums1[i] = heapq.heappop(N2)
            elif n == 0 or len(N2) == 0:
                nums1[i] = heapq.heappop(N1)
            else:
                n1 = heapq.heappop(N1)
                n2 = heapq.heappop(N2)

                if n1 < n2:
                    nums1[i] = n1
                    heapq.heappush(N2, n2)
                else:
                    nums1[i] = n2
                    heapq.heappush(N1, n1)
            i+=1
        return nums1