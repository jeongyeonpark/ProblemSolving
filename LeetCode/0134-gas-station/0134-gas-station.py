class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_sum = 0
        total_sum = 0 
        start_idx = -1
        i = 0
        while i < len(gas):
            #print(f'stat: {i}')
            curr_sum = 0
            if gas[i]-cost[i] >= 0:
                curr_sum += gas[i]-cost[i]
                start_idx = i
                i+=1
                while i < len(gas) and curr_sum+gas[i]-cost[i] >= 0 :
                    #print(f'pos while : {i}')
                    curr_sum += gas[i]-cost[i]
                    #print(f'pos curr_sum : {curr_sum}')
                    i+=1
                total_sum+=curr_sum
            else:
                curr_sum += gas[i]-cost[i]
                i+=1
                while i < len(gas) and gas[i]-cost[i] < 0 :
                    #print(f'neg while : {i}')
                    curr_sum += gas[i]-cost[i]
                    #print(f'neg sum : {curr_sum}')
                    i+=1
                total_sum+=curr_sum
        if total_sum < 0:
            return -1
        return start_idx