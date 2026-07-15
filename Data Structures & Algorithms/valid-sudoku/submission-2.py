class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                key = (i//3 , j//3)
                if val == ".": continue
                if val in row[i] or val in col[j] or val in box[key]: return False
                row[i].add(val)
                col[j].add(val)
                box[key].add(val)
        return True