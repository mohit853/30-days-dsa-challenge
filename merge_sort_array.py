class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        
        if len(nums) <=1:
            return nums
        mid = len(nums) // 2
        
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        return self.merge(left_half,right_half)
    
    
    def merge(self,left_list,right_list):
        
        n1 = len(left_list)
        n2 = len(right_list)
        i_n1 =0
        j_n2 =0
        
        sorted_list = []
        while i_n1 < n1 and j_n2 < n2:
            if left_list[i_n1] < right_list[j_n2]:
                sorted_list.append(left_list[i_n1])
                i_n1+=1
            else:
                sorted_list.append(right_list[j_n2])
                j_n2+=1
                
        sorted_list.extend(left_list[i_n1:])
        sorted_list.extend(right_list[j_n2:])
        return sorted_list

                
        
