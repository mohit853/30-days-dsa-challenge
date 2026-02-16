class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            current = intervals[i]
            curr_start = current[0]
            curr_end = current[1]
            
            if res[-1][1] >= curr_start:
                res[-1][1] = max(curr_end,res[-1][1])
            else:
                res.append(current)
        return res
            
            
