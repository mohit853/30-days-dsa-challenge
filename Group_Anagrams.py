class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        my_dict ={}

        for word in strs:

            new_word = ''.join(sorted(word))

            if new_word not in my_dict:
                my_dict[new_word] =[]

            my_dict[new_word].append(word)
        
        return list(my_dict.values())
        
