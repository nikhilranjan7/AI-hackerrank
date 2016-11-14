#!/usr/bin/env python3

def printa(s):
    for i in range(0,m//2):
        print(s)

def displayPathtoPrincess(n,grid):
    #print all the moves here
    if 'p' in grid[-1]:
        printa('DOWN')
        if (grid[-1].index('p'))!=0:
            printa('RIGHT')
        else:
            printa('LEFT')
    else:
        printa('UP')
        if (grid[0].index('p'))!=0:
            printa('RIGHT')
        else:
            printa('LEFT')

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
