class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        if not s:
            return ""
        
        lps = s[0]
        n= len(s)

        

        def expansion(left,right):
            
            while left >=0 and right <n and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1 : right]
        
        
        for mid in range(n):
            
            
            ## expansion done of possible odd length  pallindromes
            
            odd_pallindrome_mid = expansion(mid-1,mid+1)
            ## expansion done of possible even length pallindromes
            
            even_pallindrome_mid = expansion(mid,mid+1)
            
            if len(odd_pallindrome_mid) > len(lps):
                lps = odd_pallindrome_mid
            
            if len(even_pallindrome_mid) > len(lps):
                lps = even_pallindrome_mid
        
        

            
        
        
        
        
        
        
        
        
        return lps
