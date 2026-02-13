class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        min_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i+1
            right = n - 1

            while left < right:  # since index needs to be different so no <=
                curr_sum = nums[i] + nums[left] + nums[right]

                # edge case1
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

                if abs(curr_sum- target) < abs(min_sum - target):
                    min_sum = curr_sum

        return min_sum
