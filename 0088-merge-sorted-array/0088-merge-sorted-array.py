import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        N1 = [x for x in nums1 if not x == 0]
        N2 = [x for x in nums2 if not x == 0]
        i = 0

        while len(N1)>0 or len(N2)>0:
            if len(N1) == 0:
                n2 = heapq.heappop(N2)
                nums1[i] = n2
            elif len(N2) == 0:
                n1 = heapq.heappop(N1)
                nums1[i] = n1
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