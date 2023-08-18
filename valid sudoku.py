class Solution:
    # check row
    def check2D(self, board: List[List[str]], number) -> bool:
        for row in board:
            unique = []
            for num in row:
                if num == ".":
                    continue
                if num not in unique:
                    unique.append(num)
                else:
                    print(number)
                    print(unique, num)
                    return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = []
        NUMBERS = 9
        BOXSIZE = 3
        for i in range(NUMBERS):
            col = []
            for row in board:
                col.append(row[i])
            cols.append(col)
   
        j = 0
        k = 0
        boxes = []
        while (k < 3):
            box = []
            for i in range(NUMBERS):
                row = board[i][j:j+BOXSIZE]
                box.append(row)
                if (i % BOXSIZE == 2):
                    boxes.append(box)
                    box = []
            k += 1
            j += BOXSIZE

        newBoxes = []
        for row in boxes:
            newtxt = []
            for txt in row:
                newtxt += txt
            newBoxes.append(newtxt)
        return self.check2D(board,1) and self.check2D(cols,2) and self.check2D(newBoxes,3)