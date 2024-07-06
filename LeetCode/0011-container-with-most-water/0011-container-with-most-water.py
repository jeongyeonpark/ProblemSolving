class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for idx in range(len(height)):
            n = height[idx]
            for idx2 in range(len(height)-1,idx,-1):
                
                if n <= height[idx2]:
                    area = min(n, height[idx2])*(idx2-idx)
                    if area > max_area:
                        max_area = area
                    break

        for idx in range(len(height)-1,0,-1):
            n = height[idx]
            for idx2 in range(0, idx):

                if n <= height[idx2]:
                    area = min(n, height[idx2])*(idx-idx2)
                    if area > max_area:
                        max_area = area
                    break
        print(max_area)
        return max_area