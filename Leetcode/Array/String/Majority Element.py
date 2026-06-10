#solved by ma
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=nums.sort()
        
        return nums[len(nums)/2]
        
