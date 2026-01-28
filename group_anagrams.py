class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_word = {}
        
        ##"eat" :['eat','ate']
        
        for word in strs:
            
            key= sorted(word) 
            ## bcd  -> ['b','c','d']
            key = "".join(key)
            if key not in hash_word:
                hash_word[key] = []
            
            hash_word[key].append(word)
        
        
        ans = []
        
        for value in hash_word.values():
            
            ans.append(value)
            
        return ans
        
        
        
        
