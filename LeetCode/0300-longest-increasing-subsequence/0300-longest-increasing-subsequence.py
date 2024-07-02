class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize an empty list to store the end elements of the increasing subsequences
        lis = []
        
        for num in nums:
            # Find the index where the number would fit in the current LIS array
            index = bisect_left(lis, num)
            
            # If the index is equal to the length of the LIS array, append the number
            if index == len(lis):
                lis.append(num)
            else:
                # Replace the element at the found index with the current number
                lis[index] = num
 
        return len(lis)
    
    """def lengthOfLIS2(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # 이진 탐색을 수행하는 헬퍼 함수
        def binary_search(sub, val):
            print(f'binary_search(sub:{sub},val:{val})')
            low, high = 0, len(sub) - 1
            while low <= high:
                print(f'    low{low} / high{high}')
                mid = (low + high) // 2
                print(f'    mid:{mid} / val:{val}')
                if sub[mid] < val:
                    low = mid + 1
                    print(f'    low = {low}')
                else:
                    high = mid - 1
                    print(f'    high = {high}')
            print(f'        return low({low})')
            return low
        
        # LIS를 추적하는 리스트
        sub = []
        
        for num in nums:
            pos = binary_search(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        
        return len(sub)"""