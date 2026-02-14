class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = paragraph.lower()
        clean = ""
        ## clean string would be string with words and each word is space separated
        for ch in paragraph:
            if ch.isalpha():
                clean += ch
            else:
                clean += " "
        words = clean.split()
        
        
        para_map ={}
        
        for word in words:
            if word not in para_map:
                para_map[word] =1
            else:
                para_map[word] +=1
                
        
        banned_set = set(banned)
        
        for s in banned_set:
            if s in para_map:
                para_map[s] =0
        
        max_len = -1
        ans = ""
        
        for key,val in para_map.items():
            if val > 0 and val > max_len:
                max_len = val
                ans = key
        
        
        return ans
        
        
