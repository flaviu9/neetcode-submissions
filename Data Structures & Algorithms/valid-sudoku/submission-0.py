class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if i not in rows:
                    rows[i] = set()
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if j not in cols:
                    cols[j] = set()
                if val in cols[j]:
                    return False
                cols[j].add(val)
                if (i//3, j//3) not in squares:
                    squares[(i//3,j//3)] = set()
                if val in squares[(i//3,j//3)]:
                    return False
                squares[(i//3,j//3)].add(val)
        return True
