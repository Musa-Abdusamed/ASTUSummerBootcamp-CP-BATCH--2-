#solved by ma

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """method1 built-in
        import statistics 
        l=nums1+nums2
        l.sort()   gives same result with method2
        return statistics.median(l)"""
        #method2 manual/calculation  without library
        l=nums1+nums2
        l.sort()
        mid=len(l)//2
        
    
        if len(l)%2!=0:
            return l[mid]
        else:
            return (l[mid]+l[mid-1])/2
