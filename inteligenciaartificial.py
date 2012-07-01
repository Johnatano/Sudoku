'''
Created on 24/06/2012

@author: Johnatan
'''

m=[
[0,0,0,   0,0,6,  0,8,0],
[0,8,0,   0,5,0,  6,7,0],
[0,0,2,   0,0,3,  0,5,1],


[1,0,0,   2,7,0,  0,0,0],
[0,0,7,   6,0,8,  2,0,0],
[0,0,0,   0,1,4,  0,0,7],


[5,2,0,   4,0,0,  7,0,0],
[0,4,3,   0,8,0,  0,6,0],
[0,9,0,   1,0,0,  0,0,0]
]






















def doit():
    i,j=pz()
    if i==-1:return 1
    for n in range(1,10):
        if linok(i,j,n) and colok(i,j,n) and quadok(i,j,n):
            m[i][j]=n
            if doit():return 1
    m[i][j]=0
    return 0

def linok(i,p,n):
    for j in range(9):
        if m[i][j]==n:return 0
    return 1

def colok(p,j,n):
    for i in range(9):
        if m[i][j]==n: return 0
    return 1

def quadok(i,j,n):
    li=(i/3)*3
    lj=(j/3)*3
    for x in range(li,li+3):
        for y in range(lj,lj+3):
            if m[x][y]==n: return 0
    return 1

def pz():
    for i in range(9):
        for j in range(9):
            if m[i][j]==0:return i,j
    return -1,0

for p in m: print p
doit()
print
for p in m: print p
