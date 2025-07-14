class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        results = []

        ## start from 1 try till 9

        ## start from base cases
        def backtrack(ream_sum, comb, next_start):

            if ream_sum == 0 and len(comb) == k:
                return results.append(list(comb))
            elif ream_sum < 0 or len(comb) > k:
                return

            ### build the comb list

            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(ream_sum - (i + 1), comb, i+1)
                comb.pop()

        backtrack(n, [], 0)

        return results

