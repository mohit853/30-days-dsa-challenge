class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern_to_s ={}
        s_to_pattern = {}

        if len(s.split()) != len(pattern):
            return False
        i=0
        for word in s.split():
            ch = pattern[i]
            if ch in pattern_to_s and pattern_to_s[ch] != word :
                return False
            if  word in s_to_pattern and s_to_pattern[word] != ch:
                return False

            pattern_to_s[ch] = word
            s_to_pattern[word] =ch
            i+=1

        


        return True
