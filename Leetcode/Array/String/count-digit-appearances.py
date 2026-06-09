#solved by ma
class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        st=''
        for i in range(len(nums)):
            st+=str(nums[i])
        return st.count(str(digit))
        
