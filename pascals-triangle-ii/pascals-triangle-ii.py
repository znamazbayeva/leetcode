class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        arr = [[0]*n for n in range(1,35)]
        def helper(row, col):
            if row >= 0 and col >= 0 and col <=row and arr[row][col] != 0:
                return arr[row][col]
            if row == 0:
                return 1
            if col == 0 or col == row:
                return 1
            elif col > row or col < 0:
                return 0
            arr[row][col] = helper(row-1, col-1) + helper(row-1, col)
            return arr[row][col]
        res = []
        for i in range(rowIndex + 1):
            res.append(helper(rowIndex, i))
        return res