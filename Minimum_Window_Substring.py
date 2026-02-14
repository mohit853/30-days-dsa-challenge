class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        map_t = Counter(t)
        
        grp_unqiue_char = len(map_t)
        
        window = {}
        res = [-1,-1]
        resLen = float('inf')
        
        left =0
        
        curr_grp_count =0
        for right in range(len(s)):
            
            char_right = s[right]
            
            if char_right not in window:
                window[char_right] =1
            else:
                window[char_right] +=1
            
            ## if grp of char_right is done in map_t
            
            if char_right in map_t and window[char_right] == map_t[char_right]:
                curr_grp_count+=1
            
            ## once all groups of map_t are done , minimize window
            
            while curr_grp_count == grp_unqiue_char :
                
                window_len = right -left +1
                if window_len < resLen:
                    resLen = window_len
                    res = [left,right]
                s_left = s[left]
                window[s_left] -=1
                
                
                ## conidtion to break shortening of window
                if s_left in map_t and window[s_left] < map_t[s_left]:
                    curr_grp_count  -=1
                
                left+=1
        
        l,r= res
        return s[l:r+1] if resLen != float('inf') else ""
                
            
            
                
        
