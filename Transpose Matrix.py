#solved by ma

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
         #method 1
        transposed=[[matrix[row][col] for row in range(len(matrix))]for col in range(len(matrix[0])) ]
        return transposed  #this is fast than method 2



        # method 2
        #transposed=[list(row) for row in zip(*matrix)]
        #return transposed
        
