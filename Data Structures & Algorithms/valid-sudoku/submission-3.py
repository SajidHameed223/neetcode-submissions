class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if (
                        board[i][j] not in row[i]
                        and board[i][j] not in col[j]
                        and board[i][j] not in box[(i//3,j//3)]
                    ):
                        row[i].append(board[i][j])
                        col[j].append(board[i][j])
                        box[(i//3,j//3)].append(board[i][j])
                    else:
                        return False
        return True
