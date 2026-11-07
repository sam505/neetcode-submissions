class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(list)
        columns = collections.defaultdict(list)
        cells = collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i] or num in columns[j] or num in cells[(i//3, j//3)]:
                    print(rows, columns, cells, num, i, j)
                    return False
                else:
                    rows[i].append(num)
                    columns[j].append(num)
                    cells[(i//3, j//3)].append(num)

        return True
                