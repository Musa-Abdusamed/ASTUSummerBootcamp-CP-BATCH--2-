#solved by ma


class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ct=0
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i]+nums[j]<target and i<j:
                    ct+=1
        return ct
