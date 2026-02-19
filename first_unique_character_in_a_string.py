class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        s_map ={}
        
        for ch in s:
            if ch not in s_map:
                s_map[ch] =1
            else:
                s_map[ch] +=1
        
        n = len(s)
        for i in range(n):
            
            ch = s[i]
            if s_map[ch] ==1:
                return i
        return -1
        
