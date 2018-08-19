def solve(board):
    print_board(board)
    made_progress = True
    while made_progress and not is_complete(board):
        made_progress = False
        # check for rows with 1 digit missing
        for row in board:
            missing = set([i+1 for i in range(9)]).difference(set([n for n in row if n != 0]))
            if len(missing) == 1:
                row[row.index(0)] = missing.pop()
                made_progress = True

        # check for cols with 1 digit missing

        # check for boxes with 1 digit missing

        # check for spaces with only 1 possibility
        boards = []
        for i in range(9):
            poss = get_possible(board, i+1)
            boards.append(poss)
        boards.append(board)
        for i in range(9):
            for j in range(9):
                nums = [b[i][j] for b in boards]
                nums = [n for n in filter(lambda x: x, nums)]
                if len(nums) == 1:
                    board[i][j] = nums[0]
                    made_progress = True
        # print board after each iteration for debugging
        print_board(board)
    return board


def get_possible(board, n):
    possible = [[0 for i in range(9)] for i in range(9)]

    rows = board
    cols = [col for col in zip(*board)]

    boxes = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            boxes.append(box)

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                cur_box = boxes[int(i/3) + 3 * int(j/3)]
                if n not in rows[i] + list(cols[j]) + cur_box:
                    possible[i][j] = n
    return possible

def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True

def is_won(board): #board[i][j]
  ok = True
  # check rows
  for row in board:
    if 0 not in row and len(set(row)) != 9:
      ok = False
      break
  # check cols
  if ok:
    for col in zip(*board):
        if len(set(col)) != 9:
            ok = False
            break
  # check boxes
  if ok:
      for i in range(0, 9, 3):
          for j in range(0, 9, 3):
            box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if len(set(box)) != 9:
                ok = False
                break
  
  return ok

def print_board(board):
    print('-' * 17)
    for row in board:
        print('{} {} {} {} {} {} {} {} {}'.format(*row))
    print('-' * 17)