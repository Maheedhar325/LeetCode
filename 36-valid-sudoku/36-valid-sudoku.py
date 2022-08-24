class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        #check dup in rows
        for r in range(N):
            row = [v for v in board[r] if v!="."]
            if len(row) != len(set(row)): return False
            
        #check dup in cols
        for c in range(N):
            col = [board[r][c] for r in range(N) if board[r][c]!="."]
            if len(col) != len(set(col)):return False
        
        #check dup in boxes
        def helper(R,C):
            l = set()
            for r in range(R,R+3):
                for c in range(C,C+3):
                    if board[r][c] == ".": continue
                    if board[r][c] not in l:
                        l.add(board[r][c])
                    else:
                        return False
                    
            return True
        
        for R in range(0,N,3):
            for C in range(0,N,3):
                if not helper(R,C): return False
        return True
                    
        
        
        