class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        ## find vowel lenght of window k 

        vowels ={'a','e','i','o','u'}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count+=1

        ## intialize max_count
        max_count = count 

        ## loop from kth to n-1 
        n=len(s)
        for i in range(k,n):
            if s[i] in vowels:
                count+=1
            ## if i = 4 , k=3 , prev_start = 4-3 =1
            if s[i-k] in vowels:
                count-=1

            if count > max_count :
                max_count =count
        return max_count


        
