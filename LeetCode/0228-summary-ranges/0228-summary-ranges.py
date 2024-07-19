class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        output = []
        x = [nums[0]]
        for i in range(1,len(nums)):
            n = nums[i]

            if i == (len(nums)-1):
                if x[-1]+1 == n:
                    output.append(f'{x[0]}->{n}')
                else:
                    if len(x) == 1:
                        output.append(f'{x[0]}')
                    else:
                        output.append(f'{x[0]}->{x[-1]}')
                    output.append(f'{n}')
            else:
                if not x or (x[-1]+1) == n:
                    x.append(n)
                else:
                    if len(x) == 1:
                        output.append(f'{x[0]}')
                    else:
                        output.append(f'{x[0]}->{x[-1]}')
                    x = [n]
        return output