class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = set()

        p, z, n = [], [], []
        for num in nums:
            if num>0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        P, N = set(p), set(n)
        if z:
            for num in P:
                if -1*num in N:
                    r.add((-1*num, 0, num))

        if len(z)>=3:
            r.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                x = -1*(n[i]+n[j])
                if x in P: #find set
                    r.add(tuple(sorted([x, n[i], n[j]])))

        for i in range(len(p)):
            for j in range(i+1,len(p)):
                x = -1*(p[i]+p[j]) 
                if x in N:#find set
                    r.add(tuple(sorted([x, p[i], p[j]])))

        return r