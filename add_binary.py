class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a_len = len(a) 
        b_len = len(b)  

        i= a_len -1
        j = b_len -1
        carry = 0
        res=""

        while i>=0 or j>=0 or carry:

            val1 = int(a[i]) if i>=0 else 0
            val2 = int(b[j])  if j >=0 else 0

            total = val1+ val2+ carry
            res += str(total %2)
            carry = total //2

            i-=1
            j-=1
        
        final_ans =""
        n = len(res)
        for i in range(n-1,-1,-1):
            final_ans += res[i]

        
        return final_ans
        
