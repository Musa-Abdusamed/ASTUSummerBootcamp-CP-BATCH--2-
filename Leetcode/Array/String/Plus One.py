# solved by ma

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        st=""
        num=0
        emp=[]
        for i in range(len(digits)):
            st+=str(digits[i])
        num+=int(st)+1
        num1=str(num)
        for j in range(len(num1)):
            emp.append(int(num1[j]))

        return emp
