class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum =0
        curr_sum =0

        for num in nums:
            curr_sum +=num

            min_sum = min(curr_sum , min_sum)
        
        return 1- min_sum
