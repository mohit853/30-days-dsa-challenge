class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed =[]

        for ch in s:

            if  ch.isalnum() :
                processed.append(ch.lower())
        
        start = 0 
        end = len(processed)-1

        while start < end:
            if processed[start] != processed[end]:
                return False
            start+=1
            end-=1

        return True

