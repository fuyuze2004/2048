from random import randint
import time

def game(name):
    with open(name, 'a') as log:
        board = [[0 for j in range(4)] for i in range(4)]
        score = 0
        two_four(board, 0)
        two_four(board, 0)
        print('Welcome to the game of 2048!')
        print('Welcome to the game of 2048!', file = log)
        output(board, score, log)
        start = time.strftime('%Y%m%d %H:%M:%S' ,time.localtime())
        op = time.time()
        while not (is_full(board) and is_eat(board)):
            d = order(log)
            if d == 'q':
                break
            if d == 'r':
                lr(board)
            elif d == 'u':
                ud(board)
            elif d == 'd':
                ud(board)
                lr(board)
            move(board)
            score = eat(board, score)
            move(board)
            if d == 'r':
                lr(board)
            elif d == 'u':
                ud(board)
            elif d == 'd':
                lr(board)
                ud(board)
            two_four(board, 1)
            output(board, score, log)
        ed = time.time()
        long = str(int(ed - op))
        result = start + ',' + long + ',' + str(score)
        with open('game2048.csv', 'a') as table:
            print(result, file = table)
        print('Game Over')
        print('Game Over', file = log)
    
def output(board, score, log):
    for i in range(4):
        print('|-----|-----|-----|-----|')
        print('|-----|-----|-----|-----|', file = log)
        for j in range(4):
            s = ' '
            if board[i][j]:
                s = str(board[i][j])
            print('|{:^5s}'.format(s), end = '')
            print('|{:^5s}'.format(s), end = '', file = log)
        print('|')
        print('|', file = log)
    print('|-----|-----|-----|-----|')
    print('|-----|-----|-----|-----|', file = log)
    print('Your score:', score)
    print('Your score:', score, file = log)

def two_four(board, flag):
    five = [2 for i in range(4)]
    five.append(4)
    x, y = randint(0, 3), randint(0, 3)
    while board[x][y]:
        x, y = randint(0, 3), randint(0, 3) 
    if not flag:
        board[x][y] = 2
    else:
        board[x][y] = five[randint(0, 4)]

def order(log):
    while True:
        s = input('(↑:u)(↓:d)(←:l)(→:r)(quit:q): ')
        print('(↑:u)(↓:d)(←:l)(→:r)(quit:q):' + s, file = log)
        if s == 'u' or s == 'd' or s == 'l' or s == 'r' or s == 'q':
            return s

def move(board):
    for i in range(4):
        cnt = 0
        for j in range(4):
           if not board[i][j]:
               cnt += 1
        for temp in range(cnt):
            board[i].remove(0)
            board[i].append(0)
            
def eat(board, score):
    for i in range(4):
        j = 0
        while j < 3:
            if board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0
                score += board[i][j]
                j += 2
            else:
                j += 1
    return score
                
def lr(board):
    for i in range(4):
        board[i].reverse()
def ud(board):
    for i in range(4):
        for j in range(i + 1):
            board[i][j], board[j][i] = board[j][i], board[i][j]

def is_full(board):
    for r in board:
        for e in r:
            if not e:
                return 0
    return 1

def is_eat(board):
    for i in range(4):
        for j in range(4):
            if i - 1 >= 0 and board[i][j] == board[i - 1][j] or i + 1 <= 3 and board[i][j] == board[i + 1][j] or j - 1 >= 0 and board[i][j] == board[i][j - 1] or j + 1 <= 3 and board[i][j] == board[i][j + 1]:
                    return 0
    return 1
    
if __name__ == '__main__':
    name = 'game2048-{}.log'.format(str(randint(10000, 99999)))
    game(name)
