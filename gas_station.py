class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        if sum(gas) < sum(cost):
            return -1
        current_tank = 0
        start_index =0
        n= len(gas)

        for i in range(n):

            current_tank += gas[i] - cost[i]

            if current_tank <0:
                start_index =i+1

                current_tank =0

        return start_index
