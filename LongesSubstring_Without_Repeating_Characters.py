class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i=0 
        max_len =1
        n= len(s)
        my_dict = {s[0] :1} if s else {}

        for j in range(1,n):

            if s[j] in my_dict:
                while s[j] != s[i]:
                    del my_dict[s[i]]
                    i+=1
                del my_dict[s[i]]
                i+=1
            curr_len = j-i+1
            max_len = max(curr_len,max_len)
            my_dict[s[j]] = 1
        return max_len

