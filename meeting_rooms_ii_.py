class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        start = sorted( [intervals[i][0] for i in range(n)])
        end = sorted( [intervals[i][1] for i in range(n)])
        
        i =0 
        j=0
        cnt =0
        
        while i<n:
            if end[j] > start[i]:
                cnt+=1
            else:
                j+=1
            i+=1
        
        
        
        return cnt
        
        
        
        
