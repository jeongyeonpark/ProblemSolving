from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = [-1]*len(queries)
        nums = {}
        for i in range(len(equations)):
            num1 = equations[i][0]
            num2 = equations[i][1]
            val = values[i]

            if not num1 in nums:
                nums[num1] = {}
            if not num2 in nums:
                nums[num2] = {}
                
            nums[num1][num2] = val
            nums[num1][num1] = 1
            nums[num2][num1] = 1/val
            nums[num2][num2] = 1

            for key,item in nums.items():
                if num1 in item and key != num2:
                    nums[key][num2] = nums[key][num1]*val
                if num2 in item and key != num1:
                    nums[key][num1] = nums[key][num2]*(1/val)
      
        print(nums)
        for i,query in enumerate(queries):
            if not query[0] in nums or not query[1] in nums:
                pass
            elif query[0] in nums and query[1] in nums[query[0]]:
                result[i] = nums[query[0]][query[1]]
            elif query[1] in nums and query[0] in nums[query[1]]:
                result[i] = 1/nums[query[1]][query[0]]
            else:
                num1_item = [x[0] for x in nums[query[0]].items()]
                num2_item = [x[0] for x in nums[query[1]].items()]

                nn = 0
                for n1 in num1_item:
                    if n1 in num2_item:
                        result[i] = (1/nums[query[1]][n1]) * (nums[query[0]][n1])
                        nn=1
                        break
                if nn == 0:
                    for n1 in num1_item:
                        if n1 != query[0]:
                            n_items = [x[0] for x in nums[n1].items()]
                            if query[1] in n_items:
                                result[i] = nums[query[0]][n1]*nums[n1][query[1]]
                                break
                    if nn == 0:
                        for n2 in num2_item:
                            if n2 != query[1]:
                                n_items = [x[0] for x in nums[n2].items()]
                                if query[0] in n_items:
                                    result[i] = 1/(nums[query[1]][n2]*nums[n2][query[0]])
                                    break

                            

        return result

    # def dfs(self, node: str, dest: str, gr: dict, vis: set, ans: List[float], temp: float) -> None:
    #     if node in vis:
    #         return

    #     vis.add(node)
    #     if node == dest:
    #         ans[0] = temp
    #         return

    #     for ne, val in gr[node].items():
    #         self.dfs(ne, dest, gr, vis, ans, temp * val)

    # def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
    #     gr = {}

    #     for i in range(len(equations)):
    #         dividend, divisor = equations[i]
    #         value = values[i]

    #         if dividend not in gr:
    #             gr[dividend] = {}
    #         if divisor not in gr:
    #             gr[divisor] = {}

    #         gr[dividend][divisor] = value
    #         gr[divisor][dividend] = 1.0 / value

    #     return gr

    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #     gr = self.buildGraph(equations, values)

    #     finalAns = []

    #     for query in queries:
    #         dividend, divisor = query

    #         if dividend not in gr or divisor not in gr:
    #             finalAns.append(-1.0)
    #         else:
    #             vis = set()
    #             ans = [-1.0]
    #             temp = 1.0
    #             self.dfs(dividend, divisor, gr, vis, ans, temp)
    #             finalAns.append(ans[0])

    #     return finalAns