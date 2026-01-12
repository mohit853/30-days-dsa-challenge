class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        my_dict ={}

        for i in range(len(nums)):
            curr=nums[i]
            if curr in my_dict and abs(i-my_dict[curr] <=k):
                return True

            my_dict[curr] =i
        

        return False
