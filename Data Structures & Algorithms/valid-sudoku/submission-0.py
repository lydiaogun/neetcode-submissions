class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check if the element is in the row - using hashset because adding and looking is o(1)
        #check if the element is in the column - using hashet again
        #check if element is in the board
            # we use a handy trick here by dividing the row and column value by 3 to see if its in the 3 x3 box

        #create hashsets to store the column, row and square
        cols= defaultdict(set)
        row = defaultdict(set)
        square= defaultdict(set)

        #iterating each row and each column remember the double for loops from first year to look across a 2-d array (not really 2-d here)
        for r in range (9):
            for c in range(9):
                #check if its empty
                if board[r][c] == ".":
                    continue
                #check if we have already seen it in the seen sets
                if (board[r][c] in row[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3, c//3)]):
                    return False
                #if not seen add it to the appropriate sets
                cols[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True

