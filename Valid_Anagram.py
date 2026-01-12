class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict ={}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch not in s_dict:
                s_dict[ch]=1
            else:
                s_dict[ch]+=1
        
        for ch in t:

            if ch not in s_dict or s_dict[ch] ==0 :
                return False
            
            s_dict[ch]-=1

        return True
