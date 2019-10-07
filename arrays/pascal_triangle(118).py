class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            print(i)
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
