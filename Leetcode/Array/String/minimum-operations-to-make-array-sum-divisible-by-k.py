#Solution is here 👌 
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_sum=sum(nums)
        t=total_sum%k
        return t
        
