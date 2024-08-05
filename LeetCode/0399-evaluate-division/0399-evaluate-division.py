class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def clean_input(list1, list2):
            for l in list1:
                if l in list2:
                    list1.remove(l)
                    list2.remove(l)
            return list1, list2


        result = [-1]*len(queries)

        for i in range(len(equations)):
            if equations[i] in queries:
                idx = queries.index(equations[i])
                result[idx] = values[i]

        nums = {}
        for i in range(len(equations)):
            w1,w2 = clean_input(list(equations[i][0]), list(equations[i][1])) 
            value = values[i] #w1/w2=value

            if len(w1) == 1 and len(w2) == 0:
                nums[w1[0]] = value
                break
            elif len(w1) == 0 and len(w2) == 1:
                nums[w2[0]] = 1/value
                break


            if len(nums) == 0:
                nums[w2[0]] = 1

            for n in range(len(w1)):
                if w1[n] in nums and w2[n] in nums:
                    pass
                elif not w1[n] in nums and w2[n] in nums:
                    w1_v = nums[w2[n]]*value
                    nums[w1[n]] = w1_v
                elif w1[n] in nums and not w2[n] in nums:
                    w2_v = nums[w1[n]]/value
                    nums[w2[n]] = w2_v
                else:
                    nums[w2[n]] = 1
                    w1_v = nums[w2[n]]*value
                    nums[w1[n]] = w1_v

        print(nums)
        for j in range(len(queries)):
            if result[j] == -1:
                w1 = list(queries[j][0])
                w2 = list(queries[j][1])

                v1 = 1
                v2 = 1
                for w1_ in w1:
                    if w1_ in nums:
                        v1*=nums[w1_]
                    else:
                        v1 = 0

                for w2_ in w2:
                    if w2_ in nums:
                        v2*=nums[w2_]
                    else:
                        v2 = 0

                if v1 != 0 and v2 != 0:
                    result[j] = v1/v2

        return result