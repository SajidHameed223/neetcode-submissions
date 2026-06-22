class Solution:
    def isValidSudoku(self, borad: List[List[str]]) -> bool:
        rows = defaultdict(set) 
        cols = defaultdict(set) 
        squares = defaultdict(set) 
        for r in range(9):
            for c in range(9):
                if borad[r][c] == '.':
                    continue
                if borad[r][c] in rows[r] or borad[r][c] in cols[c] or borad[r][c] in squares[r//3 , c//3]:
                    return False
                rows[r].add(borad[r][c])    
                cols[c].add(borad[r][c])
                squares[r//3 , c//3].add(borad[r][c])
        return True            
                        
        