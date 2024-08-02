class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_sum = 0 
        start_idx = -1
        i = 0
        while i < len(gas):
            curr_sum = gas[i]-cost[i]
            i+=1
            if curr_sum >= 0:
                start_idx=i-1
                while i < len(gas) and curr_sum+gas[i]-cost[i] >= 0 :
                    curr_sum += gas[i]-cost[i]
                    i+=1
            else:
                while i < len(gas) and gas[i]-cost[i] < 0 :
                    curr_sum += gas[i]-cost[i]
                    i+=1
            total_sum+=curr_sum

        return start_idx if total_sum >= 0 else -1