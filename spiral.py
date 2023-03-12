import math
import random 
n=int(random.randint(2,12))
m=int(random.randint(2,12))
print('n=',n)
print('m=',m)
a=[0]*n
for i in range(n):
    a[i]=[0]*m
d=1
k=0
def vnesh(n,m,k,d):
    h=k
    for j in range(m):
        if a[h][j]==0:
            a[h][j]=d
            d+=1
    l=m-1-k
    for i in range(n):
        if a[i][l]==0:
            a[i][l]=d
            d+=1 
    h=n-k-1
    for j in range(m-1,-1,-1):
        if a[h][j]==0:
            a[h][j]=d
            d+=1 
    l=k
    for i in range(n-1,0,-1):
        if a[i][l]==0:
            a[i][l]=d
            d+=1 
    return(d)
if n>=m:
    for i in range(math.ceil(m/2)):
        d=vnesh(n,m,k,d)
        k+=1
if n<m:
    for i in range(math.ceil(n/2)):
        d=vnesh(n,m,k,d)
        k+=1
for i in range(n):
    print(a[i])