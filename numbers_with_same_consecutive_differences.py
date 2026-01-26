class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        result=[]

        def dfs(current_num , length):
            if length == n:
                result.append(current_num)
                return
            last_digit= current_num%10

            ## set of list
            neighbours=set([last_digit+k,last_digit-k])
            for neighbour in neighbours:

                if 0<=neighbour<=9:
                    dfs(current_num*10 + neighbour, length+1)

        for source_node in range(1,10):
            dfs(source_node,1)

        


        return result
