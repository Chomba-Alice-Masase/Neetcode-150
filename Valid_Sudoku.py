from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rules = 0 # if = 3, then board is valid. else is not valid.
        # We could check for duplicates to handle row validation.
        for i in range(0,9):
            for j in board[i]:

                if j != "." and board[i].count(j) > 1:
                    return False
        rules += 1
        print(rules)

        # We try and handle column validation here.
        column_dict = defaultdict(list)
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != ".":
                    column_dict[j].append(board[i][j])

        for value in column_dict.values():
            for i in value:
                if value.count(i) > 1:
                    return False
        rules += 1
        print(rules)

        # To check for squares, we'll create lists of 9 to represent the diff squares.
        squares = []

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                for k in range(3):
                    for l in range(3):
                        square.append(board[i + k][j + l])
                squares.append(square)
        
        print(squares)

        for i in range(0,9):
            for j in squares[i]:
                if squares[i].count(j) > 1 and j != '.':
                    return False
        rules += 1
        print(rules)
        # Then we perform the final check
        if rules == 3:
            return True
