class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n :

            count = count + (n&1) ## check if last digit is set and add 1 if true 
            n = n >> 1
        return count


        
