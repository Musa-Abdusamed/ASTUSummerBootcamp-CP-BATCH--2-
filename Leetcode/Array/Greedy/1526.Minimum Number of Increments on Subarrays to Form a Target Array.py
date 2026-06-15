#solved by ma



class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        
        """
        cur=prev=0
        for num in target:
            if num>prev:
                cur+=num-prev
            prev=num
        return cur

