#!/usr/bin/env python3

# Head ends here
def near(a,b,c,d):
    return (((a-b)**2) + ((c-d)**2))

def next_move(posr, posc, board):
    mini=99999999
    for i in range(0,len(board)):
        if 'd' in board[i]:
            drow=i
            for j in range(0,len(board[i])):
                if 'd'==board[i][j]:
                    cal=near(posr,i,posc,j)
                    if cal<mini:
                        mini=cal
                        x=i
                        y=j
    if mini==0:
        print('CLEAN')
    else:
        if x==posr:
            if posc<y:
                print('RIGHT')
            else:
                print('LEFT')
        elif y==posc:
            if posr<x:
                print('DOWN')
            else:
                print('UP')
        else:
            if posc<y:
                print('RIGHT')
            else:
                print('LEFT')


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
