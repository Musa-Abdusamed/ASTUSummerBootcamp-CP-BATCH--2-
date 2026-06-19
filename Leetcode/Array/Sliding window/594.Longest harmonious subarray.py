#Solved by ma

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m=0
        s=0
        n=len(nums)
        for i in range(1,n):
            while nums[i]-nums[s]>1:
                s=s+1
            if nums[i]-nums[s]==1:
                m=max(m,i-s+1)
        return m
        
