# Solved ma

class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        """
        n=len(nums)
        l=0
        r=n-1
        cot=0
        for i in range(l,r):
            if nums[i-1]%2!=nums[i]%2 and nums[i]<=threshold:
                cot+=1
        return cot    """    

        n = len(nums)
        l = 0
        r = n
        cot = 0
        best = 0
        for i in range(l, r):
            if nums[i] % 2 == 0 and nums[i] <= threshold:  # valid start
                cur = 1
                j = i + 1
                while j < n and nums[j] <= threshold and nums[j] % 2 != nums[j-1] % 2:
                    cur += 1
                    j += 1
                best = max(best, cur)
        return best
