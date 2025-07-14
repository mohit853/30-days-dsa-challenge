class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        ## 2 pointers start & end + sliding window 

        start=0
        end=0
        s_dict={}
        max_length=0
        n=len(s)
        while end<n:
            ch=s[end]
            if ch not in s_dict:
                s_dict[ch]=1
            else:
                s_dict[ch]+=1
            
            while s_dict[ch] == 3:
                s_dict[s[start]] -=1
                start+=1
            max_length = max(max_length,end-start +1)
            end+=1
        
        return max_length
            

        
