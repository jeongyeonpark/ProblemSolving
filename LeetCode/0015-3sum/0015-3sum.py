class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)

        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        if len(z) >= 3:
            res.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()

#         pos = []
#         zero = []
#         neg = []
#         for num in nums:
#             if num>0:
#                 pos.append(num)
#             elif num < 0:
#                 neg.append(num)
#             else:
#                 zero.append(num)

#         POS = set(pos)
#         NEG = set(neg)
#         if zero:
#             for P in POS:
#                 if -1*P in NEG:
#                     res.add((-1*P, 0, P))

#         if len(zero)>2:
#             res.add((0,0,0))

#         for i in range(len(pos)):
#             for j in range(i+1,len(pos)):
#                 x = -1*(pos[i]+pos[j]) 
#                 if x in neg:
#                     res.add(tuple(sorted([x, pos[i], pos[j]])))

#         for i in range(len(neg)):
#             for j in range(i+1,len(neg)):
#                 x = -1*(neg[i]+neg[j])
#                 if x in pos:
#                     res.add(tuple(sorted([x, neg[i], neg[j]])))

#         return res