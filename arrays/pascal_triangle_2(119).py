class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [[1]*(i+1) for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal[rowIndex]
