class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ## for first occurence will we apply binary search on left of  mid
        ## for right occurence we will apply binary search on right of mid  

        left =0
        right = len(nums)-1
        def binarySearch(left,right,is_search_left):
            idx=-1

            while left <= right:
                mid= (left+right)//2

                if nums[mid] > target:
                    right = mid -1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    idx=mid
                    if is_search_left:
                        right=mid-1
                    else:
                        left=mid+1
            

            return idx

            
        



        l_idx =binarySearch(left, right, True)
        r_idx = binarySearch(left, right, False)

        return [l_idx,r_idx]
