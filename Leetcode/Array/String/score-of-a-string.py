#solved by ma
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        for i in range(len(s)-1):
            l.append(abs(ord(s[i])-ord(s[i+1])))
        return sum(l)

        
