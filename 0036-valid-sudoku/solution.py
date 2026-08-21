class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            num = set()

            for j in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in num:
                    return False

                num.add(board[i][j])

        # Check columns
        for j in range(9):
            num2 = set()

            for i in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in num2:
                    return False

                num2.add(board[i][j])

        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                num3 = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] in num3:
                            return False

                        num3.add(board[i][j])

        return True
