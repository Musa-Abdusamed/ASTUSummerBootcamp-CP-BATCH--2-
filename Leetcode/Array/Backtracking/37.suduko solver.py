
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows   = [set() for _ in range(9)]
        cols   = [set() for _ in range(9)]
        boxes  = [set() for _ in range(9)]
        empty  = []

        # Initialize sets and collect empty cells
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    empty.append((i, j))    # track empty cells
                else:
                    box_idx = (i//3)*3 + (j//3)
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box_idx].add(val)

        def solve(idx):
            if idx == len(empty):           # all empty cells filled ✅
                return True

            r, c = empty[idx]
            box_idx = (r//3)*3 + (c//3)

            for num in "123456789":
                if num not in rows[r] and \
                   num not in cols[c] and \
                   num not in boxes[box_idx]:   # O(1) check ✅

                    # place
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if solve(idx+1):
                        return True

                    # undo
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            return False

        solve(0)
