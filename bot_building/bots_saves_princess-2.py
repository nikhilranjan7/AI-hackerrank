#!/usr/bin/env python3

def nextMove(n,r,c,grid):
    if 'p' in grid[r]:
        if grid[r].index('p')<c:
            print('LEFT')
        else:
            print('RIGHT')
    else:
        flag=0
        for i in range(0,r):
            if 'p' in grid[i]:
                print('UP')
                flag=1
        if flag==0:
            print('DOWN')

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

nextMove(n,r,c,grid)
