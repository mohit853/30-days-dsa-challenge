class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ## if list is in decreasing Order ,initilze it  
        n= len(temperatures)
        answer =[0]*n
        stack=[]
        for i,curr_temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = i -prev_day

            stack.append(i)
        return answer

        
        
