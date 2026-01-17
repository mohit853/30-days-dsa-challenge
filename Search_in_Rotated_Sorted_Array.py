class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## we don't need to find k instead we need to find if we are
        ## able to perform in subsection of array
        n= len(nums)
        lo=0
        hi=n-1

        while lo<=hi:

            mid = (lo+hi) //2

            if nums[mid] == target:
                return mid
            

            if nums[lo] <= nums[mid]:
                
                if nums[lo] <=target < nums[mid] :
                    hi = mid-1
                else:
                    lo= mid+1
            else:

                if nums[mid] < target <= nums[hi]:
                    lo= mid+1
                else:
                    hi=mid-1

        return -1 
            
