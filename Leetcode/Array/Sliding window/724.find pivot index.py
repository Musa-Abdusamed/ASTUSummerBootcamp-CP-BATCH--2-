

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lef, right = 0, sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if lef == right:
                return i
            lef += nums[i]
        return -1
