class Solution:
    def reverseBits(self, n: int) -> int:

        ## testcase = 011
        ## o/p will be = 100

        ## since its 32 bits 0000..11(sum of digits =32)
        ## we need to reverse 32 bits

        res = 0

        for _ in range(32):
            res = res <<1
            res = res | n &1
            n= n >>1
        return res



        
        
